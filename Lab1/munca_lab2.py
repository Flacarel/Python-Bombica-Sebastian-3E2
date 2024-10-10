#ex1
def decimal_to_binary(num):
    if num == 0:
        return "0b0"
    binary_digits = []
    
    while num > 0:
        binary_digits.append(str(num % 2))
        num = num // 2

    binary_digits.reverse()
    
    return "0b" + ''.join(binary_digits)

print(decimal_to_binary(13))

#ex2
def convert_to_16(nr):
    result = ''
    hexa = "0123456789ABCDEF"
    while nr:
        four = nr % 10000
        power = 0
        index = 0
        
        while four > 0:
            index += four%10 * (2**power)
            power += 1
            four //=10
        
        result = hexa[index] + result
        nr //= 10000
    return '0x' + result

print(convert_to_16(1000))

#ex3
def conversie_personalizata(sir, nr):
    baza = len(sir)
    rezultat = ""
    
    while nr > 0:
        rest = nr % baza
        rezultat = sir[rest] + rezultat 
        nr //= baza
    
    return rezultat

sir = "abcd"  
nr = 301
print(conversie_personalizata(sir, nr))  

#ex4
def conversie_in_hex(nr):
    hex_digits = "0123456789abcdef"
    rezultat = ""
    
    if nr == 0:
        return "0x0"
    
    while nr > 0:
        rest = nr % 16
        rezultat = hex_digits[rest] + rezultat
        nr //= 16
    
    return "0x" + rezultat


nr = 12345
print(conversie_in_hex(nr))  

#ex5
def verifica_paranteze(expresie):
    contor = 0
    
    for caracter in expresie:
        if caracter == '(':
            contor += 1 
        elif caracter == ')':
            contor -= 1  
            
        if contor < 0:
            return False 

    return contor == 0  


expresie1 = "6+8*(5+3/2-1+6/(3+9)-7*(5+7/3))"
expresie2 = "8-4*(3+7/8+4/(5-9)"

print(verifica_paranteze(expresie1))  
print(verifica_paranteze(expresie2))  

#ex6
def afiseaza_hex_propozitie(propozitie):
    cuvant = ""
    for caracter in propozitie:
        if caracter != " ":
            cuvant += format(ord(caracter), "02x")  
        else:
            if cuvant:
                print(cuvant)
            cuvant = ""
    
    if cuvant:  
        print(cuvant)


propozitie = "abc 012"
afiseaza_hex_propozitie(propozitie)


#ex7
def numara_majuscule(propozitie):
    numar_majuscule = 0
    
    for caracter in propozitie:
        if caracter.isupper():
            numar_majuscule += 1
    
    return numar_majuscule


propozitie = "A fost, de asemenea, Remarcabil pentru Razboaiele persane si Pentru razboaiele Dintre orasele-state Grecesti."

print(numara_majuscule(propozitie))  

#ex8
def transform(x,alfabet):
    rest=0
    word=""
    while(x):
        rest=x%len(alfabet)
        word=str(alfabet[rest])+word
        x=x//len(alfabet)
    return word
print(transform(30,"AEGIJLNOPSUVbdefhimnoprstuvwxy"))

#ex9
def primul_ultimul_caracter(propozitie):
    rezultat = ""
    inceput_cuvant = True
    primul = ""
    ultimul = ""
    
    for i in range(len(propozitie)):
        caracter = propozitie[i]
        
        if caracter.isalnum(): 
            if inceput_cuvant:
                primul = caracter
                inceput_cuvant = False
            ultimul = caracter  
        else:
            if not inceput_cuvant:
                rezultat += primul + " " + ultimul + " "
            inceput_cuvant = True 
    
    if not inceput_cuvant:  
        rezultat += primul + " " + ultimul
    
    return rezultat.strip() 


propozitie = "Exemplu de propozitie simpla"
print(primul_ultimul_caracter(propozitie))  


#10
def inversare_cuvinte(propozitie):
    rezultat = ""
    cuvant = ""
    
    for i in range(len(propozitie) - 1, -1, -1):  
        caracter = propozitie[i]
        
        if caracter != " ": 
            cuvant = caracter + cuvant
        else:
            if cuvant:
                rezultat += cuvant + " "
                cuvant = ""
    
    if cuvant:
        rezultat += cuvant
    
    return rezultat.strip() 


propozitie = "Aceasta este o propozitie inversata"
print(inversare_cuvinte(propozitie))  


#11
def numara_vocale_consoane(text):
    vocale = "aeiouAEIOU"
    numar_vocale = 0
    numar_consoane = 0
    
    for caracter in text:
        if caracter.isalpha():  
            if caracter in vocale:
                numar_vocale += 1
            else:
                numar_consoane += 1
    
    return numar_vocale, numar_consoane


text = "Aceasta este o propozitie cu multe vocale si consoane."
vocale, consoane = numara_vocale_consoane(text)
print(f"Vocale: {vocale}, Consoane: {consoane}")

#12
def este_palindrom(numar):
    numar_initial = numar
    numar_inversat = 0
    
    while numar > 0:
        cifra = numar % 10  
        numar_inversat = numar_inversat * 10 + cifra 
        numar //= 10 
    
    return numar_initial == numar_inversat


numar = 12321
print(este_palindrom(numar))  
