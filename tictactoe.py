bord_num = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]

def select_char():
    while True: 
        player1char = input('player1 choose between "x" or "o" :\n')
        if player1char == 'x':
            return 'X', 'O'
        elif player1char == 'o':
            return 'O', 'X'

def board():
    print(f"""
    {bord_num[1]} | {bord_num[2]} | {bord_num[3]}
    ---------
    {bord_num[4]} | {bord_num[5]} | {bord_num[6]}
    ---------
    {bord_num[7]} | {bord_num[8]} | {bord_num[9]}
    """)

def playing():
    count = 0
    value = 0
    win = [
        [bord_num[1], bord_num[5], bord_num[9]],
        [bord_num[3], bord_num[5], bord_num[7]],
        [bord_num[1], bord_num[2], bord_num[3]],
        [bord_num[4], bord_num[5], bord_num[6]],
        [bord_num[7], bord_num[8], bord_num[9]],
        [bord_num[1], bord_num[4], bord_num[7]],
    ]
    win2 = [
        [bord_num[2], bord_num[5], bord_num[8]],
        [bord_num[3], bord_num[6], bord_num[9]]
    ]
    def win_check():
        for _ in win:
            if _ == [player1char, player1char, player1char]:
                return 1, 'player1 is the winer'
            elif _ == [player2char, player2char, player2char]:
                return 1, 'player2 is the winer'
        else:
            for _ in win2:
                if _ == [player1char, player1char, player1char]:
                    return 1, 'player1 is the winer'
                elif _ == [player2char, player2char, player2char]:
                    return 1, 'player2 is the winer'
                else:
                    return 0, 'play the game'
    
    print()
    print("Your board")
    board()

    while True:
        
        while True:
            player1 = int(input("player1 enter a number:\n"))
            if player1 in range(1, 10):
                if type(bord_num[player1]) == str:
                    print("player1 choose a other number")
                else:
                    bord_num[player1] = player1char
                    count += 1
                    break
        board()

        win = [
            [bord_num[1], bord_num[5], bord_num[9]],
            [bord_num[3], bord_num[5], bord_num[7]],
            [bord_num[1], bord_num[2], bord_num[3]],
            [bord_num[4], bord_num[5], bord_num[6]],
            [bord_num[7], bord_num[8], bord_num[9]],
            [bord_num[1], bord_num[4], bord_num[7]],
        ]
        win2 = [
            [bord_num[2], bord_num[5], bord_num[8]],
            [bord_num[3], bord_num[6], bord_num[9]]
        ]

        value,win_cot = win_check()
        if value == 1:
            print(win_cot)
            break
        
        if count == 9:
            print('draw match')
            break

        while True:
            player2 = int(input('player2 enter a number:\n'))
            if player2 in range(1, 10):
                if type(bord_num[player2]) == str:
                    print("player2 choose another number")
                else:
                    bord_num[player2] = player2char
                    count += 1
                    break
        board()
        win = [
            [bord_num[1], bord_num[5], bord_num[9]],
            [bord_num[3], bord_num[5], bord_num[7]],
            [bord_num[1], bord_num[2], bord_num[3]],
            [bord_num[4], bord_num[5], bord_num[6]],
            [bord_num[7], bord_num[8], bord_num[9]],
            [bord_num[1], bord_num[4], bord_num[7]],
        ]
        win2 = [
            [bord_num[2], bord_num[5], bord_num[8]],
            [bord_num[3], bord_num[6], bord_num[9]]
        ]

player1char, player2char = select_char()

print(f'player1= {player1char}')
print(f'player2= {player2char}')

playing()


