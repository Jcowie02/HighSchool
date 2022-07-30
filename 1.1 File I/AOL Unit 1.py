import random

'''
#######################################################
####################---Functions---####################
#######################################################
'''

'''
this function displays the board. see comments/code below for details
'''


def display(wordsearch, size):
    for row in range(0, size):  # goes through each row
        line = ""  # create space (visual)
        for col in range(0, size):  # goes through each column in each row
            line = line + wordsearch[row][col] + " "  # makes sure everything is spaced out evenly
            # and each new letter in the list is added onto the variable
        print(line)  # prints each row after the column values have been assigned to each spot

'''
this def checks each row and column to see if there is a blank space, and if so, it replaces it with a random letter.
see comments below for details
'''


def fillRandom(wordsearch, size):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(0, size):
        for col in range(0, size):  # these 'for' loops ensure each column in each row is checked
            if wordsearch[row][col] == "_":
                randletter = random.choice(alph)  # chooses a random letter from variable 'alph'
                wordsearch[row][col] = randletter  # replaces the blank space with a random letter
'''
this def adds words to the main list 'wordsearch'. it chooses randomly whether to insert it vertically, horizontally,
backwards or forwards. one major problem I faced was finding a way to make sure the correct number of words go into
the corresponding difficulty, which is what the flag variable is for.
'''


def addWord(word, wordsearch, size, used, usedwords):
    rand = random.randint(0, 1)
    rand2 = random.randint(0, 1)  # had to create another random variable to put it in either fwd or bwd
    flag = False  # flag variable that sees if a word has fit in the wordsearch
    way = 0  # var for choosing backwards or forwards
    x = 0  # var that keeps track if the word will fit in the wordsearch and no overlap any other words
    if rand == 0:  # vert or horizontal is random, this one is horizontal
        row = random.randint(0, (size-1))  # chooses a random row to insert the word into
        col = 0
        for i in range(0, len(word)):
            if wordsearch[row][col + i] == "_":
                x += 1
        # runs through this loop for however long the word is, and if the word occupies only blank spaces, then the
                #  condition below happens
                if x == len(word):
                    usedwords.append(word)
                    used += 1
                    flag = True
                    # changes values of variable to be used in main code
                    if rand2 == 0: # chooses randomly to insert the words backwards or forwards
                        for i in range(0, len(word)):
                            wordsearch[row][col + i] = word[i]  # the wordsearch at a specific row and column is being
                            # replaced with the word at the same position as the subsequent column
                            # (inserted horizontally)

                    else:
                        for i in range(len(word) - 1, -1, -1):  # syntax for inserting the word backwards
                            wordsearch[row][col + way] = word[i]
                            way += 1  # variable to make the column position to move in the opposite direction as the
                            # word so it is inserted backwards

    else: # inserted vertically; this code is the same as above, only the i variable is added to the row, not the column
        row = 0
        col = random.randint(0, (size-1))
        for i in range(0, len(word)):
            if wordsearch[row + i][col] == "_":
                x += 1
                if x == len(word):
                    usedwords.append(word)
                    used += 1
                    flag = True

                    if rand2 == 0:
                        for i in range(0, len(word)):
                            wordsearch[row + i][col] = word[i]
                    else:
                        for i in range(len(word) - 1, -1, -1):
                            wordsearch[row + way][col] = word[i]
                            way += 1
    return used, flag, usedwords


'''
#######################################################
####################---Main Code---####################
#######################################################
'''

con = 0
timescompleted = 0
# these variables only need to be set equal to zero once
while con == 0:  # allows the user to play again if they want to
    print("\nYou have completed Wordsearch", timescompleted, "times")
    wordsearch = []
    usedwords = []  # this variable ensures that only the words in the wordsearch can be guessed, not the ones from the
                    # rest of the file
    used = 0
    # resets these variables if played again
    while True:  # defensive coding
        d = str(input("\nWelcome to WordSearch!\n\nPlease choose a difficulty:\nEasy(e)\nMedium(m)\nHard(h)\n").lower())
        if d == 'e' or d == 'h' or d == 'm':  # depending on the difficulty, this condition sets important variables
            # to the correct values
            if d == 'e':
                size = 7
                numofwords = 5
            elif d == 'm':
                size = 9
                numofwords = 10
            else:
                size = 12
                numofwords = 15


            # code below creates the game board, depending on the difficulty
            for row in range(0, size):
                wordsearch.append([])
                for column in range(0, size):
                    wordsearch[row].append("_")

            word = [i.strip().split() for i in open("test.txt").readlines()]  # turns the file of words into a list
            random.shuffle(word)  # randomizes the words every time the user plays
            i = 0
            while used < numofwords:  # runs this until the correct number of words is put into the specific grid
                used, flag, usedwords = addWord(word[i][0], wordsearch, size, used, usedwords)
                if flag:  # flag variable that determines if the word found an open position
                    i += 1 # if that is the case, the definition moves on to the next word

            fillRandom(wordsearch, size)
            display(wordsearch, size)
            # after the grid has been filled with random words and displayed, it breaks the loop
            break
    count = 0
    guessed = []
    while used > count:  # runs the loop until all words are guessed
        userinput = input("\nPlease input a word that you find: ").upper()  # guess need to be uppercase
        if userinput in usedwords and userinput not in guessed:
            # ensures the user hasn't guessed the same word twice, and only the specific words in the list can be
            # guessed
            guessed.append(userinput)
            count += 1
            print("Congrats! That's right!\nYou have", (numofwords-count), "words left")
        else:
            print("Try again")
    # breaks loop once everything has been guessed
    print("Good job! You got everything")
    timescompleted += 1
    while True:  # for defensive coding
        again = input("\nInput 'a' if you want to play again, input 's' if you want to stop playing, or input 'w' "
                      "if you want to wipe save data\n")
        if again == 'a':  # breaks this loop, but the main loop continues
            break
        elif again == 's':
            print("Thank you for playing word search")
            con += 1  # breaks the main loop
            break
        elif again == 'w':
            timescompleted = 0
            print("Scores were reset")
        else:
            print("Not valid input!")
