meetings=[]
n=int(input())

for i in range (n):
    start,end=map(int,input().split())
    meetings.append((start,end))

meetings.sort(key=lambda x: (x[1], x[0]))

count=0 
time=0
for (start,end) in meetings:
    if start>=time:
        count=count+1
        time=end
print(count)

