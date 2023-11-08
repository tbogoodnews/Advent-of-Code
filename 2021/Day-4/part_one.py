txt_file = open("input.txt", "r") # Open file

txt = txt_file.read() # read to list

txt_file.close()

boards = txt.split("\n\n") #split txt
nums = [int (i) for i in boards[0].split(",")] # Grab first elem and cast to ints
boards = boards[1:] # Remove numbers called
boards = [ [[int(y) for y in x.split(" ") if y!=""] for x in j.split("\n")] for j in boards] 

boards[-1].pop() # Remove hanging whitespace

called_num = 0
board_dimension = 5

winning = [None] * board_dimension # basis for a winning board

def check_board(board):
    # Check horizontals
    if winning in board:
        return True
    # Check verticals
    transpose = list(map(list, zip(*board))) 
    if winning in transpose:
        return True
    return False

def update_board(board, num):
    return [[None if y==num else y for y in row] for row in board]



while True:
    boards = [update_board(i, nums[called_num]) for i in boards]
    checked =  [check_board(x) for x in boards]
    if True in checked:
        print("Winning called number: ", nums[called_num])
        winning_board = boards[checked.index(True)]
        sum_win_board = sum([sum(filter(None, row)) for row in winning_board])
        print("Sum of winning board: ", sum_win_board)
        print("Product is: ", nums[called_num]*sum_win_board)
        break
    called_num+=1
