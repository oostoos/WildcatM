'''
Logic pertaining to core MUMPS functions, denoted by $.
'''

'''
Author: Austin Shank
Revisions:
    @AJX 2025-12-04 - Basic $piece implementation
'''

def p(string, delimiter, index):
    return __d_piece(string, delimiter, index)
def P(string, delimiter, index):
    return __d_piece(string, delimiter, index)
def piece(string, delimiter, index):
    return __d_piece(string, delimiter, index)
def PIECE(string, delimiter, index):
    return __d_piece(string, delimiter, index)

def __d_piece(string, delimiter, index):
    '''
    Pulls a piece from a string at a provided index based on the input delimiter.
    
    :param string: String from which to pull piece
    :param delimiter: Delimiter denoting pieces within this string.
    :param index: Index of the piece to pull.

    Returns:
    Piece at the given delimited index from the provided string.
    '''

    # TODO: "" index should return 1st piece, also M has an end parameter
    
    if (index < 1):
        return ""
    
    pieces = string.split(delimiter)
    
    if index > len(pieces):
        return ""
    
    return pieces[index - 1]