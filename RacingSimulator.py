#Aiden Fan #101266368
import pygame
import random
import tkinter
import tkinter.messagebox
Coordinates = {}
numCoordw = [0]*36
numCoordb = [0]*36
squareWidth = 6
squareHeight = 6
squareDimensions = 132
grid = pygame.display.set_mode((squareWidth*squareDimensions+170, (squareHeight*squareDimensions))) 
grid.fill((127, 127, 127))

red = (255, 0, 0)
blue = (0,191,255)
currColour = blue
diceRolls1 = 0
diceRolls2 = 0 
coinFlip = random.randint(1,2) #coin flip determines which player starts, 1 is for white to start and 2 is for black, this order stays consistent through the whole game
player1Turn = 0
player2Turn = 0
currRoundDisplay = 1
turn = 1
playerOnePos = 0
playerTwoPos = 0


#initializing the fonts for different texts		
pygame.init()	    
font = pygame.font.SysFont("verdana", 20)	  
font1 = pygame.font.SysFont("verdana", 15)	  
squares = 35 #number of tiles
ctr=0
toggle = 0 #keep track of of which number to subtract for the next square
pygame.init()
font2 = pygame.font.SysFont("verdana", 15)	  

def msgbox(msg):
    window = tkinter.Tk()
    window.wm_withdraw()
    tkinter.messagebox.showinfo(title="Information", message=msg)
    window.destroy()
    return None

#creating the red and blue grid
for i in range(0, squareHeight): #iterates through each row
	
	for j in range(0, squareWidth): #iterates through each column
		Coordinates[squares] = [i,j] #the i and j values of each square
		pygame.draw.rect(grid, currColour, (i * squareDimensions, j * squareDimensions, squareDimensions, squareDimensions))

		#displaying the tile number
		tileNum = font.render(str(squares),True, (0,0,0))
		grid.blit(tileNum, ((i * squareDimensions)+100,(j*squareDimensions)+5))
		numCoordw[squares] = [(i * squareDimensions)+70,(j*squareDimensions)+30] #exact requirements so that the circle doesn't go past the grid
		numCoordb[squares] = [(i * squareDimensions)+70,(j*squareDimensions)+90] #exact requirements so that the circle doesn't go past the grid
		
		#alternating tile number subtraction per row in one column
		if toggle == 0:
			toggle = 1
		elif toggle == 1:
			toggle = 0

		if toggle%2 == 1 & toggle!=0:
			squares=squares-11+ctr
		elif toggle%2 == 0:
			squares=squares-1-ctr
		pygame.display.update()

		#switches colour back and forth between red and blue
		if currColour == red:
			currColour = blue     
		else:
			currColour = red

	squares=34-i #numbering per column
	ctr+=2 #counter for tile number calculation
	if currColour == red:
		currColour = blue
	else:
		currColour = red


		

#text that displays on window
diceRoll1 = font2.render("Dice 1: ", True , (0,0,0))
grid.blit(diceRoll1, ((squareWidth*squareDimensions)+10,50))
diceRoll2 = font2.render("Dice 2: ", True , (0,0,0))
grid.blit(diceRoll2, ((squareWidth*squareDimensions)+10,70))
current_round = font2.render("Current Round: ", True, (0,0,0))
grid.blit(current_round, ((squareWidth*squareDimensions)+10,10))
coinToss = font2.render("Coin Flip: ", True, (0,0,0))
grid.blit(coinToss, ((squareWidth*squareDimensions)+10,30))

#initial circles that start on square 0
pygame.draw.circle(grid, (255,255,255),(numCoordw[0]),15,15)
pygame.draw.circle(grid, (0,0,0),(numCoordb[0]),15,15)

#rendering and displaying the dice 1 values
diceRolls1 = random.randint(1,6)
pygame.draw.rect(grid,(127,127,127),(862,53,10,35))
diceNum1 = font2.render(str(diceRolls1), True , (0,0,0))
grid.blit(diceNum1, ((squareWidth*squareDimensions)+70,50))
#rendering and displaying the dice 2 values
diceRolls2 = random.randint(1,6)
pygame.draw.rect(grid,(127,127,127),(862,73,10,15))
diceNum2 = font2.render(str(diceRolls2), True , (0,0,0))
grid.blit(diceNum2, ((squareWidth*squareDimensions)+70,70))

pygame.display.update()

if coinFlip == 1: #if the the coin flip is 1, player2turn (black) becomes 1
	player2Turn = 1
else: #otherwise player1turn (white) becomes 1
	player1Turn = 1

#while loop to display everything and loop the game until one player wins
while True:
	#prints the round, dice rolls, and player turn in terminal
	'''print("\n\n\ncurrent round: ",currRoundDisplay)
	print("dice :",diceRolls1)
	print("dice :",diceRolls2)
	print("player1turn: ",player1Turn)
	print("player2turn: ",player2Turn)'''



	#gray rectangle to cover previous dice values
	pygame.draw.rect(grid,(127,127,127),(922,13,20,15))
	round = font2.render(str(currRoundDisplay), True, (0,0,0))
	grid.blit(round,((squareWidth*squareDimensions)+130,10))

	#coin flip to determine who starts, 1 is for player one (white) and 2 is for player two (black)
	playerStart = font2.render(str(coinFlip), True, (0,0,0))
	grid.blit(playerStart,((squareWidth*squareDimensions)+85,30))


	
	pygame.display.update()
	pygame.time.delay(1000)


	
	#updates position
	if player2Turn>player1Turn: #because of the if/else statements on lines 109-112, if the coin flip is 1, player2turn becomes greater than player1turn since it starts at 0, making this statement true
		
		for x in range(0, diceRolls1): #only loops for the amount of times the dice has to move
			
			pygame.time.delay(500)

			playerOnePos += 1 #counter to update white's position until it the loops reaches the amount of times the dice roll was
			player1Turn = 1 #changing player1turn to be greater than player2turn so that the next if statement becomes true and allows black to move right after white does
			player2Turn = 0
			
			#alternating between red and blue to cover the previous circle to make it seem that the white circle goes through squares one by one
			if playerOnePos<=35:
				if playerOnePos%2 == 1:
					pygame.draw.circle(grid, red,(numCoordw[playerOnePos-1]),15,15)
				elif playerOnePos%2 == 0:
					pygame.draw.circle(grid, blue,(numCoordw[playerOnePos-1]),15,15)

			#break the for loop if white is on square 36
			if playerOnePos>35: #exact requirments / boundaries for the grid, meaning players can't go past this point
				#print("white won!") #winner gets printed in terminal
				msgbox("White won!!!")
				break

			else: #otherwise, continue printing circle
				pygame.draw.circle(grid, (255,255,255),(numCoordw[playerOnePos]),15,15)
			#pygame.draw.circle(grid, (0,0,0),(numCoordb[diceRolls2]),15,15)
			pygame.display.update()
			
		#	print("positionw: ",playerOnePos) #position of white circle

		
	elif player1Turn>player2Turn:

		for x in range(0, diceRolls2):

			pygame.time.delay(500)

			playerTwoPos += 1
			player2Turn = 1
			player1Turn = 0

			if playerTwoPos<=35:
				if playerTwoPos%2 == 1:
					pygame.draw.circle(grid, red,(numCoordb[playerTwoPos-1]),15,15)
				elif playerTwoPos%2 == 0:
					pygame.draw.circle(grid, blue,(numCoordb[playerTwoPos-1]),15,15)

			if playerTwoPos>35:
				#print("black won!")
				msgbox("Black won!!!")
				break

			else:
				pygame.draw.circle(grid, (0,0,0),(numCoordb[playerTwoPos]),15,15)
			#pygame.draw.circle(grid, (0,0,0),(numCoordb[diceRolls2]),15,15)
			pygame.display.update()
			
		#	print("positionb: ",playerTwoPos)
	
	

	

	if turn%2==0: #turn starts at 0, every 2 times this statement becomes true 
		
		#changing the dice values after both players go once
		#rendering and displaying the dice 1 values
		diceRolls1 = random.randint(1,6)
		pygame.draw.rect(grid,(127,127,127),(862,53,10,35))
		diceNum1 = font2.render(str(diceRolls1), True , (0,0,0))
		grid.blit(diceNum1, ((squareWidth*squareDimensions)+70,50))
		#dice 2 text & value
		diceRolls2 = random.randint(1,6)
		pygame.draw.rect(grid,(127,127,127),(862,73,10,15))
		diceNum2 = font2.render(str(diceRolls2), True , (0,0,0))
		grid.blit(diceNum2, ((squareWidth*squareDimensions)+70,70))
		
		currRoundDisplay+=1 #the current round being displayed adds one every time both of them goes once

	turn += 1 #turn adds 1 every time one of them goes once

	#if either player reaches the last square, the for loop is broken and then the outer while loop is broken, ending the game
	#since the turns always loop until both players have their turns, if both players end up on the last square, the winner that gets printed in the terminal is whoever got to the last square first
	if playerOnePos>35 or playerTwoPos>35:
		
		break
	
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()	

