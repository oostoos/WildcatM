'''
Common utility functions for WildcatM.
'''

'''
Author: Austin Shank
Revisions:
    @AJX 2025-12-04 - Created
'''

def isNoneOrEmptyStr(value):
    '''
    Checks if a value is None or an empty string.

    :param value: Value to check.
    
    :return: True if the value is None or an empty string, False otherwise.
    '''
    return (value == None) or (value == "")