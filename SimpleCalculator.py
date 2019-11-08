def calculator():
	print('\nДобрый день. Я калькулятор. Делаю прибавление, и вычетание\n')
	q =input('Выберите Ваше действие: 1=прибавление, 2=вычетание\n\nВаш ответ:')
	if q=='1':
		a= input('Введите число, которое будем прибавлять : ')
		b= input('Введите второе число, которое будем прибавлять : ')
		c = int(a) + int(b) 
		print('\nВаш ответ равен : ' + str(c))
		again()
	
	elif q=='2':
		a= input('Введите число, от которого будем отнимать : ')
		b= input('Введите второе число, которое будем отнимать : ')
		c= int(a) - int(b) 
		print('\nВаш ответ равен : ' + str(c))
		again()
	
def again():
    while True:
        r=input('\nIf you want to do this again tap 1, if no tap 2 : ')
        if r=='2':
            print('Спасибо, пока')
            break
        elif r=='1':
            calculator()
calculator()
