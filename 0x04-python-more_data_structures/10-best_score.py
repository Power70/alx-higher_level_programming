#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    all_scores = list(a_dictionary.values())
    max = all_scores[0]

    for i in range(len(all_scores) - 1):
        if (max < all_scores[i + 1]):
            max = all_scores[i + 1]

    for key in a_dictionary:
        if a_dictionary[key] == max:
            return key
