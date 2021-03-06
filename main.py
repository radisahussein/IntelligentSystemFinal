import pygame
from surakarta.constants import WIDTH,HEIGHT,SQUARE_SIZE,RED, WHITE, W_BCKGRND, H_BCKGRND, BOARD_POS
from surakarta.game import Game
from minimax.minimax_algorithm import minimax,minimax1,randomMove,alphabeta
import time

# push

FPS = 60

WIN = pygame.display.set_mode((W_BCKGRND,H_BCKGRND))
pygame.display.set_caption('Surakarta Board Game')
# background_image = pygame.image.load("image/surakarta_board.jpg").convert()

def get_row_col_from_mouse(pos):
    x, y = pos
    # row = (y ) // (SQUARE_SIZE) 
    # col = (x ) // (SQUARE_SIZE) 
    row = (y - 200) // (SQUARE_SIZE) 
    col = (x - 200) // (SQUARE_SIZE) 
    print(row,col)
    return row, col

def simulate():

    totalGames = 0
    red_win = 0
    white_win = 0
    gameList = []

    for i in range(50):

        run = True
        clock = pygame.time.Clock()
        game = Game(WIN)
        move_red = 0
        move_white = 0

        print("==================================")
        print("Games Played: " + str(totalGames))
        print("Red Won: " + str(red_win))
        print("White Won: " + str(white_win))
        print("==================================")

        #record time
        start = time.time()

        while run:

            clock.tick(FPS)

            if game.winner() != None:

                end = time.time()

                totalGames += 1

                if game.winner() == RED:
                    red_win += 1
                
                else:
                    white_win += 1
                
                print('Time Taken: ' + str(end-start))
                gameList.append([game.winner(), (end-start), move_red])

                run = False

            if (game.turn == WHITE):
                value, new_board = minimax(game.get_board(), 2, WHITE, game)
                game.ai_move(new_board)
                move_white += 1
            
                print("Move White Counter: " + str(move_white))
            

            elif game.turn == RED:

                value, new_board = randomMove(game.get_board(),RED,game)
                game.ai_move(new_board)

                move_red += 1

                print("Move Red Counter: " + str(move_red))

            

            game.update()
    
    
    print("Games Played: " + str(totalGames))
    print("Red Won: " + str(red_win))
    print("White Won: " + str(white_win))
    print(gameList)
    pygame.quit()
        

def randoms():

    totalGames = 0
    red_win = 0
    white_win = 0
    gameList = []

    for i in range(20):

        run = True
        clock = pygame.time.Clock()
        game = Game(WIN)
        move_red = 0
        move_white = 0

        print("==================================")
        print("Games Played: " + str(totalGames))
        print("Red Won: " + str(red_win))
        print("White Won: " + str(white_win))
        print("==================================")

        #record time
        start = time.time()

        while run:

            clock.tick(FPS)

            if game.winner() != None:

                end = time.time()

                totalGames += 1

                if game.winner() == RED:
                    red_win += 1
                
                else:
                    white_win += 1
                
                print('Time Taken: ' + str(end-start))
                gameList.append([str(game.winner()), (end-start), move_red])

                run = False

            if (game.turn == WHITE):
                value, new_board = randomMove(game.get_board(),WHITE,game)
                game.ai_move(new_board)
                move_white += 1
            
                print("Move White Counter: " + str(move_white))
            

            elif game.turn == RED:

                value, new_board = randomMove(game.get_board(),RED,game)
                game.ai_move(new_board)

                move_red += 1

                print("Move Red Counter: " + str(move_red))

            

            game.update()
    
    
    print("Games Played: " + str(totalGames))
    print("Red Won: " + str(red_win))
    print("White Won: " + str(white_win))
    print(gameList)
    pygame.quit()   

def alphasim():

    totalGames = 0
    red_win = 0
    white_win = 0
    gameList = []

    for i in range(20):

        pinf = float('inf')
        ninf = float('-inf')

        run = True
        clock = pygame.time.Clock()
        game = Game(WIN)
        move_red = 0
        move_white = 0

        print("==================================")
        print("Games Played: " + str(totalGames))
        print("Red Won: " + str(red_win))
        print("White Won: " + str(white_win))
        print("==================================")

        #record time
        start = time.time()

        while run:

            clock.tick(FPS)

            if game.winner() != None:

                end = time.time()

                totalGames += 1

                if game.winner() == RED:
                    red_win += 1
                
                else:
                    white_win += 1
                
                print('Time Taken: ' + str(end-start))
                gameList.append([str(game.winner()), (end-start), move_red])

                run = False

            if (game.turn == WHITE):
                value, new_board = randomMove(game.get_board(),WHITE,game)
                game.ai_move(new_board)
                move_white += 1
            
                print("Move White Counter: " + str(move_white))
            

            elif game.turn == RED:

                value, new_board = alphabeta(game.get_board(),2,ninf,pinf, RED, game)
                game.ai_move(new_board)

                move_red += 1

                print("Move Red Counter: " + str(move_red))

            

            game.update()
    
    
    print("Games Played: " + str(totalGames))
    print("Red Won: " + str(red_win))
    print("White Won: " + str(white_win))
    print(gameList)
    pygame.quit()   

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        # WIN.blit(background_image, [0, 0])

        # pygame.display.flip()
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 2, WHITE, game)
            game.ai_move(new_board)


        if game.winner() != None:
            print(game.winner())
            run = False



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

# main()


#AI Minimax vs Random
# simulate()

#Random vs Random
# randoms()

#Alpha Beta vs Random
alphasim()