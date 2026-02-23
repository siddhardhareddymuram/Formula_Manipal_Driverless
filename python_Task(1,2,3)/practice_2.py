arr1=[]
r=int(input("Enter the number of rows: "))
c=int(input("Enter the number of columns: "))
for i in range(r):
    row=[]
    for j in range(c):
        x=int(input())
        row.append(x)
    arr1.append(row)
def rotate(arr1):
    for i in range(r):
        for j in range(c):
            arr1[i][j],arr1[j][i]=arr1[j][i],arr1[i][j]
    for i in range(r):
        arr1[i].reverse()
for row in arr1:
    print(row)

rotate(arr1)