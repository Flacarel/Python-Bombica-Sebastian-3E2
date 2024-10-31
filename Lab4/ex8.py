def find_loop(mapping):
    result = []
    current = mapping.get("start")
    visited = set()
    while current not in visited and current in mapping:
        visited.add(current)
        result.append(current)
        current = mapping[current]
    return result


mapping = {'start': 'a', 'a': '6', '6': 'z', 'z': '2', '2': '2'}
print(find_loop(mapping))

