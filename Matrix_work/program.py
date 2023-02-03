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
def sum(matrix1,matrix2):
    if len(matrix1)!=len(matrix2):
        print("The size(line x column) of the matrix's are not the same!")
        quit()
#sum(matrix1,matrix2)
def matrix_size():
    n_m=(input("What's the size of the matrix?\nEx: n*m\nn-->number of lines\nm-->number of columns\n>>")).split("*")
    column_size=n_m[0]
    line_size=n_m[1]
    return column_size,line_size
def make_matrix():
    lines=[]
    choice=input("\nDo you want:\n1-A random matrix\n2-A personalized matrix\n>>")
    if choice=="1":
        lines.append(f"{random.randint(0,9)},{random.randint(0,9)},{random.randint(0,9)}")
        x=lines[0].split(",")
        print(x)
    elif choice=="2":
        print("2")

#column_size,line_size=matrix_size()
make_matrix()