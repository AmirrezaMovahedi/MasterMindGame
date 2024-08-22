password = None
guess = None
player_tries = [0, 0]
password_len = 0
turn = 1
player_turn = 1
check_list = []
flag = True


def check(pw, gu):
    check_status = False
    for char, y in zip(pw, range(len(pw))):
        if char == gu[y]:
            check_list[y] = char
            check_status = True
        elif check_list[y] is None or check_list[y] == 'X':
            check_list[y] = 'X'
    if check_status:
        return check_status
    else:
        return check_status


while flag:

    while True:
        password = input(f'Player {player_turn} , please enter password: ')

        if not password.isnumeric():
            print('Try again')
            continue
        elif len(password) < 4:
            print('The number of code digits must be four or more.')
            continue
        else:
            password_len = len(password)
            check_list = [None] * password_len
            print(10 * '\n')
            if player_turn == 1:
                player_turn = 2
            else:
                turn = 2
                player_turn = 1
            break

    while True:
        guess = input(f'Player {player_turn}, please enter your guess: (password len = {password_len}) ')

        if not password.isnumeric():
            print('Please use numbers.')
            continue
        elif len(guess) != password_len:
            print('The number of letters guessed by you is not the same as the number of the password.')
            continue
        elif guess == password and player_tries[turn - 1] == 0:
            check_list = [None] * password_len
            print(f'Player {player_turn} win!!')
            exit()
        elif guess == password:
            print(f'player {player_turn} Number of player attempts = {player_tries[turn - 1]}')
            check_list = [None] * password_len
            if player_turn == 1:
                flag = False
            break
        elif check(password, guess):
            player_tries[turn - 1] += 1
            for x in check_list:
                print(x, end=' ')
            print('Try again')
        else:
            for x in check_list:
                print(x, end=' ')
            player_tries[turn - 1] += 1
            print(f'The number of attempts you have made so far {player_tries[turn - 1]}')

else:
    if player_tries[0] < player_tries[1]:
        print('Player number tow wins')
    elif player_tries[0] > player_tries[1]:
        print('Player number one wins')
    else:
        print('The game was tied.')
