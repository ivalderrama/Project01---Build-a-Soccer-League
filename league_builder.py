import sys
import csv
from datetime import datetime
from datetime import timedelta

def main():
    # Opening csv file and reading from it
    with open('soccer_players.csv') as csvfile:
        reader = csv.reader(csvfile)
        # reader = csv.DictReader(csvfile)
        new_list = list(reader)

    experienced = []                            # Creating experienced players array
    never_played = []                           # Creating new players array

    sharks = []                                 # Creating team array
    dragons = []                                # Creating team array
    raptors = []                                # Creating team array

    # Assigning date in 10 days time and assigning to a variable
    date_in_10 = datetime.now() + timedelta(days=10)

    # Assigning experienced players into experienced array
    for i in range(1, len(new_list)):
        if new_list[i][2] == 'YES':
            experienced.append(new_list[i])

    # Assigning new players into never_played array
    for i in range(1, len(new_list)):
        if new_list[i][2] == 'NO':
            never_played.append(new_list[i])

    # Evenly distributing experienced and new players into teams
    sharks.extend(experienced[0:3])
    sharks.extend(never_played[0:3])

    dragons.extend(experienced[3:6])
    dragons.extend(never_played[3:6])

    raptors.extend(experienced[6:])
    raptors.extend(never_played[6:])

    # Removing the height value from the sharks array
    for i in range(len(sharks)):
        del sharks[i][1]

    # Removing the height value from the dragons array
    for i in range(len(dragons)):
        del dragons[i][1]

    # Removing the height value from the raptors array
    for i in range(len(raptors)):
        del raptors[i][1]

    # Open teams.txt file (or create if non-existent), and write to file
    with open('teams.txt', 'w') as file:

        file.write("Sharks\n")                          # Writing team title
        for line in sharks:                             # iterating through team array
            line = str(line)                            # converting each line to a string
            for char in "''[]":                         # within the line, looking for characters ''[]
                line = line.replace(char, '')           # replacing the the found characters with space
            file.write(line + '\n')                     # writing each stripped line on a new line
        file.write("\n")                                # new line to space out the heading

        file.write("Dragons\n")                         # Writing team title
        for line in dragons:                            # iterating through team array
            line = str(line)                            # converting each line to a string
            for char in "''[]":                         # within the line, looking for characters ''[]
                line = line.replace(char, '')           # replacing the the found characters with space
            file.write(line + '\n')                     # writing each stripped line on a new line
        file.write("\n")                                # new line to space out the heading

        file.write("Raptors\n")                         # Writing team title
        for line in raptors:                            # iterating through team array
            line = str(line)                            # converting each line to a string
            for char in "''[]":                         # within the line, looking for characters ''[]
                line = line.replace(char, '')           # replacing the the found characters with space
            file.write(line + '\n')                     # writing each stripped line on a new line
        file.write("\n")                                # new line to space out the heading

    for i in range(0, len(sharks)):                     # Iterating through the team array
        name = str(sharks[i][0])                        # getting name from array and assigning to variable
        guardian = str(sharks[i][2])                    # getting guardian names and assigning to variable
        lower_name = name.lower().replace(" ", "_")     # lowercasing name and replacing space with '_'
        with open(lower_name+'.txt', 'w') as file:      # creating a file from lowercased name, and opening writing message
            file.write("""Dear {},                      
            
Your child, {}, is in the Sharks team.
The date and time of his/her practice is on {}.
            
Coach """.format(guardian, name, date_in_10))

    for i in range(0, len(dragons)):                    # Iterating through the team array
        name = str(dragons[i][0])                       # getting name from array and assigning to variable
        guardian = str(dragons[i][2])                   # getting guardian names and assigning to variable
        lower_name = name.lower().replace(" ", "_")     # lowercasing name and replacing space with '_'
        with open(lower_name + '.txt', 'w') as file:    # creating a file from lowercased name, and opening writing message
            file.write("""Dear {},

Your child, {}, is in the Dragons team.
The date and time of his/her practice is on {}.

Coach """.format(guardian, name, date_in_10))

    for i in range(0, len(raptors)):                    # Iterating through the team array
        name = str(raptors[i][0])                       # getting name from array and assigning to variable
        guardian = str(raptors[i][2])                   # getting guardian names and assigning to variable
        lower_name = name.lower().replace(" ", "_")     # lowercasing name and replacing space with '_'
        with open(lower_name + '.txt', 'w') as file:    # creating a file from lowercased name, and opening writing message
            file.write("""Dear {},

Your child, {}, is in the Raptors team.
The date and time of his/her practice is on {}.

Coach """.format(guardian, name, date_in_10))


if __name__ == "__main__":
    main()                                              # Calling the main function

