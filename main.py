def showinstructions():
    print('\n')  # outputs blank and instructions heading for readability
    print('--------------------------------')
    print('----------INSTRUCTIONS----------')
    print('--------------------------------')
    print(
        "To move rooms type the word move and the direction you would like to go ----Example: Move North")  # outputs basic instructions
    print('The First Letter in the Directional word and the first letter of an item must be CAPITALIZED')
    print('Pickup every crumb of food from each room and add it to your mouse bag before the cat catches you')
    print('If you collect all the items and the cat never gets to the same room as you, you win the game')
    print('If the cat reaches the same room as you, you lose.', '\n')
    print('Beware... Invalid input or Moves you cannot make result in the cat moving regardless if you move')
    print('When you pickup an item, the cat hears you and makes a move again')
    print('Have Fun... Be Smart... Be sneaky!!!', '\n')
    print("To exit the game type exit\n")  # outputs instructions for exiting game


def showstatus(current_room, cats_room):
    print(
        '--------------------------------!!!!!-------------------------------------')  # prints the following three lines for heading and readability
    print('-------------STATUS-------------!!!!!----------------ROOMS----------------')
    print('--------------------------------!!!!!-------------------------------------', '\n')
    print('You are in the ' + current_room)  # prints the room the user is currently in
    print('The cat is in the ', cats_room, '\n')

    print('                                --------------------------------------------')
    print('                                -- Dining Room --------------- Kitchen -----')
    print('                                --------------------------------------------')
    print('                  -----------------------------------------Spare Bedroom 1 -')
    print('                  -- Hiding Room - Living Room -----------------------------')
    print('                  ----------------------------------------------------------')
    print('                                ------------------------------Game Room-----')
    print('                                --------------------------------------------')
    print('                                -- Master Bedroom ---------Spare Bedroom 2--')
    print('                                --------------------------------------------')
    print('\n')


def main():
    rooms = {  # this is the dictionary that the game uses to validate moves and the room it allows the user to be in
        'Hiding Room': {'East': 'Living Room'},
        'Living Room': {'North': 'Dining Room', 'South': 'Master Bedroom', 'West': 'Hiding Room', 'East': 'Game Room',
                        'Item': 'Cheese'},
        'Dining Room': {'East': 'Kitchen', 'South': 'Living Room', 'Item': 'Ham'},
        'Kitchen': {'West': 'Dining Room', 'South': 'Spare Bedroom 1', 'Item': 'Cookie'},
        'Spare Bedroom 1': {'North': 'Kitchen', 'South': 'Game Room', 'Item': 'Bread'},
        'Game Room': {'North': 'Spare Bedroom 1', 'South': 'Spare Bedroom 2', 'West': 'Living Room', 'Item': 'Candy'},
        'Spare Bedroom 2': {'North': 'Game Room', 'West': 'Master Bedroom', 'Item': 'Popcorn'},
        'Master Bedroom': {'North': 'Living Room', 'East': 'Spare Bedroom 2', 'Item': 'Chip', 'Villain': 'Cat'}
    }

    import random

    current_room = 'Hiding Room'  # this starts the user in the Great Hall, the user must start th e game in a room
    cats_room = 'Master Bedroom'
    items_in_inventory = []

    showinstructions()  # calls function that displays the instruction one time

    # loop forever until the exit command is given
    while True:

        showstatus(current_room, cats_room)
        if 'Villain' in rooms[
            current_room]:  # If the last move by the player lands them in the same room as the cat, game over
            print('Oh No! The Cat caught you!')
            print('Better luck next time!')
            break
        print('Directions you can move and its room:', rooms[current_room],
              '\n')  # Shows user what moves are available in the room they are currently in
        print('Items you have picked up into your inventory: ', items_in_inventory)
        if 'Item' in rooms[current_room]:
            print('The item in this room needs to be picked up', '\n')

        print("What would you like to do: ", end=' ')
        move = input('>')  # Gets input from user
        print('\n\n\n')  # Adds three blank lines to improve readability during program execution
        move = move.split()  # splits the string into two strings so that the following code can execute properly

        del rooms[cats_room]['Villain']  # Removes the cat from its current location

        # following is the only way I could change the cats location without completely disrupting the dictionary
        num1 = random.randint(1, 8)  # gets a random number
        if (num1 == 1):
            cats_room = 'Living Room'
        elif (num1 == 2):
            cats_room = 'Dining Room'
        elif (num1 == 3):
            cats_room = 'Kitchen'
        elif (num1 == 4):
            cats_room = 'Spare Bedroom 1'
        elif (num1 == 5):
            cats_room = 'Game Room'
        elif (num1 == 6):
            cats_room = 'Spare Bedroom 2'
        elif (num1 == 7):
            cats_room = 'Master Bedroom'
        rooms[cats_room]['Villain'] = 'Cat'

        if len(move) > 2 or len(move) < 1:
            # checks to insure the input is at least 1 word but not more than two, if it is not the following two lines execute
            print("Bad Input!",
                  '\n')  # prints this statement when no valid direction is given and exit command is not given
            continue  # goes back to the beginning of the loop

        # if they type 'Move' or 'move' or 'MOVE' first
        if (move[0] == 'move') or (move[0] == 'Move') or (move[0] == 'MOVE'):
            # searches dictionary in th elocation of rooms[current room] for valid location of rooms[current_room][move1]] move[1] being the second word of user input string
            if move[1] in rooms[current_room]:
                # sets the current room to the new room
                current_room = rooms[current_room][move[1]]  # moves player
            # if the input does not match a valid room and the command is not an exit command
            else:
                print('OOPS, you can not go that way!',
                      '\n')  # prints this when the move they select is not valid from the room they are currently in
                continue
        elif (move[0] == 'Pickup') or (move[0] == 'pickup') or (move[0] == 'PICKUP') and (
                'Item' in rooms[current_room]):
            if (current_room == 'Hiding Room'):  # Hiding room is only for hiding, cat cannot enter this room
                print('You can not pickup anything in the hiding room')
                continue
            if (move[1] in rooms[current_room]['Item']):
                print('you picked up:', rooms[current_room]['Item'])
                items_in_inventory.append(rooms[current_room]['Item'])
                del rooms[current_room]['Item']
                if (len(items_in_inventory) == 7):  # this is gameplay exit if all inventory is picked up successfully
                    print(
                        'Congratulations, you successfully picked up all items before the mean kitty could make a meal of you and your snacks!')
                    break
                else:
                    continue
            else:
                print('You made an invalid selection. Careful, the cat is getting closer.')
                continue
        elif (move[0] == 'exit') or (move[0] == 'Exit') or (move[0] == 'EXIT'):
            print("BYE!")
            break
            # exit() # ends loop which exits game
        else:
            print("Invalid move! Be AWARE the cat is getting closer.",
                  '\n')  # Lets the user know they did not enter a valid move
            continue
    print("Thanks for playing!")  # final sta5tement printed before game exits
    exit(0)


if __name__ == '__main__':
    main()  # This is the game executing and calling the main functionlling the main function