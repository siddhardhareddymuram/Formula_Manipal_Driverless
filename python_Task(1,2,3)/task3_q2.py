data=[]

with open("name.csv","r") as f:
    for line in f:
        num,name=line.strip().split(",")
        data.append([int(num),name])

n=len(data)

for i in range(n):
    for j in range(0,n-i-1):
        if data[j][0] > data[j+1][0]:
            data[j],data[j+1] = data[j+1],data[j]

with open("name.csv","w") as f:
    for record in data:
        f.write(str(record[0]) + "," + record[1] + "\n")
new_data=[]
for i in range(n):
    if i%2!=0:
        new_data.append(data[i])

with open("name.csv","w") as f:
    for record in new_data:
        f.write(str(record[0])+" "+record[1]+"\n")



