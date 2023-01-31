import random
g1 = ''
g2 = ''
g_bot = ''

def confet(g1, g2, conf):
    count1 = 0
    count2 = 0
    while conf > 0:
        if conf > 28:
            print(g1)
            gamer1 = int(input('Возьмите конфеты, но не более 28: '))
            if 0< gamer1 < 29:
                conf = conf - gamer1
                count1 += count1
                print('Конфет осталось: ', conf)
            else:
                print('Значение не корректно')

            if conf > 28:
                print(g2)
                gamer2 = int(input('Возьмите конфеты, но не более 28: '))
                if 0< gamer2 < 29:
                    conf = conf - gamer2
                    count2 += count2
                    print('Конфет осталось: ', conf)
                else:
                    print('Значение не корректно')
                if conf <= 28:
                    if count2 >= count1:
                        print('Поздравляю! Победил игрок', g1)
                        conf = 0 
                    else:
                        print('Поздравляю!Победил игрок', g2)
                        conf = 0 
            else:
                if count2 >= count1:
                    print('Поздравляю! Победил игрок', g1)
                    conf = 0 
                else:
                    print('Поздравляю! Победил игрок', g2)   
                    conf = 0 

def confet_bot(g1, g_bot, conf):
    count1 = 0
    count2 = 0
    while conf > 0:
        if conf > 28:
            print(g1)
            gamer1 = int(input('Возьмите конфеты, но не более 28: '))
            if 0< gamer1 < 29:
                conf = conf - gamer1
                count1 += count1
                print('Конфет осталось: ', conf)
            else:
                print('Значение не корректно')

            if conf > 28:
                gamer2 = random.randint(1,28)
                if 0< gamer2 < 29:
                    print('Бот взял: ', gamer2)
                    conf = conf - gamer2
                    count2 += count2
                    print('Конфет осталось: ', conf)
                else:
                    print('Значение не корректно')
                if conf <= 28:
                    if count2 >= count1:
                        print('Поздравляю! Победил игрок', g1)
                        conf = 0 
                    else:
                        print('Поздравляю!Победил игрок', g_bot)
                        conf = 0 
            else:
                if count2 >= count1:
                    print('Поздравляю! Победил игрок', g1)
                    conf = 0 
                else:
                    print('Поздравляю! Победил игрок', g_bot)   
                    conf = 0 


def set_plaer_name():
    global g1
    global g2
    global g_bot
    while g1 == '':
        g1 = input ('Первый игрок:')
    g2 = input ('Второй игрок (Enter для игры против бота):')
    if not g2:
        g2 = 'Бот'
        g_bot = g2
        return True
    else:
        return False

set_plaer_name()
start = random.randint(0,1)

conf = int (input('Введите количество конфет и начнем игру:'))

if g_bot == '':
    if start == 1:
        print('Первым ходит ', g1)
        confet(g1, g2, conf)
    else:
        print('Первым ходит ', g2)
        confet(g2, g1, conf)
else:
    print('Первым ходит ', g1)
    confet_bot(g1, g_bot, conf)

