import os
dictionary = {
    "hello" : "In Finnish it's hei. Typically used when greeting.",
    "car" : "In Finnish it's auto. A type of automotive vehicle.",
    "flower" : "In Finnish it's kukka. A type of common plant.",
    "computer" : "In Finnish it's tietokone",
    "fan" : "In Finnish it's tuuletin. A type of appliance that blows air."
}
print("""Welcome to the Dictionary Application DA2019
by VilleSupi
Please type in the word you're looking for.
Please, don't use capital letters.""")
Word = input()
if Word in dictionary:
    print(Word + " is listed in the dictionary. " + dictionary[Word])
    print("You can now press q to close the program.")
    if input() == 'q': os._exit(0)

if Word not in dictionary:
    print(Word + """ is not listed in the dictionary.
Would you like to add it to the dictionary?
Please make sure you didn't use capital letters, before adding
any more words into the dictionary.
Enter y for yes or close the program by pressing any key""")
if input() == 'y': print("""Please give the Finnish translation
of the given word as well as the definition of it.
It will be added to the dictionary.""")
else: os._exit(0)
Translation = input()
print("""Are you sure? Press y to save it to the dictionary.
Press any other key to cancel and close the program.""")
if input() == 'y': dictionary[Word] = "In Finnish it's " + Translation 
else: os._exit(0)