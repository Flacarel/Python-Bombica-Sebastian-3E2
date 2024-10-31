def set_operations(a, b):
    a_set, b_set = set(a), set(b)
    return [
        a_set & b_set,  
        a_set | b_set, 
        a_set - b_set,  
        b_set - a_set    
    ]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print(set_operations(a, b))