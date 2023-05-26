points1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
points2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
points3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
points4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
points5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
points8 = ['J', 'X', 'Ш', 'Э', 'Ю']
points10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

print('Введите слово:')
s = input()
sum = 0
for i in s:
    if i.upper() in points1:
        sum +=1
    elif i.upper() in points2:
        sum +=2
    elif i.upper() in points3:
        sum +=3
    elif i.upper() in points4:
        sum +=4
    elif i.upper() in points8:
        sum +=8
    elif i.upper() in points10:
        sum +=10
    else:
        print('Строка содержит некорректные символы')
        raise SystemExit(1)

print('Количество очков: ' + str(sum))
