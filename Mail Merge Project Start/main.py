#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open('Input/Names/invited_names.txt', mode='r') as names:
    names = names.readlines()
    print(names)


with open('Input/Letters/starting_letter.txt', mode='r') as letter:
    letter = letter.read()
    for name in names:
        stripped_name = name.strip('\n')
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f'Output/ReadyToSend/letter+for_{stripped_name}.txt', mode='w') as final:
            final.write(new_letter)




