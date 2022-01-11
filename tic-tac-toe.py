import random

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


def random_turn():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'

def print_board(local_board):
    print('   |   |')
    print(' ' + local_board[1] + ' | ' + local_board[2] + ' | ' + local_board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + local_board[4] + ' | ' + local_board[5] + ' | ' + local_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + local_board[7] + ' | ' + local_board[8] + ' | ' + local_board[9])
    print('   |   |')


def players_turn():
    player_input = 0
    while  player_input not in range(1,10):
        player_input = int(input('Choose index (1-9): '))
    return player_input

def check_cell_is_taken(index,local_board):
    return True if local_board[index] != ' ' else False

def board_isfull(local_board:list):
    return True if local_board.count(' ') == 0 else False


def check_for_marker(turn,marker):
    if turn == 'Player 1' and marker.lower() == 'x' or turn == 'Player 2' and marker.lower() == 'o':
        return ('x','o')
    elif turn == 'Player 1' and marker.lower() == 'o' or turn == 'Player 2' and marker.lower() == 'x':
        return ('o','x')
        
def mark_cell(index, local_board,marker):
    local_board[index] = marker


def restart():
    return input('Would you like to restart the game? (Y/N): ').lower().startswith('y')


def check_for_win(local_board, marker):
    return(
        (marker == local_board[1] and marker == local_board[2] and marker == local_board[3])
        or (marker == local_board[4] and marker == local_board[5] and marker == local_board[6])
        or (marker == local_board[7] and marker == local_board[8] and marker == local_board[9])
        or (marker == local_board[1] and marker == local_board[4] and marker == local_board[7])
        or (marker == local_board[2] and marker == local_board[5] and marker == local_board[8])
        or (marker == local_board[3] and marker == local_board[6] and marker == local_board[9])
        or (marker == local_board[1] and marker == local_board[5] and marker == local_board[9])
        or (marker == local_board[3] and marker == local_board[5] and marker == local_board[7])
    )

def main():
    turn = random_turn()
    print(f'{turn} starts first')
    choose_marker = input('Would you like to be X or O?: ')
    player1_marker,player2_marker = check_for_marker(turn,choose_marker)
    local_board = board.copy()

    while True:
        if turn == 'Player 1':
            if not board_isfull(local_board):
                index = players_turn()
                while check_cell_is_taken(index, local_board):
                    print('This cell is taken. Choose another one')
                    index = players_turn()
                else:
                    mark_cell(index, local_board, player1_marker)
                    print_board(local_board)
            else:
                print('Board is full. Draw!')
            if check_for_win(local_board, player1_marker):
                print(f'{turn} won!')
                if not restart():
                    print('Bye!')
                    exit()
                else:
                    print('Board has been reset')
                    local_board=board.copy()
            else:
                turn = 'Player 2'
        else:
            if not board_isfull(local_board):
                index = players_turn()
                while check_cell_is_taken(index, local_board):
                    print('This cell is taken. Choose another one')
                    index = players_turn()
                else:
                    mark_cell(index, local_board, player2_marker)
                    print_board(local_board)
            else:
                print('Board is full. Draw!')
            if check_for_win(local_board, player2_marker):
                print(f'{turn} won!')
                if not restart():
                    print('Bye!')
                    exit()
                else:
                    print('Board has been reset')
                    local_board=board.copy()
            turn = 'Player 1'

main()