import pandas

f = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in f.iterrows()}
print(phonetic_dict)


#Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        new_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("sorry, only letters in the alphabet please")
        generate_phonetic() #goes back to ask user
    else:
        print(new_list)

generate_phonetic()