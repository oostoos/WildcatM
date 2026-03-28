'''
Logic pertaining to core MUMPS functions, denoted by $.
'''

'''
Author: Austin Shank
Revisions:
    @AJX 2025/12/04 - Created, basic $piece implementation
    @AJX 2026/03/28 - Moved to single core file, support additional $PIECE functionality (index2, better defaulting)
'''

from src.utils import common as utils
from src.m.m_value import MValue

### $PIECE ###

def p(string, delimiter = "", index = 1):
    return __piece(string, delimiter, index)

def P(string, delimiter = "", index = 1):
    return __piece(string, delimiter, index)

def piece(string, delimiter = "", index = 1):
    return __piece(string, delimiter, index)

def PIECE(string, delimiter = "", index = 1):
    return __piece(string, delimiter, index)

def __piece(string: str | int, delimiter: str | int = "", index1: str | int = 1, index2: str | int = None):
    '''
    Pulls a piece from a string at a provided index based on the input delimiter.

    :param string: String from which to pull piece.
    :param delimiter: Delimiter denoting pieces within this string.
    :param index1: Index of the piece to pull.
    :param index2: Optional end index for a range of pieces to pull.
    
    :return: Piece at the given delimited index from the provided string.
    '''
    
    if (utils.isNoneOrEmptyStr(string)):
        return ""
    
    if (utils.isNoneOrEmptyStr(delimiter)):
        return ""  # TODO: tbh I don't know what M does here lmao, just $e?

    if (index1 < 1):
        return ""  # TODO: if we do this compare against a non-numeric what happens
    
    if (utils.isNoneOrEmptyStr(index1)):
        index1 = 1

    # Default index2 to index1
    if (utils.isNoneOrEmptyStr(index2)):
        index2 = index1
    
    pieces = string.split(delimiter)
    
    # If our input index is out of bounds, that value is just empty string
    if index1 > len(pieces):
        return ""

    # Same index, just return this position 
    if index2 == index1:
        return pieces[index1 - 1]
    
    if index2 > len(pieces):
        return pieces[index1 - 1:]   # TODO: ensure this is actually correct to return to end of string
    
    return pieces[index1 - 1:index2]

### $SELECT ###

def s(condition1, value1, condition2 = True, value2 = ""):
    return __select(condition1, value1, condition2, value2)

def S(condition1, value1, condition2 = True, value2 = ""):
    return __select(condition1, value1, condition2, value2)

def select(condition1, value1, condition2 = True, value2 = ""):
    return __select(condition1, value1, condition2, value2)

def SELECT(condition1, value1, condition2 = True, value2 = ""):
    return __select(condition1, value1, condition2, value2)

def __select(condition1, value1, condition2 = True, value2 = ""):
    '''
    Evaluates a condition and returns a value based on the result.

    :param condition1: Condition to evaluate.
    :param value1: Value to return if condition is true.
    :param condition2: Optional second condition to evaluate if the first is false. Defaults to True.
    :param value2: Optional second value to return if the first condition is false. Defaults to "".
    
    :return: Value based on the evaluation of the provided conditions.
    '''
    if (condition1):
        return value1
    
    if (condition2):
        return value2
    
    return ""

# TODO: might be worth making a select_pair class here to just force a structure for the input

# TODO