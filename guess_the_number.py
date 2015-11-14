import simplegui
import random
#secret_number = 0
num_range = 100
max_guesses = 7

def new_game():
    global secret_number, guesses
    guesses = 0
    secret_number = random.randrange(0, num_range)
    print
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", max_guesses
    
def range100():
    global num_range, max_guesses
    num_range = 100
    max_guesses = 7
    new_game()

def range1000():
    global num_range, max_guesses
    num_range = 1000
    max_guesses = 10
    new_game()
    
def input_guess(guess):
    guess = int(guess)
    global guesses
    
    print
    print "Guess was", guess
    guesses += 1
    print "Number of remaining guesses is", max_guesses - guesses
    
    if secret_number < guess:
        print "Lower"
        if guesses == max_guesses:
            print "You ran out of guesses. The number was", secret_number
            new_game()
    elif secret_number > guess:
        print "Higher"
        if guesses == max_guesses:
            print "You ran out of guesses. The number was", secret_number
            new_game()
    else:
        print "Correct. You won!"
        new_game()
    
frame = simplegui.create_frame("Guess the number", 200, 200)
inp = frame.add_input("Enter the number:", input_guess, 100)
game_100 = frame.add_button("Range is [0,100)", range100)
game_1000 = frame.add_button("Range is [0,1000)", range1000)

new_game()

