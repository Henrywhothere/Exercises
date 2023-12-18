theboard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

a = 'X'
for i in range(9):
    printboard(theboard)
    print('Turn for ' + a)
    b = input('type your place: ')
    theboard[b] = a
    if a == 'X':
        a = 'O'
    else:
        a = 'X'

printboard(theboard)
