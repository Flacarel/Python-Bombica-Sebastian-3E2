def pairwise_set_operations(*sets):
    operations = {}
    sets = list(sets)
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a, b = sets[i], sets[j]
            operations[f"{a} | {b}"] = a | b
            operations[f"{a} & {b}"] = a & b
            operations[f"{a} - {b}"] = a - b
            operations[f"{b} - {a}"] = b - a
    return operations


print(pairwise_set_operations({1, 2}, {2, 3}))

