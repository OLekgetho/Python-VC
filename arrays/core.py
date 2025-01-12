import array
from typing import Union

class Array:
    '''Return a new arrays whose items are restricted by typecode, and
       that can contain at most `size` elements.

       Arrays behave very much like Python list, except that
       the type of objects stored in them is constrained. The type is specified
       at object creation time by using a type code, which is a single character.
       The following type codes are defined:
       
           Type code   C Type             Minimum size in bytes
           'b'         signed integer     1
           'B'         unsigned integer   1
           'u'         Unicode character  2
           'h'         signed integer     2
           'H'         unsigned integer   2
           'i'         signed integer     2
           'I'         unsigned integer   2
           'l'         signed integer     4
           'L'         unsigned integer   4
           'q'         signed integer     8
           'Q'         unsigned integer   8
           'f'         floating point     4
           'd'         floating point     8

        Parameters:
            max_capacity (int): The maximum number of elements the arrays can hold.
            typecode (str, optional): The typecode of the arrays. Defaults to 'l' for int.

       '''

    def __init__(self, size: int, typecode: str = 'l'):
        if size <= 0:
            raise ValueError(f'Invalid arrays size (must be positive): {size}')
        self._size = size
        self._array = array.array(typecode, [0] * size)


    def __len__(self):
        '''
        Return the number of elements in the arrays.

        Parameters:
            None

        Returns:
            int: The number of elements in the arrays.
        '''

        return self._size
    

    def __getitem__(self, index: int) -> Union[int, float]:
        '''
        Get the value at the given index.

        Parameters:
            index (int): The index to get the value from.

        Returns:
            Union[int, float]: The value at the given index.
        '''

        if index < 0 or index >= self._size:
            raise IndexError('arrays index out of range')
        return self._array[index]
        

    def __setitem__(self, index: int, val: Union[int, float]) -> None:
        '''
        Set the value at the given index.

        Parameters:
            index (int): The index to set the value at.
            val (Union[int, float]): The value to set.

        Returns:
            None
        '''

        if index < 0 or index >= self._size:
            raise IndexError('arrays assignment index out of range')
        self._array[index] = val
    
    
    def __repr__(self):
        '''
        Return the string representation of the arrays.

        Parameters:
            None

        Returns:
            str: The string representation of the arrays.
        '''

        return repr(self._array)