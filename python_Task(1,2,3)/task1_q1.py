n = int(input("Enter number of strings: "))

strings = []

for i in range(n):
    s = input(f"Enter string {i+1}: ")
    strings.append(s)

freq = {}

for i in strings:
    for j in i:
        if j.isalpha():
            j = j.lower()
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1

print(freq)
