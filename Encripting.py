import random
import string

#quote

test="BaTAta"

#COUNT THE AMOUNT OF DIFFERENT LETTERS

diff=""
for thing in test:
    if thing not in diff:
        diff+=thing
amount=len(diff)

#See all the diferent letters

letter_sub={}
for letter in diff:
    new=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))
    letter_sub[letter]=new
print(letter_sub)

#Change the letters

new_test=""
for letter in test:
    new_test+=letter_sub[letter]
print(new_test)


#create the key for out-cript
key=""
#start:
key+=diff
print(key)
#put the encripted quote

key+="~" + new_test
print(key, len(key))

#if the key isnt 26 long it adds stuff
while len(key)<=len(diff)+123:
    place=len(diff)+random.randint(1,len(key)-len(diff))
    key=key[:place]+"~"+key[place:]
print(key,len(key))

#add diff to a doc_key.txt file
identification_number=[]
op=0
with open("/home/guimbreon/Desktop/Git_organazier/Tests/Encripting/doc_key.txt", "w") as file:
    for thing in diff:
        while len(identification_number)!=len(diff):
            number=random.randint(1,123)
            if number not in identification_number:
                identification_number.append(number)
                file.write(f">{thing}\n{random.randint(1,123)}\n")


print(identification_number)
for number in identification_number-:
    print(len(letter_sub),len(diff):
#    key=key[:len(diff)+number]+


"""
testing="0123456789"

testing=testing[:4]+"a"+testing[4:]
print(testing)
"""