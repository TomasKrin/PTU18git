income_list = []
expence_list = []
months = {
    1: 'Sausį',
    2: 'Vasarį',
    3: 'Kovą',
    4: 'Balandį',
    5: 'Gegužę',
    6: 'Birželį',
    7: 'Liepą',
    8: 'Rugpjūtį',
    9: 'Rugsėjį',
    10: 'Spalį',
    11: 'Lapkritį',
    12: 'Gruodį',
}
while True:
    print("""
    1. Įvesti pajamas
    2. Įvesti išlaidas
    3. Atspausdinti pajamų eilutes
    4. Atspausdinti išlaidų eilutes
    5. Atspausdinti statistiką iš visų duomenų
    6. Atspausdinti statistiką iš pasirinkto mėnesio
    q - Išeiti
    """)
    print('*' * 20)
    select = input('>>>> ')

    if select == 'q':
        print('Programa baigia darbą...')
        break

    if select not in ('1', '2', '3', '4', '5', '6'):
        print('Tokio pasirinkimo nera..')
        print('*' * 20)
        continue

    if select == '1':
        month = int(input('Įveskite mėnesio skaičių: '))
        income = input('Įveskite pajamų šaltinį: ')
        income_amount = float(input('Įveskite pajamų sumą: '))
        income_list.append([month, income, income_amount])
        print('*' * 20)

    elif select == '2':
        month = int(input('Įveskite mėnesio skaičių: '))
        expence = input('Įveskite išlaidos pavadinimą: ')
        expence_amount = float(input('Įveskite išlaidos sumą: '))
        expence_list.append([month, expence, expence_amount])
        print('*' * 20)

    elif select == '3':
        print('Jūsų pajamos: ')
        for m, r, a in income_list:
            print(months[m], r, a, sep=' / ')
        print('\n', '*' * 20)

    elif select == '4':
        print('Jūsų išlaidos: ')
        for m, r, a in expence_list:
            print(months[m], r, a, sep=' / ')
        print('\n', '*' * 20)

    if (len(expence_list) == 0) and (len(income_list) == 0):
        print('Truksta duomenų..')
        continue

    elif select == '5':
        income_sum = 0
        expence_sum = 0
        most_spent = expence_list[0] if len(expence_list) != 0 else []
        most_gain = income_list[0] if len(income_list) != 0 else []
        for el in income_list:
            income_sum += el[2]
            if el[2] > most_gain[2]:
                most_gain = el
        print(f'Iš viso pajamų: {income_sum}')

        for el in expence_list:
            expence_sum += el[2]
            if el[2] > most_spent[2]:
                most_spent = el
        print(f'Iš viso išlaidų: {expence_sum}')

        print(f'Jusų pingų likutis: {income_sum - expence_sum}')
        print(f'Daugiausiai pinigų gavote {months[most_gain[0]]} - {most_gain[2]} iš {most_gain[1]}')
        print(f'Daugiausiai pinigų išleidote {months[most_spent[0]]} - {most_spent[2]} priežastis - {most_spent[1]}')
        print('*' * 20)

    elif select == '6':
        m = int(input('Įveskite norimo mėnesio skaičių: '))
        if not (m in expence_list) and (m in income_list):
            print('Truksta duomenų..')
            continue
        income_sum = 0
        expence_sum = 0
        most_spent = expence_list[0] if len(expence_list) != 0 else []
        most_gain = income_list[0] if len(income_list) != 0 else []

        for el in income_list:
            if el[0] == m:
                income_sum += el[2]
                if el[2] > most_gain[2]:
                    most_gain = el
        print(f'Iš viso pajamų {months[m]}: {income_sum}')

        for el in expence_list:
            if el[0] == m:
                expence_sum += el[2]
                if el[2] > most_spent[2]:
                    most_spent = el
        print(f'Iš viso išlaidų {months[m]}: {expence_sum}')

        print(f'Jusų pingų likutis: {income_sum - expence_sum}')
        print(f'Daugiausiai pinigų gavote {months[most_gain[0]]} - {most_gain[2]} iš {most_gain[1]}')
        print(f'Daugiausiai pinigų išleidote {months[most_spent[0]]} - {most_spent[2]} priežastis - {most_spent[1]}')
    input('ENTER --> grįžti į meniu')