def what_you_du():
    try:
        you_age = int(input('Введите ваш возраст: '))
        if you_age <= 16:
            print('Тебе нужно закончить школу!')
        if you_age in range(17, 29):
            print('Тебе нужно закончить ВУЗ')    
        elif you_age >= 29:
            print('Тебе пора идти работать')
    except KeyboardInterrupt:
        print("  Пока!!!") 

what_you_du()



