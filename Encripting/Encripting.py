import random
import string
k=random.randint(1,5)
separator=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=k))
print(separator)

test="QWERTTATQW"

#test=test.replace("A",separator)

print(test)
#COUNT THE AMOUNT OF DIFFERENT LETTERS
diff=""
for thing in test:
    if thing not in diff:
        diff+=thing
amount=len(diff)
#SEPARATE ALL THE LETTERS
letter_sub={}
for letter in diff:
    new=''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5))
    letter_sub[letter]=new
print(letter_sub)
new_test=""
for letter in test:
    new_test+=letter_sub[letter]
    print(letter)

print(new_test)
"""

new=""
all=["TQ","QWERt","WW","Q"]


for letter in diff:
    sub=str(random.choices(all))
    test=test.replace(letter,sub)
    print(letter)
print(test)
#UNITE EVERYTHING!
"""