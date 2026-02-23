data=[]
with open("things.csv","r") as f:
    for line in f:
        data.append(line)
count=0
for thing in data:
    count=count+1
print("No of Things Listed in the CSV file is:",count)

