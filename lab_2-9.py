# Creator RW 9/21/22

while True:
    points = int(input('Enter amount of points:\n'))

    if points >= 15:
        print('you win a gold medal!')
    elif points > 11:
        print('you won a silver medal!')
    elif points > 8:
        print('you win a bronze')
    else:
        print('you arent a winner')