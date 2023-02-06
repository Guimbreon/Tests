import random
size=7 #digamos q é len do diff
identification_number=[]


while len(identification_number)!=size:
    number=random.randint(1,123)
    if number not in identification_number:
        identification_number.append(number)
print(identification_number)