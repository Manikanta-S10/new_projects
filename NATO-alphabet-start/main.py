import pandas 

data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(data_dict)

user_input = input('Enter the name which do you want to find words for each letter: ').upper()
out = [ data_dict[letter] for letter in user_input if letter in data_dict]
print(out)