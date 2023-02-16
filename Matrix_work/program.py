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
class data():
    def lines(self,matrix):
        all_lines=[]
        for lines in matrix:
            all_lines+=lines
        return all_lines
def make_matrix(number_of_matrix):
    choice="1"
    """helps you make matrix's, here's how:
    You have two options:
        -1:A random matrix-> the program will generate for you a random matrix for you to work with,
        -2:A personalized matrix-> You give the program a specific matrix that it'll work with.
    """
    print(f"{number_of_matrix}\n")

    #choice=input("\nDo you want:\n1-A random matrix\n2-A personalized matrix\n>>")
    
    if choice=="1":
        """
        column_size=random.randint(1,5)
        line_size=random.randint(1,5)
        """
        column_size,line_size=8,4
        n_m=[column_size,line_size]
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
    return matrix, n_m
#to sum matrixs
def sum(matrix1,matrix2):
    """Summ of the matrixs

    Args:
        matrix1 (list): The first matrix
        matrix2 (list): The second matrix

    Returns:
        int: The matrix after the Summ operations!
    """
    if len(matrix1)!=len(matrix2):
        print("The size(line x column) of the matrix's are not the same!")
        quit()
    else:
        i=0
        new_matrix=[]
        for numbers in matrix1:
            new_matrix.append(numbers+matrix2[i])
            i+=1
        
        i=0
        matrix=[]
        line=[]
        for item in new_matrix:
            line.append(item)
            i+=1
            if i==n_m[1]:
                matrix.append(line)
                line=[]
                i=0
        print("The sum of the matrixs is the following:")
        for line in matrix:
            print(line)
    return matrix
def sub(matrix1,matrix2):
    """Substraction of matrixs

    Args:
        matrix1 (list): matrix number one
        matrix2 (list): matrix numver two

    Returns:
        list: The new matrix after substractions are made!
    """
    if len(matrix1)!=len(matrix2):
        print("The size(line x column) of the matrix's are not the same!")
        quit()
    else:
        i=0
        new_matrix=[]
        for numbers in matrix1:
            new_matrix.append(numbers-matrix2[i])
            i+=1
        
        i=0
        matrix=[]
        line=[]
        for item in new_matrix:
            line.append(item)
            i+=1
            if i==n_m[1]:
                matrix.append(line)
                line=[]
                i=0
        print("The sum of the matrixs is the following:")
        for line in matrix:
            print(line)
    return matrix
#column_size,line_size=matrix_size()

matrix1,n_m=make_matrix("This is the first matrix!")
numbers1=data()
lines1=numbers1.lines(matrix1)
print(matrix1)
matrix2,n_m=make_matrix("This is the second matrix!")
numbers2=data()
lines2=numbers2.lines(matrix2)
print(matrix2)
main_choice=input("What operation do you want to do?\n1-Sum\n2-Substration\n>>")
if main_choice=="1":
    sum_of_matrix=sum(lines1,lines2)
elif main_choice=="2":
    sub_of_matriz=sub(lines1,lines2)
    """
for line in matrix:
    print(line,type(matrix),type(line),(type(line[0])))
    for item in line:
        print(item)
"""