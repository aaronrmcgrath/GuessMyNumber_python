### GuessMyNumberGame 19.09.09 ARM



### dependencies
import random, sys



### vars

## global vars
play = ''
playerName = ''
totalGuesses = 0
bPlay = False
bPlayerGuessed = False
playerGuess = 0
bComputerGuessed = False
computerGuess = 0

iLowNumber = 1
iHighNumber = 100
iGameCount = 0

bCanAdvance = False
bContinue = False
bExit = False



### functions/methods


## utility methods

# closes the app in the terminal
def end() :
    response = playerInterface(['\n\n    Thanks for playing, please come play again soon.\n', '\n    Press enter to exit.\n'])
    print('\n\nGoodbye! :D\n')
    sys.exit()

# formats string array for display and prints to terminal
def stringFormater(strArray) :
    sMsg = ''
    for s in strArray :
        sMsg = sMsg + s
    print(sMsg)

# built in interface that displays a message to user and returns input
# (at anytime this is called and 'exit' is entered it will close the app)
def playerInterface(text) :
    res = ''
    stringFormater(text)
    res = input()
    if stringCompare(res, ['exit']) :
        end()
    return res

# compares a string against multiple values, returns 'True' if any are match or 'False' if none match
def stringCompare(str, strArray) :
    bMatch = False
    for s in strArray:
        if str.lower() == s.lower() :
            return True
    return bMatch


## program/game methods

# verifies the user wants to play, captures name, gives friendly welcome, displays tips, helpful text, and rules
def displayIntro() :
    global bPlay
    global playerName
    global play
    play = playerInterface(['\n\n    Do you think you can guess my number? (y to play)\n'])
    while bPlay == False:
        if stringCompare(play, ['y', 'yes']) :
            playerName = playerInterface('\n    Great! What is your Name?\n')
            bPlay = True
        else :
            play = playerInterface('\n    Just let me know when you want to play. (y to play)')

    print('\n    Hello, {0}!\n\n'.format(playerName))
    # TODO: print welcome message, tips, and rules here!

# starts a new game and resets global vars
# to be used before a new game starts
def startGame() :
    global number
    number = random.randint(1,100)
    global bPlay
    bPlay = False
    global play
    play = ''
    global bPlayerGuessed
    bPlayerGuessed = False
    global totalGuesses
    totalGuesses = 0
    global iLowNumber
    iLowNumber = 1
    global iHighNumber
    iHighNumber = 100
    global bCanAdvance
    bCanAdvance = False
    global bContinue
    bContinue = False
    ## print(number)

#starts a new game where the user sets the numbers (Low Number & High Number)
def startGameWithPlayerNumbers(iLow, iHigh) :
    startGame()
    global iLowNumber
    iLowNumber = iLow
    global iHighNumber
    iHighNumber = iHigh

# ends a game by reseting a few vars and
# checks to see if the player wants to replay, continue to next game or exit app
def endGame() :
    global iGameCount
    iGameCount = 0
    global totalGuesses
    totalGuesses = 0
    playerToContinue()

# replays current game by resetting game specific global vars to continue fresh
def replay() :
    global bPlayerGuessed
    bPlayerGuessed = False
    global bComputerGuessed
    bComputerGuessed = False
    global bCanAdvance
    bCanAdvance = False
    global bContinue
    bContinue = False
    global bExit
    bExit = False

# presents player with choice to replay, continue, or end/exit app
def playerToContinue() :
    global play
    global bExit
    global iGameCount
    play = playerInterface(['\n    Would you like to continue or end your run?','(r to replay, c to continue, or e for end)\n'])
    if stringCompare(play, ['c','cont', 'continue']) :
        bContinue = True
        iGameCount = 0
    elif stringCompare(play, ['r', 'replay', 'retry', 'redo']) :
        stringFormater(['\n    Okay, let\'s play again!'])
        replay()
    elif stringCompare(play, ['e', 'end', 'exit', 'esc', 'escape']) :
        bExit = True
        play = ''
    if bExit == True :
        end()


## games

# Game One:
# player guesses the computers random number between 1 and 100
def gameOne() :
    global iGameCount
    global playerName
    global totalGuesses
    if totalGuesses == 0 :
        startGame()
        if iGameCount > 0:
            stringFormater(['    Well, ', playerName, ' let\'s get started. Go ahead and guess my number. It\'s between 1 and 100.'])
    global playerGuess
    playerGuess = playerInterface([''])
    global bPlayerGuessed
    try:
        playerGuess = int(playerGuess)
        totalGuesses = totalGuesses + 1
    except Exception as e:
        stringFormater(['\n    That\'s not a number, please enter again!'])
        playerGuess = 0
    if playerGuess < number :
        print('\n    Too low! Try again.\n')
    elif playerGuess > number :
        print('\n    That\'s too high! Guess again.\n')
    elif playerGuess == number :
        bPlayerGuessed = True
    if bPlayerGuessed :
        play = ''
        global bCanAdvance
        bCanAdvance = True
        print('\n        * * *        * * *        * * *        \n')
        stringFormater(['\n    Great job, ', playerName, '!\n', '    You got it in ', str(totalGuesses), ' tries!\n\n'])
        endGame()

# Game Two:
# computer guesses players number between 1 and 100
def gameTwo() :
    global bCanAdvance
    global iGameCount
    global playerName
    global computerGuess
    global bComputerGuessed
    global number
    global iLowNumber
    global iHighNumber
    global play

    #stringFormater(['iGameCount: ', str(iGameCount)])
    #stringFormater(['iLowNumber: ', str(iLowNumber)])
    #stringFormater(['iHighNumber: ', str(iHighNumber)])

    if iGameCount == 0 :
        startGame()
    else :
        number = number = random.randint(iLowNumber,iHighNumber)

    play = playerInterface(['\n\n    Is it ', str(number), '?\n', '\n    If it\'s not your number please tell me if I need to guess higher (h) or lower (l).','\n    If it is my number tell me so! (press y)'])
    if stringCompare(play, ['y', 'yes', 'yep', 'yup', 'yea', 'yeah', 'yessir', 'correct']) :
        bComputerGuessed = True
    elif stringCompare(play, ['l', 'low', 'lower']) :
        iHighNumber = number - 1
    elif stringCompare(play, ['h', 'high', 'higher']) :
        iLowNumber = number + 1
    else :
        print('\n\n    Darn... you\'re really not going to give me any clue!? That doesn\'t seem fair.\n')

    iGameCount = iGameCount + 1
    computerGuess = iGameCount

    if bComputerGuessed :
        play = ''
        bCanAdvance = True
        print('\n        * * *        * * *        * * *        \n')
        if computerGuess < 8 :
            stringFormater(['\n\n    You thought you could make it hard for me? Not this time!'])
        else :
            stringFormater(['\n\n    Great job, you had me stumped!\n'])
        iGameCount = 0
        iHighNumber = 100
        iLowNumber = 0
        endGame()

# runs the games in order, to be called once at beginning of app
def runGames() :
    global bCanAdvance
    global bContinue
    global bPlayerGuessed
    global bComputerGuessed
    stringFormater(['    Well, let\'s get started. Go ahead and guess my number. It\'s between 1 and 100.'])
    ## print(number)
    while bCanAdvance == False and bContinue == False :
        gameOne()

    bCanAdvance = False
    bContinue = False

    stringFormater(['\n\n                  *  *  *                  \n','\n    That\'s great news, this time you pick a number between 1 and 100.'])
    print('\n\n    Please think of a number, then hit enter when you\'re ready.')
    response = input()
    while bCanAdvance == False and bContinue == False :
        gameTwo()

# runs the methods/modules of the app
def run() :
    global bPlay
    # start text
    print('\n\n\n    ***    ***    ***    ***    ***    ***    \n\n')
    print('               GUESS MY NUMBER')
    print('\n\n    ***    ***    ***    ***    ***    ***    ')
    displayIntro()
    if bPlay :
        runGames()
    end()


### PLAY GAME HERE ###
run()
