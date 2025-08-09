#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder OUTPUT

with open("day-24-files/Mail-Merge/Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("day-24-files/Mail-Merge/Input/Letters/starting_letter.txt") as f:
    letter = f.read()

for name in names:
    x = letter.replace("[name]", name.strip())
    with open(f"day-24-files/Mail-Merge/Output/letter_to_{name}.txt", "a") as f:
        f.write(x)
