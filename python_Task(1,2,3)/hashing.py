


n=int(input("Enter the number of values: "))
print("Enter the values: ")
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
hash_table2=[[] for i in range(5)]
for i in range(n):
    index=arr[i]%5
    hash_table2[index].append(arr[i])
for i in range(5):
    print(f"arr{i} : {hash_table2[i]}")

for i in range(5):
    if 22 in hash_table2[i]:
        print(f"It is at Index: {i}")
        break
    else:
        print("22 is Not found in the Hash Table")
    if 22 in hash_table2[i]:
        hash_table2.remove(hash_table2[i])
        print(f"arr{i} : {hash_table2[i]}")
        break

index2=32%5
hash_table2[index2].append(32)
for i in range(5):
    print(f"arr{i} : {hash_table2[i]}")


