import random
player1_steps = 0
player1_row = 2
player1_col = 1
dice_number = 0
player2_steps = 0
player2_row = 2
player2_col = 1
win = False
def player_position(player_steps):
    if player_steps == 8 or player_steps == 0:
        return 2,1
    if player_steps == 1:
        return 3,1
    if player_steps == 2:
        return 3,2
    if player_steps == 3:
        return 3,3
    if player_steps == 4:
        return 2,3
    if player_steps == 5:
        return 1,3
    if player_steps == 6:
        return 1,2
    if player_steps == 7:
        return 1,1
#player1_row,player1_col=player_position(0)
#print(player1_row,player1_col)
def roll_dice():
    dice = [1, 2, 3]
    dic_num = random.choice(dice)
    return dic_num
def print_board(player1_row, player1_col, player2_row, player2_col):
    for i in range(1,4):
        for j in range(1,4):

            if(i==j==2):
                print("End",end="  ")
            elif(i==player1_row==player2_row and j==player1_col==player2_col):
                print("1-2", end="  ")
            elif(i==player1_row and j==player1_col):
                print("1--",end="  ")
            elif(i==player2_row and j==player2_col):
                print("--2",end="  ")
            else:
                print("---", end="  ")

        print("\n")
print_board(player1_row, player1_col, player2_row, player2_col)
while win != True:
    #player one movement
    input_val_1=True
    input_val_2=True
    if win!= True:
        while input_val_1 == True:
            confirm = input("You are the player1, type r/R to roll the dice :\n")
            if(confirm == "r" or confirm == "R"):
                dice_number = roll_dice()
                print("The dice number is : " , dice_number)
                player1_steps+=dice_number
                print("The step of player1 is :",player1_steps)
                if(player1_steps == 8):
                    win =True
                    print_board(player1_row, player1_col, player2_row, player2_col)
                    print("Game Over,Player1 is the winner")
                    break
                elif(player1_steps == player2_steps):
                    player2_steps = 0
                    print("The current player2 steps is",player2_steps)
                elif(player1_steps > 8 ):
                    player1_steps-=dice_number
                    print("It is not a valid step, we roll back the player1 steps to: ", player1_steps)
                input_val_1 = False
            else:
                print("Please enter a valid word")
            if win == True:
                break
        player1_row, player1_col = player_position(player1_steps)
        player2_row, player2_col = player_position(player2_steps)
        print_board(player1_row,player1_col,player2_row,player2_col)


    #player two movement
    if win != True:
        while input_val_2 == True:
            confirm = input("You are the player2, type r/R to roll the dice :\n")
            if(confirm == "r" or confirm == "R"):
                dice_number = roll_dice()
                print("The dice number is : " , dice_number)
                player2_steps+=dice_number
                print("The step of player2 is :",player2_steps)
                if(player2_steps == 8):
                    win =True
                    print_board(player1_row, player1_col, player2_row, player2_col)
                    print("Game Over,Player2 is the winner")
                    break
                elif(player2_steps == player1_steps):
                    player1_steps = 0
                    print("The current player1 steps is",player1_steps)
                elif(player2_steps > 8 ):
                    player2_steps-=dice_number
                    print("It is not a valid step, we roll back the player2 steps to: ",player2_steps)
                input_val_2 = False
            else:
                print("Please enter a valid word")
            if win == True:
                break
        player1_row, player1_col = player_position(player1_steps)
        player2_row, player2_col = player_position(player2_steps)
        print_board(player1_row,player1_col,player2_row,player2_col)
    else:
        pass

