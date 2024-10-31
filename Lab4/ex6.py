def unique_and_duplicates(lst):
    unique_elements = set(lst)
    unique_count = len(unique_elements)
    duplicate_count = len(lst) - unique_count
    return unique_count, duplicate_count


lst = [1, 2, 2, 3, 4, 4, 5]
print(unique_and_duplicates(lst))

