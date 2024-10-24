#ex1
def fibonacci_string(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibo = [0, 1]
    for i in range(n - 2):
        next_fibo = fibo[-1] + fibo[-2]
        fibo.append(next_fibo)

    return fibo


print(fibonacci_string(10))

#ex2
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def nrPrime(n):
    primes = []
    for i in n:
        if isPrime(i):
            primes.append(i)

    return primes


print(nrPrime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#ex3
def operations(a, b):
    intersection = []
    for i in a:
        if i in b:
            intersection.append(i)
    reunion = []
    for i in a:
        reunion.append(i)
    for i in b:
        if i not in reunion:
            reunion.append(i)
    differenceA = []
    for i in a:
        if i not in b:
            differenceA.append(i)

    differenceB = []
    for i in b:
        if i not in a:
            differenceB.append(i)

    return intersection, reunion, differenceA, differenceB


print(operations([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

#ex4
def compose(musical_notes, moves, start):
    song = []
    limita = len(musical_notes)
    song.append(musical_notes[start])
    for i in moves:
        if start + i > limita:
            song.append(musical_notes[(start + i) % limita])
            start = (start + i) % limita
        else:
            song.append(musical_notes[start + i])
            start = start + i
    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

#ex5
def matrix(m):
    lines = len(m)
    columns = len(m[0])
    for i in range(lines):
        for j in range(columns):
            if i > j:
                m[i][j] = 0
    return m


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(matrix(m))

#ex6
def exact(x,*lists):
    frecv={}
    total=[]
    for list in lists:
        for i in list:
            if i in frecv:
                frecv[i]+=1
            else:
                frecv[i]=1
    for i in frecv:
        if frecv[i]==x:
            total.append(i)
    return total


print(exact(2,[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))

#ex7
def isPalindrom(n):
    return str(n)==str(n)[::-1]

def tuplu(list):
    max=-1
    count=0
    for i in list:
        if isPalindrom(i) is True:
            count+=1
            if(i>max):
                max=i
    return (count,max)

result = tuplu([123, 456, 789, 10, 11, 22, 101])
print(result)

#ex8
def filter_by_ascii(x=1, string_list=None, flag=True):
    if string_list is None:
        string_list = []
    
    result = []
    
    for s in string_list:
        if flag:
            filtered_chars = [char for char in s if ord(char) % x == 0]
        else:
            filtered_chars = [char for char in s if ord(char) % x != 0]
        result.append(filtered_chars)
    
    return result

x = 2
string_list = ["test", "hello", "lab002"]
flag = False
output = filter_by_ascii(x, string_list, flag)
print(output)

#ex9
def find_blocked_spectators(matrix):
    blocked_seats = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for row in range(1, rows): 
        for col in range(cols):
            for prev_row in range(0, row):  
                if matrix[prev_row][col] >= matrix[row][col]:
                    blocked_seats.append((row, col))
                    break 
    
    return blocked_seats

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
output = find_blocked_spectators(matrix)
print(output)

#ex10
def zip_with_none(*lists):
    max_len = max(len(lst) for lst in lists) 
    result = []
    
    for i in range(max_len):
        tuple_item = tuple(lst[i] if i < len(lst) else None for lst in lists)  
        result.append(tuple_item)
    
    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

output = zip_with_none(list1, list2, list3)
print(output)

#ex11

def get_third_char_of_second_element(t):
    return t[1][2]

def sort_by_third_char(tuples_list):
    return sorted(tuples_list, key=get_third_char_of_second_element)

input_list = [('abc', 'bcd'), ('abc', 'zza')]
output = sort_by_third_char(input_list)
print(output)

#ex12
def group_by_rhyme(words):
    rhyme_dict = {}  
    
    for word in words:
        rhyme_key = word[-2:]
        if rhyme_key not in rhyme_dict:
            rhyme_dict[rhyme_key] = []
        
        rhyme_dict[rhyme_key].append(word)
    
    return list(rhyme_dict.values())

input_words = ['ana', 'banana', 'carte', 'arme', 'parte']
output = group_by_rhyme(input_words)
print(output)
