Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> name = Maurice
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name = Maurice
NameError: name 'Maurice' is not defined
>>> name = "Maurice"
>>> nachname = "Knaust"
>>> gesamter_name += "Maurice"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    gesamter_name += "Maurice"
NameError: name 'gesamter_name' is not defined
>>> gesmater_name =+ "Maurice"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    gesmater_name =+ "Maurice"
TypeError: bad operand type for unary +: 'str'
>>> Name += Maurice
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    Name += Maurice
NameError: name 'Name' is not defined
>>> name += "maurice"
>>> name += " "
>>> name += "knaust"
>>> name
'Mauricemaurice knaust'
>>> /gamemode 1#
SyntaxError: invalid syntax
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help (dir)
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> str
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(...)
 |      S.capitalize() -> str
 |      
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |  
 |  casefold(...)
 |      S.casefold() -> str
 |      
 |      Return a version of S suitable for caseless comparisons.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |      
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |      
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |  
 |  isprintable(...)
 |      S.isprintable() -> bool
 |      
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> str
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> str
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string, starting at the end of the string and
 |      working to the front.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> str
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(...)
 |      S.split(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.
 |  
 |  splitlines(...)
 |      S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> str
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(...)
 |      S.swapcase() -> str
 |      
 |      Return a copy of S with uppercase characters converted to lowercase
 |      and vice versa.
 |  
 |  title(...)
 |      S.title() -> str
 |      
 |      Return a titlecased version of S, i.e. words start with title case
 |      characters, all remaining cased characters have lower case.
 |  
 |  translate(...)
 |      S.translate(table) -> str
 |      
 |      Return a copy of the string S, where all characters have been mapped
 |      through the given translation table, which must be a mapping of
 |      Unicode ordinals to Unicode ordinals, strings, or None.
 |      Unmapped characters are left untouched. Characters mapped to None
 |      are deleted.
 |  
 |  upper(...)
 |      S.upper() -> str
 |      
 |      Return a copy of S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

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
 |  __ge__(self, value, /)
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
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
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

>>> print("Hallo, wie gehts?")
Hallo, wie gehts?
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
herzlichen Glückwunsch. Happy birthday to you :D
Du bist 14 Jahre alt
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2018
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 5
du hast heute nicht Geburtstag
du bist -1 Jahre alt
du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2005
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
herzlichen Glückwunsch. Happy birthday to you :D
Du bist 12 Jahre alt
>>> name
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> nachname
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    nachname
NameError: name 'nachname' is not defined
>>> print(gesamter_name)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(gesamter_name)
NameError: name 'gesamter_name' is not defined
>>> print(nachname)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(nachname)
NameError: name 'nachname' is not defined
>>> print("ich hoffe dir geht es gut")
ich hoffe dir geht es gut
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2018
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
herzlichen Glückwunsch. Happy birthday to you :D
Du bist -1 Jahre alt
du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 15
du hast heute nicht Geburtstag
du bist 14 Jahre alt
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2018
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
herzlichen Glückwunsch. Happy birthday to you :D
Du bist -1 Jahre alt
du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 12
Am wie vielten Tag hast du Geburtstag? 7
du hast heute nicht Geburtstag
du bist 14 Jahre alt
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2444
in welchem Monat (als Zahl) bist du geboren? 2
Am wie vielten Tag hast du Geburtstag? 5
du hast heute nicht Geburtstag
du bist -427 Jahre alt
du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein
bitte gebe diesmal dein richtiges Alter an
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2000
in welchem Monat (als Zahl) bist du geboren? 3
Am wie vielten Tag hast du Geburtstag? 6
du hast heute nicht Geburtstag
du bist 17 Jahre alt
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 12334445444
in welchem Monat (als Zahl) bist du geboren? 324926923
Am wie vielten Tag hast du Geburtstag? 5765935382623
du hast heute nicht Geburtstag
du bist -12334443427 Jahre alt
du hast geschummelt, denn du kannst nicht unter Null Jahre alt sein
bitte gebe diesmal dein richtiges Alter an
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 1899
in welchem Monat (als Zahl) bist du geboren? 6
Am wie vielten Tag hast du Geburtstag? 3
du hast heute nicht Geburtstag
du bist 118 Jahre alt
Traceback (most recent call last):
  File "H:\Informatik AG\Projekttage-2017\Lektion 2\neu.py", line 14, in <module>
    if Jahr < 1900:
NameError: name 'Jahr' is not defined
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 1899
in welchem Monat (als Zahl) bist du geboren? 3
Am wie vielten Tag hast du Geburtstag? 7
du hast heute nicht Geburtstag
du bist 118 Jahre alt
Traceback (most recent call last):
  File "H:\Informatik AG\Projekttage-2017\Lektion 2\neu.py", line 14, in <module>
    if Jahr < 1900:
NameError: name 'Jahr' is not defined
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 1899
in welchem Monat (als Zahl) bist du geboren? 4
Am wie vielten Tag hast du Geburtstag? 5
du hast heute nicht Geburtstag
du bist 118 Jahre alt
DU hast geschumelt. Du kannst nicht über 100 Jahre alt sein. Ich weiß es einfach
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 1900
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 5
du hast heute nicht Geburtstag
du bist 117 Jahre alt
>>> print("wie geht es dir? Ich hoffe es geht dir gut, wenn nicht dann ruf mich einfach an.")
wie geht es dir? Ich hoffe es geht dir gut, wenn nicht dann ruf mich einfach an.
>>> print(;()
      
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 1899
in welchem Monat (als Zahl) bist du geboren? 3
Am wie vielten Tag hast du Geburtstag? 5
du hast heute nicht Geburtstag
du bist 118 Jahre alt
Du hast geschumelt. Du kannst nicht über 100 Jahre alt sein. Ich weiß es einfach
Bitte gebe diesmal dein richtiges Alter an
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
Was ist dein Name?Maurice
Traceback (most recent call last):
  File "H:\Informatik AG\Projekttage-2017\Lektion 2\neu.py", line 4, in <module>
    name = int(input("Was ist dein Name?"))
ValueError: invalid literal for int() with base 10: 'Maurice'
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 7
Am wie vielten Tag hast du Geburtstag? 19
herzlichen Glückwunsch
Du bist 14 Jahre alt
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 2003
in welchem Monat (als Zahl) bist du geboren? 34
Am wie vielten Tag hast du Geburtstag? 5
du hast heute nicht Geburtstag
du bist 14 Jahre alt
>>> ================================ RESTART ================================
>>> 
In welchen Jahr bist du geboren? 1999
In welchem Monat (als Zahl) bist du geboren? 
Traceback (most recent call last):
  File "H:\Informatik AG\Projekttage-2017\Lektion 2\neu.py", line 2, in <module>
    monat = int(input("In welchem Monat (als Zahl) bist du geboren? "))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
