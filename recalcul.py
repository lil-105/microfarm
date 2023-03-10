import os
import sys

cake_cost = 1.718
soul_cost = 43.056
bunch_of_peonies_cost = 3.031
tp_potion_cost = 204.952

def main():
    global cake, soul, bunch_of_peonies, tp_potion, cost
    
    print("")
    print('=' * 120)
    print(f"{' '*39}[X]    Калькулятор для склада     [X]")
    print(f"{' '*39}[X]   Актуален только для топа    [X]")
    print(f"{' '*39}[X]   Чтобы внести свои значения  [X]")
    print(f"{' '*39}[X]     Введите номер и число     [X]")
    print('=' * 120)
    print("")
    print("")
    print("")
    print(f"{' '*23}[1] Тортов: {cake} шт.")
    print(f"{' '*23}[2] Душ компании: {soul} шт.")
    print(f"{' '*23}[3] Букетов пионов: {bunch_of_peonies} шт.")
    print(f"{' '*23}[4] Зелий телепортации: {tp_potion} шт.")
    print("")
    print("")
    print("")
    if cost >= 1000:
        print(f"{' '*39}Итоговая стоимость склада: ", "{:.3f}".format(cost / 1000), "скстлн.")
    else:
        print(f"{' '*39}Итоговая стоимость склада: ", "{:.3f}".format(cost), "квнтл.")
    print(f"{' '*40}Чтобы завершить работу нажмите ENTER.")
    print("")
    print(f"{' '*51}MADE BY POCHKA")
    print("")

cake = 0
soul = 0
bunch_of_peonies = 0
tp_potion = 0
cost = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost

while True:
    main()
    choice = input(f"{' '*20}Ввод: ")
    if len(choice) == 0:
        break
    if not choice.isdigit():
        os.system('cls')
        print('\033[31m' + f"\n{' '*42}[Ошибка: Введите только число.]" + '\033[0m')
        continue

    choice = int(choice)
    if choice == 0:
        os.system('cls')
        print(f"\n{' '*20}Экран очищен.") #Позже удалить
    elif choice == 1:
        icake = input(f"{' '*20}Введите новое значение: ")
        if not icake.isdigit():
            os.system('cls')
            print('\033[31m' + f"\n{' '*42}[Ошибка: Введите только число.]" + '\033[0m')
            continue
        cake = int(icake)
        cost = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost
        os.system('cls')
    elif choice == 2:
        isoul = input(f"{' '*20}Введите новое значение: ")
        if not isoul.isdigit():
            os.system('cls')
            print('\033[31m' + f"\n{' '*42}[Ошибка: Введите только число.]" + '\033[0m')
            continue
        soul = int(isoul)
        cost = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost
        os.system('cls')
    elif choice == 3:
        ibunch_of_peonies = input(f"{' '*20}Введите новое значение: ")
        if not ibunch_of_peonies.isdigit():
            os.system('cls')
            print('\033[31m' + f"\n{' '*42}[Ошибка: Введите только число.]" + '\033[0m')
            continue
        bunch_of_peonies = int(ibunch_of_peonies)
        cost = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost
        os.system('cls')
    elif choice == 4:
        itp_potion = input(f"{' '*20}Введите новое значение: ")
        if not itp_potion.isdigit():
            os.system('cls')
            print('\033[31m' + f"\n{' '*42}[Ошибка: Введите только число.]" + '\033[0m')
            continue
        tp_potion = int(itp_potion)
        cost = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost
        os.system('cls')
    else:
    	os.system('cls')
    	cost = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost
    	print('\033[31m' + f"\n{' '*42}[Ошибка: Введите только число.]" + '\033[0m')
    	continue

