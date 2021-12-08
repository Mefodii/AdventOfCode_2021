from collections import Counter


def list_to_int(data):
    return list(map(int, data))


def subtract_string_list(list1, list2):
    return list((Counter(list1)-Counter(list2)).elements())