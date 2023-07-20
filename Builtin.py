Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:25:23) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help(id)
Help on built-in function id in module builtins:

id(...)
    id(object) -> integer
    
    Return the identity of an object.  This is guaranteed to be unique among
    simultaneously existing objects.  (Hint: it's the object's memory address.)

>>> help(int)
Help on class int in module builtins:

class int(object)
 |  int(x=0) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(...)
 |  
 |  __ge__(...)
 |      __ge__=($self, value, /)
 |      --
 |      
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitablefor use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(...)
 |      Returns size in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(...)
 |      int.bit_length() -> int
 |      
 |      Number of bits necessary to represent self in binary.
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  from_bytes(...) from builtins.type
 |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
 |      
 |      Return the integer represented by the given array of bytes.
 |      
 |      The bytes argument must either support the buffer protocol or be an
 |      iterable object producing bytes.  Bytes and bytearray are examples of
 |      built-in objects that support the buffer protocol.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument indicates whether two's complement is
 |      used to represent the integer.
 |  
 |  to_bytes(...)
 |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
 |      
 |      Return an array of bytes representing an integer.
 |      
 |      The integer is represented using length bytes.  An OverflowError is
 |      raised if the integer is not representable with the given number of
 |      bytes.
 |      
 |      The byteorder argument determines the byte order used to represent the
 |      integer.  If byteorder is 'big', the most significant byte is at the
 |      beginning of the byte array.  If byteorder is 'little', the most
 |      significant byte is at the end of the byte array.  To request the native
 |      byte order of the host system, use `sys.byteorder' as the byte order value.
 |      
 |      The signed keyword-only argument determines whether two's complement is
 |      used to represent the integer.  If signed is False and a negative integer
 |      is given, an OverflowError is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> dir(_builtins_)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    dir(_builtins_)
NameError: name '_builtins_' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> print("NK")
NK
>>> print('nk')
nk
>>> x=100
>>> print(x)
100
>>> print("Value of x : ",x)
Value of x :  100
>>> print(x,"x Value  ")
100 x Value  
>>> a=1
>>> b=2
>>> c=3
>>> print(a,b,c)
1 2 3
>>> print(a,b,"Value of x : ",x)
1 2 Value of x :  100
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> id(a)
1934328000
>>> type(a)
<class 'int'>
>>> print(a,"\n",b)
1 
 2
>>> print(a,"\t",b)
1 	 2
>>> p=1
>>> p
1
>>> id(p)
1934328000
>>> p=2
>>> id(p)
1934328032
>>> k="NK"
>>> len(k)
2
>>> len("N I S H A")
9
>>> len([1,2,3])
3
>>> pow(2,2)
4
>>> 2**2
4
>>> abs(-7)
7
>>> x=40
>>> y=20
>>> min(x,y)
20
>>> ord('N')
78
>>> max(x,y)
40
>>> bin(10)
'0b1010'
>>> bin(s)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    bin(s)
NameError: name 's' is not defined
>>> bin((ord("n")))
'0b1101110'
>>> g=10.09
>>> round(g)
10
>>> floor(g)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    floor(g)
NameError: name 'floor' is not defined
>>> round(10.343434599,3)
10.343
>>> chr(78)
'N'
>>> ord("N")
78
>>> ord("p")
112
>>> 112-32
80
>>> ord("P")
80
>>> chr((ord(n)-32))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    chr((ord(n)-32))
NameError: name 'n' is not defined
>>> chr((ord("n")-32))
'N'
>>> ================================ RESTART ================================
>>> 
NK
>>> ================================ RESTART ================================
>>> 
NK
Hello
>>> ================================ RESTART ================================
>>> 
NK
Hello
>>> ================================ RESTART ================================
>>> 
Addition :  30
>>> ================================ RESTART ================================
>>> 
percentage :  30.0
>>> ================================ RESTART ================================
>>> 
percentage :  0.6
>>> ================================ RESTART ================================
>>> 
percentage :  60.0
>>> ================================ RESTART ================================
>>> 
percentage :  60.0
Total :  150
>>> ================================ RESTART ================================
>>> 
percentage :  60.0
Total :  150
Total marks :  250
>>> ================================ RESTART ================================
>>> 
percentage :  60.0
obtained :  150
Total marks :  250
>>> ================================ RESTART ================================
>>> 
percentage :  30.0
Total marks :  150
>>> ================================ RESTART ================================
>>> 
Area :  961.625
>>> ================================ RESTART ================================
>>> 
Area of rectangle  :  200
Area of square  :  2500
>>> ================================ RESTART ================================
>>> 

>>> ================================ RESTART ================================
>>> 
20
<class 'str'>
>>> ================================ RESTART ================================
>>> 
20
<class 'str'>
<class 'str'>
>>> ================================ RESTART ================================
>>> 
20
<class 'str'>
<class 'int'> 20
>>> ================================ RESTART ================================
>>> 
20
<class 'str'>
<class 'int'> 20
<class 'str'>
>>> ================================ RESTART ================================
>>> 
10 20
<class 'str'>
Traceback (most recent call last):
  File "C:/Users/BALRAM/Desktop/ph/inut.py", line 4, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: '10 20'
>>> ================================ RESTART ================================
>>> 
10 20

10 20
>>> ================================ RESTART ================================
>>> 
10 20
Traceback (most recent call last):
  File "C:/Users/BALRAM/Desktop/ph/inut.py", line 3, in <module>
    x=int(a)
ValueError: invalid literal for int() with base 10: '10 20'
>>> ================================ RESTART ================================
>>> 
Enter 1 :10
Enter 2  :20
1020
>>> ================================ RESTART ================================
>>> 
Enter 1 :10
Enter 2  :20
30
>>> ================================ RESTART ================================
>>> 
Enter 1 :10
Enter 2  :20
Traceback (most recent call last):
  File "C:/Users/BALRAM/Desktop/ph/inut.py", line 4, in <module>
    c=x+y
NameError: name 'x' is not defined
>>> ================================ RESTART ================================
>>> 
Enter 1 :10
Enter 2  :20
30
>>> ================================ RESTART ================================
>>> 
Enter 1 :98
Enter 2  :99
Enter 3 :97
Enter 4  :99
Enter 5 :95
total :  488
percentage :  97.6
>>> ================================ RESTART ================================
>>> 
Enter byte : 2345623
byte :  2345623
kb :  2290.6474609375
mb:  2.2369604110717773
gb :  0.0021845316514372826
bit :  18764984
>>> 
