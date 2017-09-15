#!/usr/bin/python
from __future__ import print_function

import re
import sys

TEST_STEP=0
def testStep(desc, step=None):
    global TEST_STEP
    TEST_STEP = TEST_STEP + 1 if step is None else step
    print('\n{}: {}'.format(TEST_STEP, desc))

testStep("built-in", 0)


'''
16 divmod(a, b)
Take two (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division.
With mixed operand types, the rules for binary arithmetic operators apply.
For integers, the result is the same as

(a // b, a % b).

For floating point numbers the result is

(q, a % b),

where q is usually math.floor(a / b) but may be 1 less than that.
In any case

q * b + a % b

is very close to a, if a % b is non-zero it has the same sign as b, and 0 <= abs(a % b) < abs(b)
'''
testStep("divmode", 16)
print(divmod(0,10))

print(divmod(1,10))
print(divmod(11,10))

print(divmod(10.10,10))

'''
17 enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0) and the corresponding value obtained from iterating over iterable. enumerate() is useful for obtaining an indexed series:

 (0, seq[0]), (1, seq[1]), (2, seq[2]), .... 

For example:
'''
testStep("enumerate")
for i, season in enumerate(['Spring', 'Summer', 'Fall', 'Winter']):
     print(i, season)

for i, season in enumerate({1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}):
     print(i, season, type(season))


'''
18 eval(expression, globals=None, locals=None)
The arguments are a string and optional globals and locals.
If provided, globals must be a dictionary. If provided, locals can be any mapping object. The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace.
If the globals dictionary is present and lacks __builtins__, the current globals are copied into globals before expression is parsed.
This means that expression normally has full access to the standard builtins module and restricted environments are propagated.
If the locals dictionary is omitted it defaults to the globals dictionary.
If both dictionaries are omitted, the expression is executed in the environment where eval() is called.
The return value is the result of the evaluated expression. Syntax errors are reported as exceptions.
'''
testStep("eval")
X=1
print(eval('print(X+10)'))

'''
19 exec(object[, globals[, locals]])
This function supports dynamic execution of Python code.
object must be either a string or a code object.
If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs).
If it is a code object, it is simply executed.
In all cases, the code that's executed is expected to be valid as file input.
Be aware that the return and yield statements may not be used outside of function definitions even within the context of code passed to the exec() function.
The return value is None.
In all cases, if the optional parts are om
'''
testStep("exec")
exec('print(1)')

'''
20 filter(function, iterable)
Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed. Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item
'''
testStep("filter")
lst=[1,2,3,4,6]

filter(print , lst)


'''
21 float([x])
Convert a string or a number to floating point.
If the argument is a string, it must contain a possibly signed decimal or floating point number, possibly embedded in whitespace.
The argument may also be [+|-]nan or [+|-]inf.
Otherwise, the argument may be an integer or a floating point number, and a floating point number with the same value (within Python's floating point precision) is returned.
If no argument is given, 0.0 is returned
'''

testStep("float")
print(float('2.3'))

print(float('1'))
print(float('11.10'))

'''
25 globals()
Return a dictionary representing the current global symbol table.
This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called). 
'''
testStep("globals",25)
print(globals())

'''
26 hasattr(object, name)
The arguments are an object and a string.
The result is True if the string is the name of one of the object's attributes, False if not.
(This is implemented by calling getattr(object, name) and seeing whether it raises an exceptions or not.) 
'''
testStep("hasattr")
class TestAtt(object):
    myvalue=10
    def __repr__(self) :
        return "TestAtt"

print(hasattr(TestAtt, 'myvalue'))

'''
27 hash(object)
Return the hash value of the object (if it has one).
Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup.
Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0). 
'''
testStep("hash")
print(hash(TestAtt))

'''
28 help([object])
Invoke the built-in help system. (This function is intended for interactive use.)
If no argument is given, the interactive help system starts on the interpreter console.
If the argument is a string, then the string is looked up as the name of a module, function, class, method, keyword, or documentation topic, and a help page is printed on the console. 
'''
testStep("help")
#help(TestAtt)

print(dir(TestAtt))

'''
29 hex(x)
Convert an integer number to a hexadecimal string.
The result is a valid Python expression.
If x is not a Python int object, it has to define an __index__() method that returns an integer. 
'''
testStep("hex")
print(hex(0x10))
print(hex(10))
HEXV=hex(0x10)
print(type(HEXV))

'''
33 int([number | string[, base]])
Convert a number or string to an integer.
If no arguments are given, return 0.
If a number is given, return number.__int__().
Conversion of floating point numbers to integers truncates towards zero.
A string must be a base-radix integer literal optionally preceded by + or - (with no space in between) and optionally surrounded by whitespace.
A base-n literal consists of the digits 0 to n-1, with a to z (or A to Z) having values 10 to 35.
The default base is 10.
The allowed values are 0 and 2-36. Base-2, -8, and -16 literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with integer literals in code.
Base 0 means to interpret exactly as a code literal, so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not legal, while int('010') is, as well as int('010', 8). 
'''

testStep("int", 33)
print(int('10'))

print(int('0x10',16))

print(int('0b10',2 ))

print(int('10'))

''' 
37  len(s)
'''
testStep("len", 37)
print(len('abcd'))

print(len(lst))

'''
38 list([iterable])
Return a list whose items are the same and in the same order as iterable's items.
iterable may be either a sequence, a container that supports iteration, or an iterator object.
If iterable is already a list, a copy is made and returned, similar to iterable[:].
For instance,
'''
testStep("list", 38)
print(list('abcabacd'))


print(list( (1, 2, 3) ))

dct={1:'Spring', 2:'Summer', 3:'Fall', 4:'Winter'}

print(list(dct))

'''
40 map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the results.
If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.
With multiple iterables, the iterator stops when the shortest iterable is exhausted
'''
testStep("map", 40)
print(map(bin, lst))

print(filter(bin, lst))

print(map(float, lst))

print(map(ord, 'abcd'))

filter(print, lst)


'''
41 max(iterable[, args...], *[, key])
With a single argument iterable, return the largest item of a non-empty iterable (such as a string, tuple or list).
With more than one argument, return the largest of the arguments.
The optional keyword-only key argument specifies a one-argument ordering function like that used for list.sort(). 
'''
testStep("max")
print(max(lst))
print(max(list('abcabacd')))

'''
46 oct(x)
Convert an integer number to an octal string.
The result is a valid Python expression.
If x is not a Python int object, it has to define an __index__() method that returns an integer. 
'''
testStep("oct", 46)
print(oct(10))

print(type(oct(1)))

'''
48 ord(c)
Given a string of length one, return an integer representing the Unicode code point of the character.
For example,
'''
testStep('ord', 48)
print(ord('a'))

#print(ord('\u20'))

#print(ord('\u2020'))

print(chr(97))

'''
49 pow(x, y[, z])
Return x to the power y; if z is present, return x to the power y, modulo z (computed more efficiently than pow(x, y) % z).
The two-argument form pow(x, y) is equivalent to using the power operator: x**y.
The arguments must have numeric types.
With mixed operand types, the coercion rules for binary arithmetic operators apply.
For int operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered.
For example, 10**2 returns 100, but 10**-2 returns 0.01.
If the second argument is negative, the third argument must be omitted.
If z is present, x and y must be of integer types, and y must be non-negative. 
'''

testStep('pow')

print(pow(2,10))
print(pow(2,-10))
print(pow(2,10, 10))

'''
53 repr(object)
Return a string containing a printable representation of an object.
For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object.
A class can control what this function returns for its instances by defining a __repr__() method. 
'''
testStep('repr')

print(repr(lst))

testatt = TestAtt()
print(repr(TestAtt))
print(repr(testatt))

'''
54 reversed(seq)
Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0). 
'''

testStep('reversed')
lst1=reversed(lst)
print(lst)
print(lst1)

'''
55 round(x[, n])
Return the floating point value x rounded to n digits after the decimal point.
If n is omitted, it defaults to zero. Delegates to x.__round__(n).
For the built-in types supporting round(), values are rounded to the closest multiple of 10 to the power minus n; if two multiples are equally close, rounding is done toward the even choice (so, for example, both round(0.5) and round(-0.5) are 0, and round(1.5) is 2).
The return value is an in
'''

testStep('round')
print(round(100.01))
print(round(100.50))
print(round(123456.56789, 3))


'''
56 set([iterable])
Return a new set, optionally with elements taken from iterable. 
'''
testStep('set')

print(set(lst))

newset = set(lst)

print(newset)

print(set(dct))

'''
58 slice([start], stop[, step])
Return a slice object representing the set of indices specified by range(start, stop, step).
The start and step arguments default to None.
Slice objects have read-only data attributes start, stop and step which merely return the argument values (or their default).
They have no other explicit functionality; however they are used by Numerical Python and other third party extensions.
Slice objects are also generated when extended indexing syntax is used.
For example: a[start:stop:step] or a[start:stop, i]. 
'''
testStep('slice')

print(slice( 1000))

'''
59 sorted(iterable[, key][, reverse])
Return a new sorted list from the items in iterable.
Has two optional arguments which must be specified as keyword arguments.
key specifies a function of one argument that is used to extract a comparison key from each list element: key=str.lower.
The default value is None.
reverse is a boolean value.
If set to True, then the list elements are sorted as if each comparison were reversed. 
'''

testStep('sorted')

print(sorted(lst))

print(sorted(dct))


print(sorted(lst,  reverse=True))

print(sorted(dct,  reverse=True))

print(sorted(lst, key=print))

'''
61 str([object[, encoding[, errors]]])
Return a string version of an object, using one of the following modes:
If encoding and/or errors are given, str() will decode the object which can either be a byte string or a character buffer using the codec for encoding.
The encoding parameter is a string giving the name of an encoding; if the encoding is not known, LookupError is raised. Error handling is done according to errors; this specifies the treatment of characters which are invalid in the input encoding.
If errors is 'strict' (the default), a ValueError is raised on errors, while a value of 'ignore' causes errors to be silently ignored, and a value of 'replace' causes the official Unicode replacement character, U+FFFD, to be used to replace input characters which cannot be decoded. See also the codecs module.
When only object is given, this returns its nicely printable representa
'''
testStep('str', 61)

print(str(TestAtt))
print(str(testatt))

'''
62 sum(iterable[, start])
Sums start and the items of an iterable from left to right and returns the total. start defaults to 0.
The iterable's items are normally numbers, and are not allowed to be strings.
The fast, correct way to concatenate a sequence of strings is by calling ''.join(sequence). 
'''
testStep('sum')

print(sum(lst))

'''
64 tuple([iterable])
Return a tuple whose items are the same and in the same order as iterable's items. iterable may be a sequence, a container that supports iteration, or an iterator object.
If iterable is already a tuple, it is returned unchanged.
For instance, tuple('abc') returns ('a', 'b', 'c') and tuple([1, 2, 3]) returns (1, 2, 3).
If no argument is given, returns a new empty tuple, (). tuple is an immutable sequence type
'''
testStep('tuple', 64)

print(tuple('abc'))
print(tuple(lst))
print(tuple(dct))

'''
65 type(object)
Return the type of an object.
The return value is a type object and generally the same object as returned by object.__class__.
The isinstance() built-in function is recommended for testing the type of an object, because it takes subclasses into account.
With three arguments, type() functions as a constructor as detailed below. 
'''
testStep('type')
print(type(1))
print(type(1.0))
print(type(0b110))
print(type(0o110))
print(type(0x110))
print(type('1.0'))
print(type(lst))
print(type(dct))
print(type(TestAtt))
print(type(testatt))

#print(type('testatt', object, dict(myvalue)))

'''
67 vars([object])
Without an argument, act like locals().
With a module, class or class instance object as argument (or anything else that has a __dict__ attribute), return that attribute. 
'''
testStep('vars', 67)

print(vars())
print(vars(testatt))
'''
68 zip(*iterables)
Make an iterator that aggregates elements from each of the iterables.
Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
The iterator stops when the shortest input iterable is exhausted.
With a single iterable argument, it returns an iterator of 1-tuples.
With no arguments, it returns an empty iterator. Equivalent to: 
'''
testStep('zip')
print(zip(lst, dct))




testStep('string method', 0)
'''
1 capitalize( )
Return a copy of the string with only its first character capitalized. For 8-bit strings, this method is locale-dependent. 
'''
testStep('capitalize', 1)
s = 'Black holes are where God divided by zero'
s2 = 'sample.txt'

print( s.capitalize())

'''
2 center( width[, fillchar])
Return centered in a string of length width. Padding is done using the specified fillchar (default is a space).
'''
testStep('center')
print(s.center(50,'*'))

'''
3 count( sub[, start[, end]])
Return the number of occurrences of substring sub in string S[start:end]. Optional arguments start and end are interpreted as in slice notation.
'''
testStep('count')

print(s.count('i'))

print(s.count('hole'))

print(s.count('l'))

print(map(s.count, s))

'''
4 decode( [encoding[, errors]])
Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding. errors may be given to set a different error handling scheme. The default is 'strict', meaning that encoding errors raise UnicodeError. Other possible values are 'ignore', 'replace' and any other name registered via codecs.register_error.

>>> s.decode()
u'Black holes are where God divided by zero'
'''
testStep('decode')

print(s.decode())

'''
5 encode( [encoding[,errors]])
Return an encoded version of the string. Default encoding is the current default string encoding. errors may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'. 
'''
testStep('encode')
print(s.encode())

'''
6 endswith( suffix[, start[, end]])
Return True if the string ends with the specified suffix, otherwise return False. suffix can also be a tuple of suffixes to look for. With optional start, test beginning at that position. With optional end, stop comparing at that position.
'''

testStep('endswith')
print(s.endswith('txt'))

print(s2.endswith('txt'))


''' 
7 expandtabs( [tabsize])
Return a copy of the string where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed. 
'''
testStep('expandtabs')

print('a\tb'.expandtabs())

'''
8 find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found, such that sub is contained in the range [start, end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
'''
testStep('find')
S = 'aaaaaSPYbbbbSPYcccc'
where = S.find('SPY')
print(where)
S = S[:where] + 'SKY' + S[(where+3):]
print(S)

print(S.find('spy'))
print(S.find('a'))
print(S.rfind('a'))


'''
9 index( sub[, start[, end]])
Like find(), but raise ValueError when the substring is not found. 
'''
testStep('index')

print(S.index('SKY'))
#print(S.index('spy'))

'''
10 isalnum( )
Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise. For 8-bit strings, this method is locale-dependent.
'''

testStep('isalnum')
print('abc123'.isalnum())

print('abcdef'.isalnum())
print('abc def'.isalnum())

'''
11 isalpha( )
Return true if all characters in the string are alphabetic and there is at least one character, false otherwise. For 8-bit strings, this method is locale-dependent.

>>> 'abc'.isalpha()
True
>>> 'abc7'.isalpha()
False

'''
testStep('isalpha')

'''
12 isdigit( )
Return true if all characters in the string are digits and there is at least one character, false otherwise. For 8-bit strings, this method is locale-dependent.

>>> '123'.isdigit()
True
>>> '123a'.isdigit()
False
'''
testStep('isdigit')

'''
13 islower( )
Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise. For 8-bit strings, this method is locale-dependent.
'''
testStep('islower')

'''
14 isspace( )
Return true if there are only whitespace characters in the string and there is at least one character, false otherwise. For 8-bit strings, this method is locale-dependent.

>>> '1 f'.isspace()
False
>>> '  '.isspace()
True
'''
testStep('isspace')

'''
15 istitle( )
Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise. For 8-bit strings, this method is locale-dependent.

>>> 'Black holes'.istitle()
False
>>> 'Black Holes'.istitle()
True
'''
testStep('istitle')

'''
16 isupper( )
Return true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise. For 8-bit strings, this method is locale-dependent. 
'''
testStep('isupper')

''' 
17 join( seq)
Return a string which is the concatenation of the strings in the sequence seq. The separator between elements is the string providing this method.
'''
testStep('join')
seq = ['a','b','c','d']
print(''.join(seq))
print('-'.join(seq))
print(','.join([`x` for x in xrange(101)]))
print(range(10))
print(xrange(10))

'''
18 ljust( width[, fillchar])
Return the string left justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s).

>>> '123'.ljust(10)
'123       '
'''
testStep('ljust')

'''
19 lower( )
Return a copy of the string converted to lowercase. For 8-bit strings, this method is locale-dependent.
'''
testStep('lower')
'''
20 lstrip( [chars])
Return a copy of the string with leading characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are stripped:

>>> '     too much left side space  '.lstrip()
'too much left side space  '
>>> 'www.bogotobogo.com'.lstrip('w.')
'bogotobogo.com'
'''
testStep('lstrip')

'''
21 partition( sep)
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

>>> s.partition('are')
('Black holes ', 'are', ' where God divided by zero')

'''
testStep('partition')

'''
22 replace( old, new[, count])
Return a copy of the string with all occurrences of substring old replaced by new. If the optional argument count is given, only the first count occurrences are replaced.

>>> S = 'beetles'
>>> S = S[:3] + 'xx' + S[5:]
>>> S
'beexxes'

>>> S = 'beetles'
>>> S = S.replace('ee','xx')
>>> S
'bxxtles'
'''
testStep('replace')

'''
23 rfind( sub [,start [,end]])
Return the highest index in the string where substring sub is found, such that sub is contained within s[start,end]. Optional arguments start and end are interpreted as in slice notation. Return -1 on failure. 
'''
testStep('rfind')

'''
24 irndex( sub[, start[, end]])
Like rfind() but raises ValueError when the substring sub is not found.
'''
testStep('rindex')

'''
25 rjust( width[, fillchar])
Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is a space). The original string is returned if width is less than len(s).

>>> '123'.rjust(10)
'       123'
'''
testStep('rjust')
'''
26 rpartition( sep)
Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing two empty strings, followed by the string itself. 
'''
testStep('rpartition')

'''
27 rsplit( [sep [,maxsplit]])
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done, the rightmost ones. If sep is not specified or None, any whitespace string is a separator. Except for splitting from the right, rsplit() behaves like split() which is described in detail below.
'''
testStep('rspilt')
'''
28 rstrip( [chars])
Return a copy of the string with trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a suffix; rather, all combinations of its values are stripped:

>>> ' too much right side space    '.rstrip()
' too much right side space'

>>> 'mississippi'.rstrip('im')
'mississipp'
>>> 'mississippi'.rstrip('ip')
'mississ'
'''
testStep('rstrip')

'''
29 split( [sep [,maxsplit]])
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done. (thus, the list will have at most maxsplit+1 element).
If maxsplit is not specified, then there is no limit on the number of splits (all possible splits are made). Consecutive delimiters are not grouped together and are deemed to delimit empty strings: 
'''
testStep('split')

print('1,,2'.split(','))

print('1, 2, 3, '.split(', '))

import re
# split with semicolon, comma, space
str = 'Life; a walking, shadow'
print(re.split(';|,| ', str))
# split with semicolon+space, comma+space, space
print(re.split('; |, | ',str))

'''
30 splitlines( [keepends])
Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true. 
'''
testStep('splitlines')

print(r'a\r\nb\rc\nd\te'.splitlines())

'''
31 startswith( prefix[, start[, end]])
Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.
'''
testStep('startswith')
'''
32 strip( [chars])
Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed.
If omitted or None, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:

>>> '   too much space    '.strip()
'too much space'
>>> 'www.bogotobogo.com'.strip('.wmoc')
'bogotobog'
>>> 
'''
testStep('strip')
'''
33 swapcase( )
Return a copy of the string with uppercase characters converted to lowercase and vice versa. For 8-bit strings, this method is locale-dependent.
'''
testStep('swapcase')
'''
34 title( )
Return a titlecased version of the string: words start with uppercase characters, all remaining cased characters are lowercase. For 8-bit strings, this method is locale-dependent. 
'''
testStep('title')
print(s)
print(s.title())

'''
35 translate(table[, deletechars])
Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256.
We can use the maketrans() helper function in the string module to create a translation table.
For Unicode objects, the translate() method does not accept the optional deletechars argument. Instead, it returns a copy of the s where all characters have been mapped through the given translation table which must be a mapping of Unicode ordinals to Unicode ordinals, Unicode strings or None.
Unmapped characters are left untouched.
Characters mapped to None are deleted.
'''
testStep('translate')

print(s.translate('0123456789abcdef'*16))

'''
36 upper( )
Return a copy of the string converted to uppercase. For 8-bit strings, this method is locale-dependent.
'''
testStep('upper')
'''
37 zfill(width)
Return the numeric string left filled with zeros in a string of length width. The original string is returned if width is less than len(s). 
'''

testStep('zfill')
print('0'.zfill(10))
print('a'.zfill(3))

print('abcdefg'.zfill(16))

'''
list
'''
testStep('list method', 0)

'''
1 append(x)

    Append a new element x to the end of list L. Does not return a value.
'''
testStep('append')

colors = ['red', 'green', 'blue']
colors.append('indigo')
print(colors)

'''
2 L.count(x)

    Return the number of elements of L that compare equal to x.

    >>> [59, 0, 0, 0, 63, 0, 0].count(0)
    5
    >>> ['x', 'y'].count('Fomalhaut')
    0
'''
testStep('count')
print([59, 0, 0, 0, 63, 0, 0].count(0))
print (['x', 'y'].count('Fomalhaut'))

'''
3 L.extend(S)

    Append another sequence S to L.

    >>> colors
    ['red', 'green', 'blue', 'indigo']
    >>> colors.extend(['violet', 'pale puce'])
    >>> colors
    ['red', 'green', 'blue', 'indigo', 'violet', 'pale puce']
'''
testStep('extend')
print(['red', 'green', 'blue', 'indigo'].extend(['violet', 'pale puce']))

'''
4 L.index(x[, start[, end]])

    If L contains any elements that equal x, return the index of the first such element, otherwise raise a ValueError exception.

    The optional start and end arguments can be used to search only positions within the slice L[start:end].

    >>> colors
    ['red', 'green', 'blue', 'indigo', 'violet', 'pale puce']
    >>> colors.index('blue')
    2
    >>> colors.index('taupe')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: list.index(x): x not in list
    >>> M=[0, 0, 3, 0, 0, 3, 3, 0, 0, 3]
    >>> M.index(3)
    2
    >>> M.index(3, 4, 8)
    5
    >>> M.index(3, 0, 2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: list.index(x): x not in list
'''
testStep('index')
print(['red', 'green', 'blue', 'indigo', 'violet', 'pale puce'].index('blue'))
print([0, 0, 3, 0, 0, 3, 3, 0, 0, 3].index(3))
print([0, 0, 3, 0, 0, 3, 3, 0, 0, 3].index(3, 4, 8))


'''
5 L.insert(i,x)

    Insert a new element x into list L just before the ith element, shifting all higher-number elements to the right. No value is returned.

    >>> colors
    ['red', 'green', 'blue', 'indigo', 'violet', 'pale puce']
    >>> colors[1]
    'green'
    >>> colors.insert(1, "yellow")
    >>> colors
    ['red', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pale puce']
'''
testStep('insert')
print(['red', 'green', 'blue', 'indigo', 'violet', 'pale puce'].insert(1, 'yellow'))

'''
6 L.pop([i])

    Remove and return the element with index i from L. The default value for i is -1, so if you pass no argument, the last element is removed.

    >>> colors
    ['red', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pale puce']
    >>> tos = colors.pop()
    >>> tos
    'pale puce'
    >>> colors
    ['red', 'yellow', 'green', 'blue', 'indigo', 'violet']
    >>> colors[4]
    'indigo'
    >>> dye = colors.pop(4)
    >>> dye
    'indigo'
    >>> colors
    ['red', 'yellow', 'green', 'blue', 'violet']
'''

testStep('pop')
print(['red', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pale puce'].pop())
print(['red', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pale puce'].pop(1))


'''
7 L.remove(x)

    Remove the first element of L that is equal to x. If there aren't any such elements, raises ValueError.

    >>> colors
    ['red', 'yellow', 'green', 'blue', 'violet']
    >>> colors.remove('yellow')
    >>> colors
    ['red', 'green', 'blue', 'violet']
    >>> colors.remove('cornflower')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: list.remove(x): x not in list
    >>> notMuch = [0, 0, 3, 0]
    >>> notMuch.remove(0)
    >>> notMuch
    [0, 3, 0]
    >>> notMuch.remove(0)
    >>> notMuch
    [3, 0]
    >>> notMuch.remove(0)
    >>> notMuch
    [3]
    >>> notMuch.remove(0)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: list.remove(x): x not in list
'''
testStep('remove')
print( ['red', 'yellow', 'green', 'blue', 'violet'].remove('yellow'))
print([0, 0, 3, 0].remove(0))

'''
8 L.reverse()
    Reverses the elements of L in place. Does not return a result. Compare Section 20.36, reversed(): Produce a reverse iterator.
    >>> colors['red', 'green', 'blue', 'violet']
    >>> colors.reverse()
    >>> colors
    ['violet', 'blue', 'green', 'red']
'''
testStep('reverse')
print(['red', 'green', 'blue', 'violet'].reverse())

'''
9 L.sort(cmp[,key[,reverse]]])

    Sort list L in place. Does not return a result. Compare Section 20.39, sorted(): Sort a sequence.

    The reordering is guaranteed to be stablethat is, if two elements are considered equal, their order after sorting will not change.

    While sorting, Python will use the built-in cmp() function to compare elements; see Section 20.8, cmp(): Compare two values. You may provide, as the first argument to the .sort() method, your own comparator function to compare elements. This function must have the same calling sequence and return value convention as the built-in cmp() function: it must take two arguments, and return a negative number of the first argument precedes the second, a positive number if the second argument precedes the first, or zero if they are considered equal.

    You may also provide a key extractor function that is applied to each element to determine its key. This function must take one argument and return the value to be used as the sort key. If you want to provide a key extractor function but not a comparator function, pass None as the first argument to the method.

    Additionally, you may provide a third argument of True to sort the sequence in descending order; the default behavior is to sort into ascending order.

    >>> temps=[67, 73, 85, 93, 92, 78, 95, 100, 104]
    >>> temps.sort()
    >>> temps
    [67, 73, 78, 85, 92, 93, 95, 100, 104]
    >>> def reverser(n1, n2):
    ...     #Comparison function to use reverse order.
    ...     
    ...     return cmp(n2, n1)
    ... 
    >>> temps.sort(reverser)
    >>> temps
    [104, 100, 95, 93, 92, 85, 78, 73, 67]
    >>> def unitsDigit(n):
    ...     #Returns only the units digit of n.
    ...     
    ...     return n % 10
    ... 
    >>> temps.sort(None, unitsDigit)
    >>> temps
    [100, 92, 93, 73, 104, 95, 85, 67, 78]
    >>> temps.sort(None, None, True)
    >>> temps
    [104, 100, 95, 93, 92, 85, 78, 73, 67]
'''
testStep('sort')

def reverser(n1, n2):
    return n2 <n1

print([67, 73, 78, 85, 92, 93, 95, 100, 104].sort(reverser))

print([67, 73, 78, 85, 92, 93, 95, 100, 104].sort())


testStep('dict method',0)

testStep('dict create')

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)


testStep('dict[key]')
print(a['one'])
a['one'] += 10
print(a['one'])

testStep('d.clear')
print(a)
a.clear()
print(a)

testStep('d.copy')

f=d.copy()
print(f)
d.clear()
print(f)

testStep('d.get')

print(f.get('one'))

testStep('d.has_key')

print(f.has_key('one'))

testStep('d.items')

print(f.items())

testStep('d.pop')

print(f.pop('one'))
print(f)

testStep('d.popitem')
print(e)
print(e.popitem())
print(e)

testStep('d.update')
print(e.update(four=3,five=5,six=6))
print(e)

testStep('d.values')
print(e.values())
print(e)

testStep('d.viewitems')
print(e.viewitems())

testStep('d.viewkeys')
print(e.viewkeys())

testStep('d.viewvalues')
print(e.viewvalues())

