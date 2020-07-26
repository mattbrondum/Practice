
# Recursion practice

test_list = [1, 2, [3, 4], [[5, 6], [[[[7]]]]]]
# Write a function to flatten a list of lists


def flatten_list(input_val, result=None):
    if result is None:
        result = []

    for val in input_val:
        if isinstance(val, list):
            flatten_list(val, result)
        else:
            result.append(val)

    return result


print(flatten_list(test_list))




