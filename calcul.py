import gc
gc.collect()

cake_cost = 			1.718
soul_cost = 			43.056
bunch_of_peonies_cost = 3.031
tp_potion_cost = 		204.952

print("==========================")
print("- Калькулятор для склада  ")
print("- Актуален только для топа")
print("==========================")
print(" ")
print(" ")
print(" ")

while True:
	icake = input("Введите количество тортов: ")
	if icake.isdigit():
		cake = int(icake)
		break
	else:
		print(" ")
		print("- Введите число.")
		print(" ")
		print("- " * 50)
		print(" ")

print(" ")
print("- Ваше количество тортов: ", cake)
print(" ")
print("- " * 50)
print(" ")

while True:
	isoul = input("Введите количество душ: ")
	if isoul.isdigit():		
		soul = int(isoul)
		break
	else:
		print(" ")
		print("- Введите число.")
		print(" ")
		print("- " * 50)
		print(" ")

print(" ")
print("- Ваше количество душ: ", soul)
print(" ")
print("- " * 50)
print(" ")

while True:
	ibunch_of_peonies = input("Введите количество букетов пионов: ")
	if ibunch_of_peonies.isdigit():
		bunch_of_peonies = int(ibunch_of_peonies)
		break
	else:
		print(" ")
		print("- Введите число.")
		print(" ")
		print("- " * 50)
		print(" ")

print(" ")
print("- Ваше количество букетов пионов: ", bunch_of_peonies)
print(" ")
print("- " * 50)
print(" ")

while True:
	itp_potion = input("Введите количество зелий телепортации: ")
	if itp_potion.isdigit():
		tp_potion = int(itp_potion)
		break
	else:
		print(" ")
		print("- Введите число.")
		print(" ")
		print("- " * 50)
		print(" ")

print(" ")
print("- Ваше количество тортов: ", tp_potion)
print(" ")
print("- " * 50)
print(" ")

result = cake * cake_cost + soul * soul_cost + bunch_of_peonies * bunch_of_peonies_cost + tp_potion * tp_potion_cost


if result >= 1000:
	print("Общая стоимость продуктов на складе: ", "{:.3f}".format(result / 1000), "скстлн.")
else:
	print("Общая стоимость продуктов на складе: ", "{:.3f}".format(result), "квнтл.")

input("Нажмите клавишу ENTER чтобы выйти.")
