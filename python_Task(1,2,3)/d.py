n=int(input('enter the number of elements: '))
print("Enter the elements: ")
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)
hash_table=[[] for i in range(10)]
for i in range(n):
    index=nums[i]%10
    hash_table[index].append(nums[i])
for i in range(10):
    print(f"hash{i} : {hash_table[i]}")
count=[0 for i in range(10)]
for i in range(10):
    for num in hash_table[i]:
        count[i]=count[i]+1
    
for i in range(10):
    print(f"Index{i} has {count[i]} elements")
    
