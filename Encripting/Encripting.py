import random
import string

#quote

quote="A tua nota é ~15"

#COUNT THE AMOUNT OF DIFFERENT LETTERS

diff=""
for thing in quote:
    if thing not in diff:
        diff+=thing
amount=len(diff)

#See all the diferent letters

letter_sub={}
for letter in diff:
    new=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))
    letter_sub[letter]=new


#Change the letters

new_quote=""
for letter in quote:
    new_quote+=letter_sub[letter]

#Creating the encripted text:
encripted=""
encripted+=new_quote

#add the items to the key.txt

#with open(input("What file do u want to put the doc_keys?\n>>"), "w") as file:
with open("/home/guimbreon/Desktop/Git_organazier/Tests/Encripting/key.txt", "w") as file:
    
    for letter in letter_sub:
        file.write(f">{letter}\n{letter_sub[letter]}\n")


print(f"\n{encripted}\n")