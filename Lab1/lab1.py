#ex1
def cmmdc(a, b):
    while b != 0:
        aux = a % b
        a = b
        b = aux
    return a


def gaseste_cmmdc():
    n = int(input("Introdu numarul de numere: "))
    rezultat = int(input("Introdu primul numar: "))
    for i in range(2, n + 1):
        num = int(input(f"Introdu al {i}-lea numar: "))
        rezultat = cmmdc(rezultat, num)

    return rezultat


print(gaseste_cmmdc())


# ex2
def vocale(cuvant):
    vocale = "aeiouAEIOU"
    nrVocale = 0
    for i in range(len(cuvant)):
        if cuvant[i] in vocale:
            nrVocale += 1
    return nrVocale


print(vocale("AEaac"))


# ex3
def aparitii(a, b):
    return b.count(a)


print(aparitii("of", "cofbofloofof"))


# ex4
def convert(string):
    result = ""
    index = 0
    for char in string:
        if char.isupper() and index != 0:
            result += "_"
        result += char.lower()
        index += 1
    return result


print(convert("AcasaLaMine"))


# ex5
def palindrom(numar):
    return str(numar) == str(numar)[::-1]


print(palindrom(101))


# ex6
def extragere(cuvant):
    numar = ""
    for i in cuvant:
        if i.isdigit():
            numar += i
        elif numar:
            break
    if numar:
        return int(numar)
    else:
        return None


print(extragere("ab12c5"))
print(extragere("abc"))


# ex7
def biti(numar):
    return bin(numar).count("1")


print(biti(24))


# ex8
def words(prop):
    count = prop.strip().split()
    return len(count)


print(words("Ana are mere si pere"))
