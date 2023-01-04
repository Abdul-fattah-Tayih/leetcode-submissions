from typing import List

def lists_contain_same_items(first_list: List, second_list: List) -> bool:
    """
        Determine whether 2 unsorted lists contain the same elements regardless of order
    """
    if len(first_list) != len(second_list):
        return False

    first_list.sort()
    second_list.sort()

    return first_list == second_list