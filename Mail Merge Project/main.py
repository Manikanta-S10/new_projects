# Reading the invited_named.txt file and converting it into list of names 
with open('Input/Names/invited_names.txt') as names_file:
    names_list = names_file.readlines()

# Reading Starting_letter and replace the name and create a new file with contents
with open('Input\Letters\starting_letter.txt') as starting_letter:
    letter = starting_letter.read()
    for name in names_list:
        stripped_name = name.strip()
        replace_letter = letter.replace('[name]',stripped_name)
        with open(f'Output\ReadyToSend\{stripped_name}.txt',mode='w') as completed_letter:
            completed_letter.write(replace_letter)











    



