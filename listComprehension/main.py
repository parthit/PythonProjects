import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in df.iterrows()}

user_input = input('Enter the word to be converted NATO mnemonic: ').upper()

ans = [dict[letter] for letter in user_input]

print(ans)




