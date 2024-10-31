def compare_dicts(dict1, dict2):
    if dict1.keys() != dict2.keys():
        return False
    for key in dict1:
        if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            if not compare_dicts(dict1[key], dict2[key]):
                return False
        elif isinstance(dict1[key], (list, set)) and isinstance(dict2[key], (list, set)):
            if set(dict1[key]) != set(dict2[key]):
                return False
        else:
            if dict1[key] != dict2[key]:
                return False
    return True


dict1 = {'a': 1, 'b': {'c': 3}}
dict2 = {'a': 1, 'b': {'c': 3}}
print(compare_dicts(dict1, dict2))