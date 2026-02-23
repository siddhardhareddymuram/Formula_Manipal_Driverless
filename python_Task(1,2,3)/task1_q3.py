from task1_q2 import q2

class q3(q2):
    def __init__(self, arr, key):
        super().__init__(arr)  
        self.key = key

    def binary_search(self):
        low = 0
        high = len(self.arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.arr[mid] == self.key:
                return mid
            elif self.arr[mid] > self.key:
                high = mid - 1
            else:
                low = mid + 1

        return -1




n = int(input("Enter number of strings: "))
lst = []

for i in range(n):
    s = input("Enter string: ")
    lst.append(s)

key = input("Enter string to search: ")

obj = q3(lst, key)

obj.selection_sort()
print("Sorted List:", obj.arr)


result = obj.binary_search()

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")