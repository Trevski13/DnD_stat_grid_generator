#Imports
from random import randint
import os

#Print the grid to console
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

#Output grid to file
def output_grid(grid):
    if os.path.isfile("grid.txt"):
        os.remove("grid.txt")
    for row in grid:
        print(' '.join(row), file=open("grid.txt", "a"))

def keep_highest(num1, num2, num3, num4):
    rolls = [num1, num2, num3, num4]
    sorted(rolls, key=int, reverse=True)
    total = 0
    for i in range(3):
        total += rolls[i]
    return total

#Creating the empty gird
stat_grid = []

#Grabbing the grid size
grid_cols = int(input('How many colums would you like?: '))
grid_rows = int(input('How many rows would you like?: '))

#Setting the row to default for test
#row = "10" * gird_cols

#Setting stat_grid to default for test
#for i in range(gird_rows):
#    stat_grid.append(row)

#Displaying choices for stat_grid creation
print('How would you like to make your stat grid?')
print('     1 - 3d6')
print('     2 - 2d6+6')
print('     3 - 4d6 keep highest 3')
print('     4 - 4d6 keep highest 3 re-roll 1s')
print('     5 - 3d8')
print('     6 - Stat Range')

#Prompt for choice
choice = int(input('Please enter choice (1 - 6): '))

while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
    choice = int(input('Please enter a vaid option (1 - 6): '))
else:
    choice_text_output = ''
    
    if choice == 1:
        choice_text_output = '3d6'
    elif choice == 2:
        choice_text_output = '2d6+6'
    elif choice == 3:
        choice_text_output = '4d6 keep highest 3'
    elif choice == 4:
        choice_text_output = '4d6 keep highest 3 re-roll 1s'
    elif choice == 5:
        choice_text_output = '3d8'
    elif choice == 6:
        choice_text_output = 'Stat Range'
        stat_range_start = int(input('Please enter lowest stat value in the range: '))
        stat_range_end = int(input('Please enter highest stat value in the range: '))

    print()
    print('Your choice is option ' + choice_text_output)
    print()

#Set the rolls to and empty list and the roll total to zero
dice_rolls = []
dice_roll_total = 0

#If statments that handle grid creation method
if choice == 1:
    for rows in range(grid_rows):
        for cols in range(grid_cols):
            dice_roll_total = randint(1, 6) + randint(1, 6) + randint(1, 6)
            if dice_roll_total < 10:
                dice_rolls.append('0' + str(dice_roll_total))
            else:
                dice_rolls.append(str(dice_roll_total))
        stat_grid.append(dice_rolls)
        dice_rolls = []
    print_grid(stat_grid)
elif choice == 2:
    for rows in range(grid_rows):
        for cols in range(grid_cols):
            dice_roll_total = randint(1, 6) + randint(1, 6) + 6
            if dice_roll_total < 10:
                dice_rolls.append('0' + str(dice_roll_total))
            else:
                dice_rolls.append(str(dice_roll_total))
        stat_grid.append(dice_rolls)
        dice_rolls = []
    print_grid(stat_grid)
elif choice == 3:
    for rows in range(grid_rows):
        for cols in range(grid_cols):
            dice_roll_total = keep_highest(randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
            if dice_roll_total < 10:
                dice_rolls.append('0' + str(dice_roll_total))
            else:
                dice_rolls.append(str(dice_roll_total))
        stat_grid.append(dice_rolls)
        dice_rolls = []
    print_grid(stat_grid)
elif choice == 4:
    for rows in range(grid_rows):
        for cols in range(grid_cols):
            roll1 = randint(1, 6)
            roll2 = randint(1, 6)
            roll3 = randint(1, 6)
            roll4 = randint(1, 6)
            no_ones = False
            while no_ones == False:
                if roll1 == 1:
                    roll1 = randint(1, 6)
                elif roll2 == 1:
                    roll2 = randint(1, 6)
                elif roll3 == 1:
                    roll3 = randint(1, 6)
                elif roll4 == 1:
                    roll4 = randint(1, 6)
                else:
                    no_ones = True
            dice_roll_total = keep_highest(roll1, roll2, roll3, roll4)
            if dice_roll_total < 10:
                dice_rolls.append('0' + str(dice_roll_total))
            else:
                dice_rolls.append(str(dice_roll_total))
        stat_grid.append(dice_rolls)
        dice_rolls = []
    print_grid(stat_grid)
elif choice == 5:
    for rows in range(grid_rows):
        for cols in range(grid_cols):
            dice_roll_total = randint(1, 8) + randint(1, 8) + randint(1, 8)
            if dice_roll_total < 10:
                dice_rolls.append('0' + str(dice_roll_total))
            else:
                dice_rolls.append(str(dice_roll_total))
        stat_grid.append(dice_rolls)
        dice_rolls = []
    print_grid(stat_grid)
elif choice == 6:
    for rows in range(grid_rows):
        for cols in range(grid_cols):
            dice_roll_total = randint(stat_range_start, stat_range_end)
            if dice_roll_total < 10:
                dice_rolls.append('0' + str(dice_roll_total))
            else:
                dice_rolls.append(str(dice_roll_total))
        stat_grid.append(dice_rolls)
        dice_rolls = []
    print_grid(stat_grid)

#Prompt for export
print()
export = input('Would you like to export the grid? (y/n): ')

while export.lower() != 'y' and export.lower() != 'n':
    export = input('Please enter a vaid option (y/n): ')
else:
    if export.lower() == 'y':
        print()
        print('Exporting grid to current directory...')
        output_grid(stat_grid)
    elif export.lower() == 'n':
        print()
        print('Well fuck you too')

#Exit program
exit = input('Press any key to exit')
