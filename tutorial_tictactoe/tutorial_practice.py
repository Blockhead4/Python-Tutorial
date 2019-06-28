import itertools 

game = [[2, 1, 1],
        [1, 1, 0],
        [1, 0, 2]]

def win(current_game):

    # horizontal    
    for i, row in enumerate(game):
        print(i, row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print('player ?? is the winner horizontally!! (-)') 
            return True

    # vertical
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print('player ?? is the winner vertically!! (-)') 
            return True

    # diagonal
    diags = []
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])    
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print('player ?? is the winner diagnolly!! (/)')
        return True 

    diags = []
    for row, col in enumerate(range(len(game))):
        diags.append(game[row][col])
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print('player ?? is the winner diagnolly!! (\\)')
        return True

    return False


def game_board(plyaer=0, row=0, column=0, just_display=False):

    print("   "+ "  ".join([str(i) for i in range(len(game))]))
    for i, row in enumerate(game):
        print(i, row)

game_board()
