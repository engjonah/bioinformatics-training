import random
class Board:
	def __init__(self):
		self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]
	def show(self):
		string_board = "current board:\n---------------\n  0 1 2\n"
		counter = 0
		for row in self.board:
			string_board+= str(counter) + " "
			counter+=1
			for col in row:
				string_board+=col + " "
			string_board+="\n"
		print(string_board)
	def full(self):
		for row in self.board:
			for col in row:
				if col=="-":
					return False
		return True
	def placement(self, marker, x, y):
		if self.board[x][y]=='-':
			self.board[x][y] = marker


def playRound(marker, board):
	if marker=="X":
		human_turn(marker, board)
		bot_turn(marker, board)
	else:
		bot_turn(marker, board)
		human_turn(marker, board)

def human_turn(marker, board):
	if not checkWinner(board)[0] and board.full():
		return
	if checkWinner(board)[0]:
		return
	#Human going
	board.show()
	x_placement = input("please pick a row: ")
	y_placement = input("please pick a column: ")
	if int(x_placement)>2 or int(y_placement)>2 or int(x_placement)<0 or int(y_placement)<0:
		print("location is not on board. please pick again.")
		playRound(marker, board)
		return
	elif board.board!="-":
		board.placement(marker, int(x_placement), int(y_placement))
	else:
		print("Please enter the position of an empty location")
		playRound(marker, board)
		return
	board.show()

def bot_turn(marker, board):
	if checkWinner(board)[0]:
		return
	if not checkWinner(board)[0] and board.full():
		return
	print ("computer is going...\n")
	#Bot going
	if marker=="X":
		bot_marker="O"
	elif marker=="O":
		bot_marker="X"
	#potential locations
	locations = []
	for x in range(3):
		for y in range(3):
			if board.board[x][y]=="-":
				locations.append([x,y])
	chosen_location = locations[random.randrange(0,len(locations))]
	board.placement(bot_marker, chosen_location[0], chosen_location[1])

#returns if winner exists and winner's marker
def checkWinner(board):
	#Check horizontal
	for x in range (3):
		if board.board[x][0]!="-" and board.board[x][0]==board.board[x][1]==board.board[x][2]:
			return [True, board.board[x][0]]
	#Check Vertical
	for x in range (3):
		if board.board[0][x]!="-" and board.board[0][x]==board.board[1][x]==board.board[2][x]:
			return [True, board.board[0][x]]
	#Check Diagonal
	if (board.board[0][0]!="-" and board.board[0][0]==board.board[1][1]==board.board[2][2]):
		return [True, board.board[0][0]]
	if (board.board[0][2]!="-" and board.board[0][2]==board.board[1][1]==board.board[2][0]):
		return [True, board.board[0][2]]
	
	return [False, '-']

def play():
	print("Welcome to Tic-Tac-Toe!")
	board = Board()
	marker = "-"
	markers = ["x","X","o","O"]
	while marker not in markers:
		marker = input("Please choose a marker X or O: ")
		if (marker not in markers):
			print("Error: Marker input not correct.")
	marker = marker.upper()
	print("marker is " + marker)
	winner = False
	round_counter=1
	while winner == False and not board.full():
		print("---------\n-Round " + str(round_counter) + "-\n---------")
		playRound(marker, board)
		winner_info = checkWinner(board)
		winner = winner_info[0]
		round_counter+=1
	if not winner and board.full():
		print("Stalemate!")
		return
	print("winner is: " + winner_info[1])


#if __name__ == "__main__":
#	play()
play()
