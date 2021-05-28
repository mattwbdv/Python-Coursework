game_board = {'(1, 1)': '  ', '(1, 2)': '  ', '(1, 3)': '  ',
            '(2, 1)': '  ', '(2, 2)': '  ', '(2, 3)': '  ',
            '(3, 1)': '  ', '(3, 2)': '  ', '(3, 3)': '  '}


def print_board(game_board):
    print('  1  2  3')
    print('1 ' + game_board['(1, 1)'] + '|' + game_board['(1, 2)'] + '|' + game_board['(1, 3)'])
    print('  --+--+--')
    print('2 ' + game_board['(2, 1)'] + '|' + game_board['(2, 2)'] + '|' + game_board['(2, 3)'])
    print('  --+--+--')
    print('3 ' + game_board['(3, 1)'] + '|' + game_board['(3, 2)'] + '|' + game_board['(3, 3)'])


def game():
    turn = ' X'
    count = 0

    for i in range(10):
        print_board(game_board)
        print("Enter " + turn + " move (row,column no spaces)>")
        move = str(tuple(map(int, raw_input().split(','))))

        if str(game_board[move]) == '  ':
            game_board[move] = turn
            count += 1

        else:
            print("Invalid move, try again.")
            continue

        if count >= 5:
            if game_board['(1, 1)'] == game_board['(1, 2)'] == game_board['(1, 3)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break
            elif game_board['(3, 2)'] == game_board['(2, 2)'] == game_board['(1, 2)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break
            elif game_board['(3, 3)'] == game_board['(2, 3)'] == game_board['(1, 3)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break
            elif game_board['(1, 1)'] == game_board['(2, 2)'] == game_board['(3, 3)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break
            elif game_board['(3, 1)'] == game_board['(2, 2)'] == game_board['(1, 3)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break

            elif game_board['(2, 1)'] == game_board['(2, 2)'] == game_board['(2, 3)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break
            elif game_board['(3, 1)'] == game_board['(3, 2)'] == game_board['(3, 3)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break
            elif game_board['(3, 1)'] == game_board['(2, 1)'] == game_board['(1, 1)'] != ' ':
                print_board(game_board)
                print(turn + " is the winner!")
                break

        if count == 9:
            print("There are no more moves. It's a tie!")

        if turn == ' X':
            turn = ' O'
        else:
            turn = ' X'


if __name__ == "__main__":
    game()

