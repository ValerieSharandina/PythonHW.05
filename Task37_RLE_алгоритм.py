'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах
'''



def read_file(file):
    file = open(file, 'r', encoding='utf-8')
    lines = file.readline()
    lines = [line.rstrip('\n') for line in lines]
    file.close()
    return lines
lines = read_file('encoded_text.txt')
print(lines)


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

encoded_val = rle_encode(lines)
print(encoded_val)

with open('encoded1_text.txt', 'w') as modified: modified.write(f"{encoded_val}\n")


lines = read_file('encoded1_text.txt')
print(lines)


def rle_decode(data1):
    decode = ''
    count = ''
    for char in data1:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decoded_val = rle_decode(lines)
print(decoded_val)

with open('decoded_text.txt', 'w') as modified: modified.write(f"{decoded_val}\n")



