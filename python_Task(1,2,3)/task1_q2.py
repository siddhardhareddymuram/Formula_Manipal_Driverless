class q2:
    def __init__(self, arr):
        self.arr = arr

    def selection_sort(self):
        n = len(self.arr)

        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

       
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

        return self.arr




n = int(input("Enter number of strings: "))
lst = []

for i in range(n):
    s = input("Enter string: ")
    lst.append(s)

obj = q2(lst)
sorted_list = obj.selection_sort()

print("Sorted List:", sorted_list)