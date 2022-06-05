#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first
    character
    """
    s_length = len(sentence)
    if s_length == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return ((s_length, f_char))
