import random 

score = 0 #to keep score your points
failed_attempt = 0 #counts and stores any inputs other than "2","4","6" and "8"
num = eval(input('Specify Your matrics size: ')) #to specify the game board (input 3 to get a 3x3
                                                 # matrics or 4 to get a 4x4 matrics.....)

##################################################################################################

game = [] #my game board
for i in range(num):
    game.append([0]*num) #creats a multi-list of my game board
    
game[random.randint(0,num-1)][random.randint(0,num-1)] = 2 #chooses one position in my multi list(in my game board)
                                                           #and changes its value to 2(this only happens at the start of the game
game[random.randint(0,num-1)][random.randint(0,num-1)] = 2 #chooses one position in my multi list(in my game board)
                                                           #and changes its value to 2(this only happens at the start of the game


####################################################################################################

#this function makes my game board(multi list) reverse. like a matrics.
################################################################################################## 
def reverse(game):
    new=[]
    for i in range(len(game)):
        new.append([])
        for j in range(len(game[0])):
            new[i].append(game[i][len(game[0])-j-1])
    return new

#this function makes my game board(multi list) transpose. like a matrics.
def transpose(game):
    Transpose=[]
    for i in range(len(game[0])):
        Transpose.append([])
        for j in range(len(game)):
            Transpose[i].append(game[j][i])
    return Transpose

##########################################################################################
#left
def left(game):
    global score 
    for single_line in game:
        i=0
        j=1
        while j<len(single_line) and i < len(single_line):
            if single_line[i]==0 and single_line[j]==0:
                j+=1
            elif single_line[i]!=0 and single_line[j]==0:
               j+=1
            elif single_line[i]==0 and single_line[j]!=0:
                single_line[i],single_line[j]=single_line[j],single_line[i]
            elif single_line[i]!=0 and single_line[i]==single_line[j]:
                score += single_line[i]**2
                single_line[i]*=2
                single_line[j]=0
                i+=1
                j+=1
            elif single_line[i]!=0 and single_line[i]!=single_line[j]:
                single_line[i+1],single_line[j]=single_line[j],single_line[i+1]
                i+=1
                j+=1
    return game

#right
def right(game):
    return reverse(left(reverse(game)))
#up
def up(game):
    return transpose(left(transpose(game)))
#down
def down(game):
    return transpose(right(transpose(game)))

#################################################################################################

while True: #this makes it execute forever
    
    # a function to display my multi-list(game)
    
    def show():
        for b in game:
            print (b)
        return game
    show()
    go = game

    #this a fucnction that copys and stores my game board(I will use this later for game over and random
    #generation of number)
    def show_go():
        for j in go:
            print (j)
        return go
    #takes inputs for movement
    movement_choice = input("Make your move: 8 for up, 2 for down, 4 for left and 6 for right ")
    if movement_choice == "8":
        game = up(game)
    elif movement_choice == "2":
        game = down(game)
    elif movement_choice == "4":
        game = left(game)
    elif movement_choice == "6":
        game = right(game)
    else:
        failed_attempt +=   1
        continue

    #for choosing random postition (that is zero) and to change that value to 2 or 4
    #stores all the 0s in my game board in a list of rows and columns
    
    row = []
    column = []
    for i in range(0,num):
        for j in range(0,num):
            if game[i][j] == 0:
                row.append(i)
                column.append(j)
            if game[i][j] == 2048:
                print('Congrats!')
                
    # For randomly generating 2 or 4 if and only if a move is made and if that move is avilable
    
    if (movement_choice == "2" and go != down(game)):
        print ('Your Score is:', score)
        if len(row) > 1: 
            random_index = row.index(random.choice(row))
            row_to_place = row[random_index]
            column_to_place = column[random_index]
            fout = [2,2,2,2,2,2,2,2,4,4]
            x = random.choice(fout)
            game[row_to_place][column_to_place] = x
    if (movement_choice == "6"):
        print ('Your Score is:', score)
        if len(row) > 1: 
            random_index = row.index(random.choice(row))
            row_to_place = row[random_index]
            column_to_place = column[random_index]
            fout = [2,2,2,2,2,2,2,2,4,4]
            x = random.choice(fout)
            game[row_to_place][column_to_place] = x
    if (movement_choice == "4"):
        print ('Your Score is:', score)
        if len(row) > 1: 
            random_index = row.index(random.choice(row))
            row_to_place = row[random_index]
            column_to_place = column[random_index]
            fout = [2,2,2,2,2,2,2,2,4,4]
            x = random.choice(fout)
            game[row_to_place][column_to_place] = x
    if (movement_choice == "8" and go != up(game)):
        print ('Your Score is:', score)
        if len(row) > 1: 
            random_index = row.index(random.choice(row))
            row_to_place = row[random_index]
            column_to_place = column[random_index]
            fout = [2,2,2,2,2,2,2,2,4,4]
            x = random.choice(fout)
            game[row_to_place][column_to_place] = x
    if len(row) == 1:
        print ('Your Score is:', score)
        
        row_to_place = row[0]
        column_to_place = column[0]
        fout = [2,2,2,2,2,2,2,2,4,4]
        x = random.choice(fout)
        game[row_to_place][column_to_place] = x

    #The game over condition
        
    if len(row) == 0:
        if game != right(go) or game != left(go)or game != up(go)or game != down(go):
            print('Please be cautious and choose your next move carefully')
            continue
        else:
            break
print ("Total Score:",str(score))
print ("Game Over")
    
