n=int(input("Enter the number of points: "))
x=[]
y=[]
for i in range(n):
    a=int(input(f"Enter the X-Coordinate of Point{i+1}:"))
    x.append(a)
    b=int(input(f"Enter the Y-Coordinate of Point{i+1}:"))
    y.append(b)
ref=[]

ref.append(int(input("Enter X -Coordinate of Reference Point: ")))
ref.append(int(input("Enter Y -Coordinate of Reference Point: ")))
dist=[]
for i in range(n):
    k=((x[i]-ref[0])**2+(y[i]-ref[1])**2)**0.5 
    dist.append(k)
for i in range(1,n):
    key=dist[i]
    keyx=x[i]
    keyy=y[i]
    j=i-1 -
    while j>=0 and key<dist[j]:
        dist[j+1]=dist[j]
        x[j+1]=x[j]
        y[j+1]=y[j]
        j-=1
    dist[j+1]=key
    x[j+1]=keyx
    y[j+1]=keyy
print("Sorted Coordinates based on proximity to Reference Point:")
for i in range(n):
    print((x[i],y[i]))
