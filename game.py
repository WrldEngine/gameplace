import pygame

newGame=True
loggedIn=False
miniGame=False

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
greyBackground =(203, 206, 203)


width=65
height=65
radius=30

margin=0

xDistanceFromEdge=220

pygame.init()

gameBoard=[[None]*8]*8

windowSize= [960, 640]
screen = pygame.display.set_mode(windowSize)

pygame.display.set_caption("Draughts Game")

done = False

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            column = (pos[0]-xDistanceFromEdge) // (width+margin)
            row = pos[1] // (height+margin)


    screen.fill(greyBackground)

    def boardGui(black,white):
        for boardRow in range(8):
            for boardColumn in range(8):
                xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
                yCoordinate=(margin+height) * boardRow + margin
                if boardRow%2==0 and boardColumn%2==0:
                    currentColour = black
                if boardRow%2!=0 and boardColumn%2==0:
                    currentColour = white
                if boardRow%2==0 and boardColumn%2!=0:
                    currentColour = white
                if boardRow%2!=0 and boardColumn%2!=0:
                    currentColour = black
                pygame.draw.rect(screen,currentColour,[xCoordinate,yCoordinate, width, height])

    def piecesGameBoard(gameBoard):
        if newGame==True:
            newGameBoard(gameBoard)

    def newGameBoard(gameBoard):
        for x in range(8):
            for y in range(3):
                if ((x%2!=0) and (y%2==0)) or ((x%2==0) and (y%2!=0)):
                    gameBoard[x][y]="NormalBlack"

            for y in range(5,8):
                if ((x%2==0) and (y%2==0)) or ((x%2!=0) and (y%2!=0)):
                    gameBoard[x][y]="NormalRed"
        print(gameBoard)

        drawPieces(gameBoard,black,red)

    def drawPieces(gameBoard,black,red):
        for x in range(8):
            for y in range(8):
                xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
                yCoordinate=(margin+height) * y + margin+33
                if gameBoard[x][y]=="NormalBlack":
                    pygame.draw.circle(screen,black,(xCoordinate,yCoordinate),radius)

                if gameBoard[x][y]=="kingBlack":
                    pygame.draw.circle(screen,black,(xCoordinate,yCoordinate),radius)
                if gameBoard[x][y]=="NormalRed":
                    pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)

                if gameBoard[x][y]=="KingRed":
                    pygame.draw.circle(screen,red,(xCoordinate,yCoordinate),radius)

    boardGui(black,white)
    piecesGameBoard(gameBoard)

    clock.tick(60)

    pygame.display.flip()

pygame.quit()