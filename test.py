suma = 0

while True:
    user_inp = input('Įveskite skaičių: ')
    print(user_inp)
    if user_inp.replace('.', '', 1).lstrip('-').isdigit():
        number = float(user_inp)
        if number < 0:
            print('Įvestas neigiamas skaičius')
            break
        suma += number
    else:
        print('Jūs nurodėte ne skaičių....')
        break
if type(suma) == float:
    if suma.is_integer():
        print(f'Jūsų įvestų skaičių suma yra: {int(suma)}')
    else:
        print(f'Jūsų įvestų skaičių suma yra: {suma}')
print('Hello GITHUB')
