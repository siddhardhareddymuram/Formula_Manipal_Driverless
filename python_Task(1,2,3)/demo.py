def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                arr[min],arr[j]=arr[j],arr[min]
nums=[5,6,9,1,2]
selection_sort(nums)
print(nums)

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

bubble_sort(nums)
print(nums)

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        while j>0 and arr[i]<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]
insertion_sort(nums)
print(nums)
