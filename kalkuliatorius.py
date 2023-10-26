menu_variants = ('1', '2', '3', '4', '5')
history = []
print('Skaičiuotuvas\n')
while True:
    print('1. Sudėtis \n'
          '2. Atimtis \n'
          '3. Daugyba \n'
          '4. Dalyba \n'
          '5. Atspausdinti skaičių seką nuo x iki y \n'
          'Baigti darbą - q')
    print('*' * 30)
    selection = input('>>>> ')

    if selection == 'q':
        print('Atliktų veiksmų istorija: \n')
        for el in history:
            if type(el) == list:
                print(*el)
            else:
                print(el)
        break

    if not selection in menu_variants:
        print('Tokio pasirinkimo nėra..')
        print('*' * 30)
        continue

    x = float(input('Įveskite pirmą skaičių: '))
    y = float(input('Įveskite antrą skaičių: '))
    x_int_check = int(x) if x.is_integer() else x
    y_int_check = int(y) if y.is_integer() else y

    if selection == '1':
        res = x + y
        res_int_check = int(res) if res.is_integer() else res
        res_string = f'{x_int_check} + {y_int_check} = {res_int_check}'
        print(res_string)
        history.append(res_string)
        print('*' * 30)

    elif selection == '2':
        res = x - y
        res_int_check = int(res) if res.is_integer() else res
        res_string = f'{x_int_check} - {y_int_check} = {res_int_check}'
        print(res_string)
        history.append(res_string)
        print('*' * 30)
