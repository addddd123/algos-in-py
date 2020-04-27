import random
start=int(input("input start "))
stop=int(input(" input stop"))
limit=int(input("input limit"))
lis= [random.randint(start, stop) for iter in range(limit)] 
print("random genrated list is ",lis)
temp=0
temp1=0
j=0
track=0
count=0
while(j<len(lis)):
    print("counted",count)
    count+=1
    for i in range(len(lis)-1):
        if lis[i+1]<lis[i]:
            temp=lis[i]
            temp1=lis[i+1]
            lis[i+1]=temp
            lis[i]=temp1
            track+=1
    if track==0:
        j=len(lis)
    track=0
    i=0
    j+=1  
    
print("sorted list is ",lis)


