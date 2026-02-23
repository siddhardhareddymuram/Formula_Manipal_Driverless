arr1=[]
arr2=[]
product=[]

r1=int(input("Enter the number of rows in matrix-A: "))
c1=int(input("Enter the number of columns in matrix-A: "))

for i in range(r1):
    row=[]
    for j in range(c1):
        x=int(input())
        row.append(x)
    arr1.append(row)

r2=int(input("Enter the number of rows in matrix-B: "))
c2=int(input("Enter the number of columns in matrix-B: "))

for i in range(r2):
    row=[]
    for j in range(c2):
        x=int(input())
        row.append(x)
    arr2.append(row)

def matrix_multiplication(arr1,arr2):

    if c1!=r2:
        print("Matrix Multiplication is NOT Possible !!!")
        return
    
    for i in range(r1):
        row=[0]*c2
        product.append(row)
   

    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                product[i][j]+=arr1[i][k] * arr2[k][j]

    print("Multiplied Matrix is:")
    for row in product:
        print(row)

matrix_multiplication(arr1,arr2)
