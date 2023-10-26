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
