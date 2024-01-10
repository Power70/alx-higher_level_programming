#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for pair in my_list:
        score, weight = pair
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_score / total_weight

# Example usage:
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

