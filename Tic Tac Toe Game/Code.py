def display_layout(B):
    print('        *    '+'     *    ')
    print('        *    '+'     *    ')
    print('   '+B[1]+'    *    '+B[2]+'    *    '+B[3])
    print('        *    '+'     *    ')
    print('* * * * * * * * * * * * * *')
    print('        *    '+'     *    ')
    print('   '+B[4]+'    *    '+B[5]+'    *    '+B[6])
    print('        *    '+'     *    ')
    print('* * * * * * * * * * * * * *')
    print('        *    '+'     *    ')
    print('   '+B[7]+'    *    '+B[8]+'    *    '+B[9])
    print('        *    '+'     *    ')
    print('        *    '+'     *    ')
def welcome():
    print('WELCOME TO TIC TAC TOE GAME CREATED BY SHIKHAR MISHRA')
    print('NEW GAME -> ENTER 1')
    print('QUIT -> ENTER 2')
    user_response = input()
    if user_response == '1':
        new_game()
    elif user_response == '2':
        print('GOODBYE')
    else:
        print('INCORRECT RESPONSE, TRY AGAIN')
        welcome()
def new_game():
    contents = ['NA',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player_1 = player_2 = ''
    print('IT IS A TWO PLAYER GAME, THEY ARE PLAYER 1 AND PLAYER 2')
    print('LETS CHOOSE RANDOMLY WHO WILL GO FIRST')
    import random
    flip = random.randint(1,2)
    if flip == 1:
        print('PLAYER 1 GOT SELECTED RANDOMLY')
        player_1,player_2 = choose_marker(1)
        game_on(flip,player_1,player_2,contents)
    else:
        print('PLAYER 2 GOT SELECTED RANDOMLY')
        player_1,player_2 = choose_marker(2)
        game_on(flip,player_1,player_2,contents)
def choose_marker(a):
    print(f'PLAYER {a} CHOOSE YOUR MARKER BETWEEN X OR O')
    mark = input()
    if a ==1:
        if mark == 'X':
            return ('X','O')
        elif mark == 'O':
            return ('O','X')
    elif a == 2:
        if mark == 'X':
            return ('O','X')
        elif mark == 'O':
            return ('X','O')
    else:
        print('INVALID INPUT, TRY AGAIN')
        return choose_marker(a)
def game_on(a,b,c,d):
    gaming = True
    display_layout(d)
    while gaming:
        if a == 1:
            pos = 10
            while pos not in [1,2,3,4,5,6,7,8,9]:
                print(f'PLAYER {a} CHOOSE POSITION FROM 1 TO 9 TO PLACE YOUR MARKER')
                pos = int(input())
            if d[pos] == ' ':
                d[pos] = b
                display_layout(d)
                a = 2
                if winning(b,d):
                    print('PLAYER 1 WINS')
                    gaming = False
                if full_check(d):
                    gaming = False
            else:
                print('THAT PLACE IS TAKEN, TRY AGAIN')
                game_on(a,b,c,d)
        elif a == 2:
            pos = 10
            while pos not in [1,2,3,4,5,6,7,8,9]:
                print(f'PLAYER {a} CHOOSE POSITION FROM 1 TO 9 TO PLACE YOUR MARKER')
                pos = int(input())
            if d[pos] == ' ':
                d[pos] = c
                display_layout(d)
                a = 1
                if winning(c,d):
                    print('PLAYER 2 WINS')
                    gaming = False
                if full_check(d):
                    gaming = False
            else:
                print('THAT PLACE IS TAKEN, TRY AGAIN')
                game_on(a,b,c,d)
    else:
        gaming = False
        lastly()
def winning(mark,d):
    return ((d[1]==d[2]==d[3]==mark) or (d[4]==d[5]==d[6]==mark) or
           (d[7]==d[8]==d[9]==mark) or (d[1]==d[4]==d[7]==mark) or
            (d[2]==d[5]==d[8]==mark) or (d[3]==d[6]==d[9]==mark) or
            (d[1]==d[5]==d[9]==mark) or (d[3]==d[5]==d[7]==mark))
def full_check(d):
    for i in range(1,10):
        if d[i] == ' ':
            return False
    return True
def lastly():
    print('WANT TO PLAY AGAIN ? YES OR NO')
    last = input()
    if last == 'YES':
        new_game()
    elif last == 'NO':
        print('GOODBYE')
    else:
        print('WRONG INPUT, TRY AGAIN')
        lastly()
welcome()
