from random import randint

SIZE_N = 5
SIZE_M = 5

point_x = randint(0, SIZE_N - 1)
point_y = randint(0, SIZE_M - 1)

finish_point_x = randint(0, SIZE_N - 1)
finish_point_y = randint(0, SIZE_M - 1)

game_map = ''
input_value = ''

score = 0

while(True):

    for m in range(SIZE_M):
        row = '|'
        for n in range(SIZE_N):
            if point_x == n and point_y == m:
                row += 'X|'
            elif n == finish_point_x and m == finish_point_y:
                row += 'O|'
            else:
                row += ' |'
        
        game_map += row + '\n'
    
    print(game_map)

    game_map = ''

  

    if point_x == finish_point_x and point_y == finish_point_y:
        print(f'You win! Your score: {score}')
        break

    try:
        input_value = input('Input u / d / l / r to move your person: ')
        score += 1
    except KeyboardInterrupt:
        print('Enter "exit" to exit or u / d / l / r to move you person')
        continue

    if input_value == 'exit':
        print('You exit!')
        break

    if input_value == 'u' and point_y > 0:
        point_y -= 1
    elif input_value == 'd' and point_y + 1 < SIZE_M:
        point_y += 1
    elif input_value == 'l' and point_x > 0:
        point_x -= 1
    elif input_value == 'r' and point_x + 1 < SIZE_N:
        point_x += 1


