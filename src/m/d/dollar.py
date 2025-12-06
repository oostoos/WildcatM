'''
Logic pertaining to core MUMPS functions, denoted by $.
'''

'''
Author: Austin Shank
Revisions:
    @AJX 2025-12-04 - Created, basic $piece implementation
'''

from src.utils import common as utils

### $piece ###

def d_p(string, delimiter = "", index = 1):
    return __d_piece(string, delimiter, index)
def d_P(string, delimiter = "", index = 1):
    return __d_piece(string, delimiter, index)
def d_piece(string, delimiter = "", index = 1):
    return __d_piece(string, delimiter, index)
def d_PIECE(string, delimiter = "", index = 1):
    return __d_piece(string, delimiter, index)

def __d_piece(string, delimiter = "", index = 1):
    '''
    Pulls a piece from a string at a provided index based on the input delimiter.

    :param string: String from which to pull piece
    :param delimiter: Delimiter denoting pieces within this string.
    :param index: Index of the piece to pull.
    
    :return: Piece at the given delimited index from the provided string.
    '''

    # TODO: M has an end parameter
    
    if (utils.isNoneOrEmptyStr(string)):
        return ""
    
    if (utils.isNoneOrEmptyStr(delimiter)):
        # TODO: tbh I don't know what M does here lmao, just $e?
        return ""

    # TODO: may only need to cover "" case here
    if (utils.isNoneOrEmptyStr(index)):
        index = 1
    
    if (index < 1):
        return ""
    
    pieces = string.split(delimiter)
    
    if index > len(pieces):
        return ""
    
    return pieces[index - 1]

### $select ###

# TODO