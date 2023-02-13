import random
matrix=["1","2","3",
        "4","5","6",
        "7","8","9"]
#image for matrix modding
im_matrix="""
1 2 3
4 5 6
7 8 9
"""
#sum(matrix1,matrix2)
class data():
    def __init__(self,matrix):
        
        for lines in matrix:
            self.line=lines
        return self.line

def make_matrix():
    """helps you make matrix's, here's how:
    You have two options:
        -1:A random matrix-> the program will generate for you a random matrix for you to work with,
        -2:A personalized matrix-> You give the program a specific matrix that it'll work with.
    """
    lines=[]
    choice=input("\nDo you want:\n1-A random matrix\n2-A personalized matrix\n>>")
    if choice=="1":
        column_size=random.randint(1,5)
        line_size=random.randint(1,5)
        i,p=0,0
        line=[]
        matrix=[]
        while i!=column_size:
            while p!=line_size:
                line.append(random.randint(0,9))
                p+=1
            matrix.append(line)
            line=[]
            p=0
            i+=1
    elif choice=="2":
        n_m=(input("What's the size of the matrix?\nEx: n*m   n and m are integers!\nn-->number of lines\nm-->number of columns\n>>")).split("*")
        try:
            for item in n_m:
                1/int(item)
        except:
            print("Your input is formated incorrectly!\n\nn*m   n and m are integers!\nn-->number of lines\nm-->number of columns\n")
            quit()
        for item in n_m:
            if len(n_m)!=2: 
                print("Your input is formated incorrectly!\n\nREMEMBER:\nn*m   n and m are integers!\nn-->number of lines\nm-->number of columns\n")
                quit()
        column_size=n_m[0]
        line_size=n_m[1]
    return matrix
#to sum matrixs
def sum(matrix1,matrix2):
    if len(matrix1)!=len(matrix2):
        print("The size(line x column) of the matrix's are not the same!")
        quit()
#column_size,line_size=matrix_size()

matrix=make_matrix()
numbers=data(matrix)
print(self.line)
print(matrix)
for line in matrix:
    print(line,type(matrix),type(line),(type(line[0])))
    for item in line:
        print(item)
