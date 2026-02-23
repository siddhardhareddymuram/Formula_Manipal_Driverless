n=int(input("Enter the number of elements in the list: "))
nums=[]
for i in range(n):
    x=int(input())
    nums.append(x)

hash_table=[[] for i in range(10)]
def insert_sorted(bucket,value):
    low=0
    high=len(bucket)-1
    while low<=high:
      mid=(low+high)//2
      if bucket[mid] < value:
        low = mid + 1
      else:
        high = mid - 1
    bucket.insert(low,value)

for num in nums:
    index=num%10
    insert_sorted(hash_table[index],num)

print("Hash Table is: ")
for i in range(10):
    print(f"Index {i}: {hash_table[i]}")
nums2=[]

add=int(input("Enter the numbers to be insrted: "))

for i in range(add):
    x=int(input())
    index=x%10
    insert_sorted(hash_table[index],x)
   
    
print("Final Hash table is: ")
for i in range(10):
    print(f"index{i}: {hash_table[i]}")

    