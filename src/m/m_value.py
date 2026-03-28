'''
Defines an M value, intended to be used in M functions that are dependent on the concept of an M value, such as $piece.
In general, we try to keep the data structures that are able to be used within this code flexible (ie allowing more 
complex structures such as objects), but there are some cases where a given function is designed around the concept 
of a string/number, therefore we have this structure to identify and support those functions.

Author: Austin Shank
Revisions:
    @AJX 2026/03/28 - Created
'''

class MValue:
    # TODO