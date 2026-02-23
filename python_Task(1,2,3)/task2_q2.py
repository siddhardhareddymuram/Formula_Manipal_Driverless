n=int(input("Enter the number of elements in the list: "))
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)

hash_table=[[] for i in range(10)]
for num in nums:
    index=num%10
    hash_table[index].append(num)
print("Hash Table is: ")
for i in range(10):
    print(f"Index {i}: {hash_table[i]}")
