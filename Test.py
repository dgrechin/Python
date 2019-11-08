def calculate():

   

    print('\nТЕСТ: НАСКОЛЬКО ВЫ ЗЛОПАМЯТНЫЙ ЧЕЛОВЕК? =)\n')
    Answer1 =input('Для начала выберите Позволите ли Вы сфотографировать себя в день рождения? : \n'
                    '1: отографироваться – это моя страсть\n'
                    '2: сделать этого не позволю, т. к. плохо получаюсь на фотографиях\n'
                    '3: разрешу, но в душе буду злиться\n'
                    'Ваш ответ : ')
    if(Answer1 == '1') or (Answer1 == '2') or (Answer1 == '3'):
    
        Answer2 = input('\nВы хотите позвонить, но телефонная будка занята очень долго, Вы: \n'
                    '1: вежливо просите освободить кабину \n'
                    '2: будете стоять и ждать\n'
                    '3: не отстанете, пока не добьетесь своего\n'
                    'Ваш ответ : ')
        if(Answer2 == '1') or (Answer2 == '2') or (Answer2 == '3'):

            Answer3 = input('\nСчитаете ли Вы, что у Вас есть недостатки, от которых нужно избавляться?\n'
                    '1: у меня очень много таких недостатков\n'
                    '2: я обладаю только одним серьезным недостатком\n'
                    '3: я человек без недостатков\n'
                    'Ваш ответ : ')



            if((Answer1 == '1') and (Answer2 == '1') and (Answer3 == '1')
               or (Answer1 == '2') and (Answer2 == '1') and (Answer3 == '1')
               or (Answer1 == '3') and (Answer2 == '1') and (Answer3 == '1')
               or (Answer1 == '1') and (Answer2 == '2') and (Answer3 == '1')
               or (Answer1 == '1') and (Answer2 == '3') and (Answer3 == '1')
               or (Answer1 == '1') and (Answer2 == '1') and (Answer3 == '2')
               or (Answer1 == '1') and (Answer2 == '1') and (Answer3 == '3')
               or (Answer1 == '3') and (Answer2 == '1') and (Answer3 == '2')
               or (Answer1 == '1') and (Answer2 == '3') and (Answer3 == '2')):
                    print('\nВот ваш ответ : Вы очень спокойный человек\n')
                    play_again()
        
            elif((Answer1 == '2') and (Answer2 == '2') and (Answer3 == '1')
                 or (Answer1 == '3') and (Answer2 == '2') and (Answer3 == '1')
                 or (Answer1 == '2') and (Answer2 == '3') and (Answer3 == '1')
                 or (Answer1 == '2') and (Answer2 == '1') and (Answer3 == '2')
                 or (Answer1 == '2') and (Answer2 == '1') and (Answer3 == '3')
                 or (Answer1 == '3') and (Answer2 == '2') and (Answer3 == '1')
                 or (Answer1 == '3') and (Answer2 == '3') and (Answer3 == '1')
                 or (Answer1 == '3') and (Answer2 == '2') and (Answer3 == '3')
                 or (Answer1 == '2') and (Answer2 == '2') and (Answer3 == '2')):
                     print('\nВот ваш ответ : Вы относительно спокойный человек\n')
                     play_again()
                      
                 
            elif((Answer1 == '1') and (Answer2 == '2') and (Answer3 == '3')
                 or (Answer1 == '1') and (Answer2 == '3') and (Answer3 == '3')
                 or (Answer1 == '2') and (Answer2 == '3') and (Answer3 == '3')
                 or (Answer1 == '3') and (Answer2 == '3') and (Answer3 == '3')
                 or (Answer1 == '3') and (Answer2 == '2') and (Answer3 == '2')
                 or (Answer1 == '2') and (Answer2 == '2') and (Answer3 == '3')
                 or (Answer1 == '2') and (Answer2 == '3') and (Answer3 == '2')
                 or (Answer1 == '3') and (Answer2 == '3') and (Answer3 == '2')
                 or (Answer1 == '1') and (Answer2 == '2') and (Answer3 == '2')):
                     print('\nВот ваш ответ : Вы совсем не спокойный человек\n')
                     play_again()
           

            else:
                print('1Вы случайно нажали не то. Запустите тест еще раз')
                play_again()
        else:
            print ('2Вы случайно нажали не то. Запустите тест еще раз')
            play_again()


   
            
    
    else:
        print ('\nВы случайно нажали не то. Запустите тест еще раз')
        play_again()

def play_again():
    while True :
        again = input("Если хотите начать заново введите 1 или если не хотите введите 2\nВаш ответ : ")           
        if again not in {"1","2"}:
             print("Введите еще раз")               
        elif again == "2":
            print( "Спасибо, до свидания")
            break
        elif again == "1":
            calculate()
calculate()
   

