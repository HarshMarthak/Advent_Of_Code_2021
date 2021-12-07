with open("dataday4.txt") as f:
	checked=[int(x) for x in f.readline().strip("\n").split(',')]
	boards = []


	while f.readline():
		board=[]
		for i in range(5):
			board.extend([int(x) for x in f.readline().strip('\n').split(' ')if x != ''])
		boards.append(board)


def Completed(board):
	count=0
	for i in range(5):
		if board[count] + board[count+1] + board[count+2] + board[count+3] + board[count+4] ==-5:
			return True
		count+=5

	count=0
	for i in range(5):
		if board[count] + board[count+5] + board[count+10] + board[count+15] + board[count+20] ==-5:
			return True
		count+=1
	return False


done = False
while done==False:
	number=checked[0]
	checked=checked[1:]
	for board in boards:
		for i in range(len(board)):
			if board[i]==number:
				board[i]=-1
	for board in boards:
		if Completed(board):
			total=sum([x for x in board if x !=-1])
			print("Solution 1 : ", total*number)
			done = True

done = False
while done==False:
	number=checked[0]
	checked=checked[1:]
	for board in boards:
		for i in range(len(board)):
			if board[i]==number:
				board[i]=-1
	no = 0
	while no < len(boards):
		if Completed(boards[no]):
			if len(boards) > 1:
				boards.pop(no)

			else:
				done=True
				print(boards[no])
				break
		else:
			no+=1
total=sum([x for x in boards[no] if x !=-1])
print("Solution 2 : ", total*number)
