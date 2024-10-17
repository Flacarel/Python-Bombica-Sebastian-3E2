#ex1

def char_freq(r_file,w_file):
    with open(r_file, 'r') as f:
        content = f.read()
    paragraphs = content.split()
    char_freq = dict()
    for par in paragraphs:
        for char in par:
            if char.lower() not in char_freq:
                char_freq[char.lower()] = 0
            char_freq[char.lower()] += 1
    print(char_freq)
    write_file = open(w_file,'w')
    histogram = []
    height_of_hist = max(char_freq.values())
    for i in range(height_of_hist):
        line = []
        for value in char_freq.values():
            if value <= i:
                line.append('o')
            else:
                line.append(' ')
        histogram.append(line)
    histogram.append(char_freq.keys())
    open(w_file,'w').write('\n'.join(''.join(line) for line in histogram))



#ex2
char_list = [(chr(i), i, 25 - (i - 65)) for i in range(65, 91)]
print(char_list)


#ex3

def afiseaza_tabel(text):
    text_bytes = text.encode('utf-8')
    header = "   " + " ".join(f"{i:02X}" for i in range(16))
    desparaser = "+" + '-' * 48

    print(header)
    print(desparaser)

    for index in range(0, len(text_bytes), 16):
        left = f"{index:04X}"

        byte_segment = text_bytes[index:index+16]

        right = " ".join(f"{b:02X}" for b in byte_segment)

        print(f"{left} | {right}")

afiseaza_tabel("Acesta este un exemplu mai lung")

#ex4
def hex_to_binary_matrices(hex_lists):
    with open('binary_matrices.txt', 'w') as f:
        for hex_list in hex_lists:
            matrix = ['{0:08b}'.format(num) for num in hex_list]
            for row in matrix:
                f.write(''.join(row) + '\n')
            f.write('\n')


hex_lists = [
    [0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
    [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]
]


hex_to_binary_matrices(hex_lists)
