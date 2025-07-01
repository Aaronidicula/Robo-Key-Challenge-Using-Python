# RoboKey Challenge game. A small Game. Created by Aaron Idicula
guess_the_secret_key = ""
guess_count = 0
guess_limit = 6
loop_break = False
Passkey = 1234
secret_key_reset = False
Secret_Key_Store = { "giraffe":1234, "tiger":1234, "lion":1234, "cat":1234, "horse":1234, "city":2346 } #Key-Dictionary
for sk in Secret_Key_Store:                                                                             #Looping through the dictionary
    secret_key_reset = False
    while guess_the_secret_key != sk and guess_count != guess_limit and secret_key_reset == False:      #Checking the security key input
        guess_the_secret_key=input("Guess the secret key: ")
        print(f"your secret key was:{sk}")
        guess_count += 1
        secret_key_reset = True
    if guess_the_secret_key == sk:
        print("You Won!")
        loop_break = True # log the value
        break
    if guess_count == guess_limit:
        print("Out of Guesses!  You Lose!")
    else:
        print(f"You have {guess_limit - guess_count} guesses remaining!")                              #Alert
if loop_break == True:
    print(f"Your corresponding passcode is {Secret_Key_Store[sk]}")
    if Secret_Key_Store[sk] == Passkey:
        print("You have succesfully unlocked the door as the value to the passcode is matched!")
    else:
        print("Even though you have guessed the correct secret key the corresponding value to open the door is not matched! So the door remains locked!")
else:
    print("Sorry! Try Next time!")
