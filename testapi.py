#!/usr/bin/python
'''
 -*- coding: utf-8 -*-
 some useful class
'''

from __future__ import print_function
import subprocess
import time
import re
import pexpect
from pexpect import pxssh

class ConnectionException(Exception):
    ''' connection related '''
    pass

class Executable(object):
    ''' virtual interface , all the inherent should implement execute_cmd'''
    #execute cmd
    # result - list of text line
    def execute_cmd(self, cmd, timeout=-1):
        pass
    def execute_cmd_state(self, cmd):
        lines = self.execute_cmd(cmd + ' 1>/dev/null 2>/dev/null; echo $?')
        return int(lines[0])

class TerminalSession(Executable):
    ''' The base class for terminal application'''
    def __init__(self):
        self._handle = None
        self._prompt = None

    def __del__(self):
        self.disconnect()

    def set_prompt(self, prompt):
        self._prompt = prompt

    def disconnect(self):
        if self._handle != None and self._handle.isalive():
            self._handle.close()
            self._handle = None

    def is_connected(self):
        return self._handle != None and self._handle.isalive()

    def reconnect(self):
        pass

    def is_online(self, timeout=0):
        if self.is_connected():
            return True
        while timeout > 0:
            if self.reconnect():
                return True
            else:
                time.sleep(1)
                timeout -= 1
        return False

    def _send(self, cmdstr):
        if self._handle != None and self._handle.isalive():
            self._handle.sendline(cmdstr)
            self._handle.flush()
        else:
            raise ConnectionException

    def _recv(self, timeout):
        if self._handle != None and self._handle.isalive():
            try:
                self._handle.expect(self._prompt, timeout=timeout)
                #print("B=> " + self._handle.before.encode('string-escape'))
                #print("M=> " + self._handle.match.group() .encode('string-escape'))
                #print("A=> " + self._handle.after.encode('string-escape'))
                return self._handle.before
            except pexpect.TIMEOUT:
                #print("TIMEOUT")
                return
            except pexpect.EOF:
                self._handle = None
                raise ConnectionException
        else:
            raise ConnectionException


    def execute_cmd(self, cmd, timeout=-1):
        cmd = cmd.rstrip()
        self._send(cmd)
        while True:
            buf = self._recv(timeout)
            if buf is None:
                break
            lines = buf.replace('\r', '').splitlines()
            if len(lines) > 0:
                if lines[0] == cmd:
                    del lines[0]
                    return lines
    def _exit(self):
        self.execute_cmd('exit')

    def setwinsize(self, row, cols):
        self.execute_cmd('stty rows {} cols {}'.format(row, cols))
        self._handle.setwinsize(row, cols)

    # This sends a control character to the child such as Ctrl-C or
    # Ctrl-D. For example, to send a Ctrl-G (ASCII 7)::
    # sendcontrol('g')
    def sendcontrol(self, char):
        self._handle.sendcontrol(char)

    def test(self):
        while True:
            cmd = raw_input(":")
            print(self.execute_cmd(cmd), sep='\n')


class AdbSession(TerminalSession):
    ''' adb terminal session '''
    def __init__(self):
        super(AdbSession, self).__init__()
        self._prompt = ['/[^\"\'\r\n ]* # ', '/[^\"\'\r\n ]* $ ']
        self._device = None

    def connect(self, device=None):
        self.disconnect()
        dev = '' if device is None else '-s ' + device
        self._handle = pexpect.spawn("adb shell " + dev)
        self.setwinsize(25, 400)
        self._device = device
        return self.is_connected()

    def reconnect(self):
        if self.is_connected():
            return True
        return self.connect(self._device)

class NetAdbSession(TerminalSession):
    ''' adb terminal session and connect through internet'''
    def __init__(self):
        super(NetAdbSession, self).__init__()
        self._prompt = ['/[^\"\'\r\n ]* # ', '/[^\"\'\r\n ]* $ ']
        self._host = None
        self._port = None

    def connect(self, host, port=5037):
        self.disconnect()
        self._handle = pexpect.spawn("adb connect {}:{}".format(host, port))
        self.setwinsize(25, 400)
        self._host = host
        self._port = port
        return self.is_connected()

    def reconnect(self):
        if self.is_connected():
            return True
        return self.connect(self._host, self._port)

class SSHSession(TerminalSession):
    ''' SSH terminal session '''
    def __init__(self):
        super(SSHSession, self).__init__()
        self._host = None
        self._user = None
        self._password = None

    def connect(self, host, user, password):
        self.disconnect()
        try:
            self._handle = pxssh.pxssh()
            self._handle.login(host, user, password)
            self.setwinsize(25, 400)
        except pxssh.ExceptionPxssh as ex:
            print("pxssh failed on login.")
            print(ex)
            self._handle = None
        self._host = host
        self._user = user
        self._password = password
        return self.is_connected()

    def reconnect(self):
        if self.is_connected():
            return True
        return self.connect(self._host, self._user, self._password)

    def _recv(self, timeout=-1):
        if self._handle != None and self._handle.isalive():
            try:
                self._handle.prompt(timeout=timeout)
                return self._handle.before
            except pexpect.TIMEOUT:
                #print("TIMEOUT")
                return
            except pexpect.EOF:
                self._handle = None
                raise ConnectionException
        else:
            raise ConnectionException

class ProcSession(TerminalSession):
    ''' one process terminal session '''
    def __init__(self):
        super(ProcSession, self).__init__()

    def start(self, cmd):
        self.disconnect()
        self._prompt = '\r\n'
        self._handle = pexpect.spawn(cmd)
        return self.is_connected()

    def readline(self, timeout=-1):
        return self._recv(timeout)

    def test(self):
        while True:
            line = self.readline(0.5)
            if line:
                print(line)

class LinuxBox(Executable):
    ''' linux OS interface, it must be inherent and implement the execute_cmd '''
    def __init__(self):
        super(LinuxBox, self).__init__()

    def ifconfig(self, dev_name, params):
        self.execute_cmd('ifconfig {} {}'.format(dev_name, params))

    def iperfs(self, local_ip):
        self.execute_cmd('iperf -u -s -B {} -fk -i 1 > /tmp/iperf.log'.format(local_ip), 0)

    def iperfc(self, remote_ip, bps, length):
        self.execute_cmd('iperf -u -c {} -b {} -l {} -t 600 -i 1 >/dev/null&'.format(remote_ip, bps, length), 0)

    def iperfs_tcp(self, local_ip):
        self.execute_cmd('iperf -s -B {} -fk -i 1 > /tmp/iperf.log'.format(local_ip), 0)

    def iperfc_tcp(self, remote_ip, length):
        self.execute_cmd('iperf -c {} -l {} -t 600 -i 1 >/dev/null&'.format(remote_ip, length))

    def killall(self, proc):
        self.execute_cmd('killall {}'.format(proc))

    def reboot(self):
        self.execute_cmd('reboot')

   #create vlan interface for dev
    def set_vlan(self, dev, vlan_id, addr=''):
        self.execute_cmd('ip link add link {} name {}.{} type vlan id {}'.\
                    format(dev, dev, vlan_id, vlan_id))
        self.execute_cmd('ifconfig {}.{} up {}'.format(dev, vlan_id, addr))

    #delete vlan interface for dev
    def del_vlan(self, dev, vlan_id):
        if vlan_id is not None:
            self.del_dev('{}.{}'.format(dev, vlan_id))
        else:
            for vid in range(255):
                dev_name = '{}.{}'.format(dev, vid)
                if self.execute_cmd_state('ip address show ' + dev_name) == 0:
                    self.del_dev(dev_name)

    def release_dhcp(self, dev):
        self.execute_cmd('dhclient -r  {}'.format(dev))

    def del_dev(self, dev):
        self.execute_cmd('ip link delete  {}'.format(dev))

    def insmod(self, kmod):
        self.execute_cmd('insmod   {}'.format(kmod))

    def rmmod(self, kmod):
        self.execute_cmd('rmmod   {}'.format(kmod))
    #get interface parameter
    #@retal -- {mtu:, inet:, cid, mac}
    def get_ifconfig(self, dev):
        lines = self.execute_cmd('ip addr show dev {}'.format(dev))
        retval = {}
        for line in lines:
            result = re.search(r'mtu\s(\d+)', line)
            if result:
                retval['mtu'] = result.group(1)
            result = re.search(r'link/ether\s([\w:]*)', line)
            if result:
                retval['mac'] = result.group(1)
            result = re.search(r'inet\s([\d.]*)/(\d*)', line)
            if result:
                retval['inet'] = result.group(1)
                retval['cid'] = result.group(2)
        return retval
    #param gre_name -- gre interface name.
    #param dev_name -- gate device for gre
    #param remote_ip -- IP on remote gate device
    #param mpls     -- mpls_labe, default 4001
    def create_gre(self, gre_name, dev_name, remote_ip, mpls=None):
        mpls = 4001 if mpls is None else mpls
        flags = 0x1e3
        ip_config = self.get_ifconfig(dev_name)
        if ip_config['inet']:
            self.execute_cmd('ip link add  {} type vc'.format(gre_name))
            self.execute_cmd('ip vcconf {} remote {} local {} mpls-label {}  flags {}'\
                .format(gre_name, remote_ip, ip_config['inet'], mpls, flags))
            self.execute_cmd('ifconfig {} mtu {} up'.format(gre_name, int(ip_config['mtu'])-42))

    #param dev_name -- interface name
    #param mac      -- mac address for gre interface
    def set_mac(self, dev_name, mac):
        self.execute_cmd('ip link set  {} down; ifconfig {} hw ether {} up '.format(dev_name, dev_name, mac))

    #param br_name  -- bridge interface name
    #param intfs  --- list of interface attached to br_name
    def set_bridge(self, br_name, intfs):
        self.execute_cmd('brctl addbr {}'.format(br_name))
        for intf in intfs:
            self.execute_cmd('brctl addif {} {}'.format(br_name, intf))

class TestRouter(LinuxBox):
    ''' the Test router with linux OS '''
    def __init__(self):
        super(TestRouter, self).__init__()
        self._params = []
        self._connection = None

    def connect_adb(self, device=None):
        self._params = [device]
        self._connection = AdbSession()
        return self._connection.connect(*self._params)

    def disconnect(self):
        return self._connection.disconnect()

    def is_online(self, timeout=0):
        return self._connection.is_online(timeout)

    def execute_cmd(self, cmd, timeout=-1):
       # print(cmd)
        return self._connection.execute_cmd(cmd, timeout)

    def test(self):
        cmd = ''
        while True:
            print(self.execute_cmd(cmd))
            cmd = raw_input(":")

    def rdb_set(self, rdb_name, value, flag=None):
        #print(rdb_name + ' => ' + str(value))
        flag = '' if flag is None else '-' + flag
        self.execute_cmd('rdb_set {} {} {}'.format(flag, rdb_name, value), 3)

    def rdb_unset(self, rdb_name):
        #print('delete ' + rdb_name)
        self.execute_cmd('rdb_del {}'.format(rdb_name), 3)

    def rdb_get(self, rdb_name):
        value = self.execute_cmd('rdb_get {}'.format(rdb_name), 3)
        if len(value) == 1:
            return value[0]

    def rdb_list(self, rdb_name):
        return self.execute_cmd('rdb_get -l {}'.format(rdb_name))

    def rdb_watch(self, rdb_name, timeout):
        self.execute_cmd('rdb_wait {} {}'.format(rdb_name, timeout), timeout)
        return self.rdb_get(rdb_name)

    def rdb_list_value(self, rdb_name):
        return self.execute_cmd('rdb_get -L {}'.format(rdb_name))

    def sendcontrol(self, char):
        self._connection.sendcontrol(char)

class TestBed(LinuxBox):
    ''' The test machine with linux OS'''
    def __init__(self):
        super(TestBed, self).__init__()

    def execute_cmd(self, cmd, timeout=-1):
        print(cmd)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        result = process.communicate()
        return result[0].splitlines()

    @staticmethod
    def wait(seconds):
        #print("wait {}".format(seconds))
        time.sleep(seconds)

    def adb_pull(self, remote_path, local_path):
        self.execute_cmd('adb pull {} {}'.format(remote_path, local_path))

    def adb_push(self, local_path, remote_path):
        self.execute_cmd('adb push {} {}'.format(local_path, remote_path))

    @staticmethod
    def scp_pull(remote_pathname, local_path, passwd):
        #scp  username@hostname:pathdir/file.ext  pathdir/
        scp_cmd = 'scp {} {}'.format(remote_pathname, local_path)
        print(scp_cmd)
        child = pexpect.spawn(scp_cmd)
        retval = child.expect(["password:", pexpect.EOF])
        if retval == 0: # send password
            child.sendline(passwd)
            child.expect(pexpect.EOF)
        elif retval == 1:
            print("Got the key or connection timeout")

    @staticmethod
    def scp_push(local_file, remote_pathname, passwd):
        #scp pathdir/file.ext username@hostname:pathdir
        scp_cmd = 'scp {} {}'.format(local_file, remote_pathname)
        print(scp_cmd)
        child = pexpect.spawn(scp_cmd)
        retval = child.expect(["password:", pexpect.EOF])
        if retval == 0: # send password
            child.sendline(passwd)
            child.expect(pexpect.EOF)
        elif retval == 1:
            print("Got the key or connection timeout")

class TestServer(LinuxBox):
    def __init__(self):
        super(TestServer, self).__init__()
        self._params = []
        self._connection = None

    def connect_ssh(self, host, user, passwd):
        self._connection = SSHSession()
        self._params = [host, user, passwd]
        return self._connection.connect(host, user, passwd)

    def disconnect(self):
        return self._connection.disconnect()

    def is_online(self, timeout=0):
        return self._connection.is_online(timeout)

    def execute_cmd(self, cmd, timeout=-1):
        print(cmd)
        return self._connection.execute_cmd('sudo ' + cmd, timeout)

    def sendcontrol(self, char):
        self._connection.sendcontrol(char)

class TestLog(object):
    ''' Test log and step track'''
    def __init__(self):
        self._step = [0, 0]
        self._step_msg = ['', '']
        self._step_level = 0
        self._msg_list = []

    def _get_step_info(self, msg):
        step_name = '.'.join(str(x) for x in self._step[ :self._step_level+1])
        return step_name, msg if msg is not None else self._step_msg[self._step_level]

    def record_fail(self, msg=None):
        step_name, msg = self._get_step_info(msg)
        self._msg_list.append([step_name, 'fail', msg])
        print("Result fail: " + msg)

    def record_success(self, msg=None):
        step_name, msg = self._get_step_info(msg)
        self._msg_list.append([step_name, 'success', msg])
        print("Result success : " + msg)

    def record_info(self, msg):
        step_name, msg = self._get_step_info(msg)
        self._msg_list.append([step_name, 'info', msg])
        print(msg)

    def test_step(self, msg, level=0, step=None):
        if level in range(len(self._step)):
            self._step_level = level
            self._step_msg[level] = msg
            if step is not None:
                self._step[level] = step
            else:
                self._step[level] = self._step[level] + 1
            step_name, msg = self._get_step_info(msg)
            self._msg_list.append([step_name, 'step', msg])
            print('Test '+step_name, ': ', msg)
        else:
            raise Exception

if __name__ == '__main__':
    '''
    r = TestRouter()
    r.connect_adb()
    r.disconnect()
    print(r.is_online(10))
    #r.rdb_set('avc.1.dscp_to_cos', '0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
    #print(r.rdb_list_value('vlan'))
    #print(r.rdb_get('avc.1.dscp_to_cos'))
    raw_input()
    r.del_dev('gre10')
    r.create_gre('gre10', 'rmnet_data1', '172.22.5.51', 3001)
    r.set_mac('gre10', 'D6:56:4B:DB:A8:00')
    r.ifconfig('gre10 192.168.31.33')
    r.set_bridge('br10', ['gre10'])
    '''

    ts = TestServer()
    ts.connect_ssh('172.22.5.51', "leeh", "thesis10")
    #s.test()

    #ts.create_gre('gre10', 'eth0', '192.168.4.2')
    ts.execute_cmd("ping 172.22.5.50", 0)
    raw_input('ctrol-c')
    ts.sendcontrol('c')
    raw_input()


    s = TestBed()
    '''
    print(s.execute_cmd('ls'))
    print(s.ifconfig('eth0 0'))
    print(s.set_vlan('eth0', 1, '192.168.31.33'))
    s.del_vlan('eth0', 1)
    p= ProcSession()
    p.start("ping 172.22.3.60")

    p.test()

    s.adb_push("result.log", '/tmp')
    s.adb_pull("/tmp/sshd.pid", './')
    s.scp_push('result.log', 'leeh@172.22.5.51:/tmp', 'thesis10')
    s.scp_pull('leeh@172.22.5.51:/mnt/vbox/gre1.pcap', './', 'thesis10')
    '''
    print(s.get_ifconfig('eth0'))

