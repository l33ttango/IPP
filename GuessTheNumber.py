# Guess the Number
# input will come from buttons and an input field
# Should be played in codeskulptor
# http://www.codeskulptor.org/#user40_vnwAQVbIGY_2.py

import simplegui, random
guesses_left = 7
secret_number = 50
is_1000 = False

# helper function to start and restart the game
def new_game():
    global guesses_left, secret_number
    if is_1000:
        guesses_left = 10
        secret_number = random.randrange(0, 1000)
        print "New game. Range is from 0 to 1000. \nNumber of guesses remaining is 10"
    else:
        guesses_left = 7
        secret_number = random.randrange(0, 100)
        print "New game. Range is from 0 to 100. \nNumber of guesses remaining is 7. \n"


# define event handlers for control panel
def range100():
    global is_1000
    is_1000 = False
    new_game()

def range1000():
    global guesses_left, is_1000
    is_1000 = True
    new_game()
    
    
def input_guess(guess):
    global guesses_left
    print "Guess was", guess
    if int(guess) == secret_number:
        print "Correct! \n"
        new_game()
    elif guesses_left - 1 == 0:   
        print "You lose! The correct answer is %s. \n" %secret_number
        new_game()
    elif int(guess) < secret_number:
        guesses_left += -1 
        print "You have %s guesses left." % guesses_left
        print "Higher! \n"
    else:         
        guesses_left += -1        
        print "You have %s guesses left." % guesses_left
        print "Lower! \n"
        
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 300)
frame.add_input("Your guess:", input_guess, 50)
frame.add_button("Range is [0, 100)", range100, 125)
frame.add_button("Range is [0, 1000)", range1000, 125)

# register event handlers for control elements and start frame


# call new_game
new_game()
