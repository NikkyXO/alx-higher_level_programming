#!/usr/bin/python3
def best_score(a_dictionary):
    """
        Function that returns a key with the biggest integer value
        You can assume that all values are only integers
        If no score found, return None
        You can assume all students have a different score

    """
    score = 0
    winner = None
    if type(a_dictionary) is dict:

        for k, v in a_dictionary.items():
            if v > score:
                score = v
                winner = k
        return winner
