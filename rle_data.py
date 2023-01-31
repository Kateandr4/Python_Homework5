
def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond

def file_decode(decod_txt):
    decode = ''
    count = ''
    for char in decod_txt:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode



with open('text.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open('text.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()
print(my_txt)

txt_compr = file_encod(my_txt)

with open('text_code.txt', 'w') as file:
    file.write(f'{txt_compr}')
print(txt_compr)
#---------------------

with open('text_code.txt', 'w') as file:
    file.write(input('Напишите текст необходимый для распаковки: '))
with open('text_code.txt', 'r') as file:
    my_txt2 = file.readline()
    txt_compr2 = my_txt.split()
print(my_txt)

txt_compr2 = file_decode(my_txt2)

with open('text.txt', 'w') as file:
    file.write(f'{txt_compr2}')
print(txt_compr2)

