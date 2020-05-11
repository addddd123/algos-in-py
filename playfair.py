import random
lis=[]
for i in range(65,300):
    s=chr(random.randint(65,90)) 
    if s in lis:
       pass
    elif s !='J' :  
        lis.append(s)
    if len(lis)==25:
        
        break

    
key_row= [lis[i:i+5] for i in range(0, len(lis), 5)]

A=key_row
flatA = sum(A, [])     # Flattens the 2D list
len0 = len(A[0])
lenall = len(flatA)
key_col = [flatA[i:lenall:len0] for i in range(len0)]
print(key_col,"\n")
print("##\n\n",key_row)
#above flasttenning is done to make row and column checking easy
#no receiving string from user
n=list(map(str,input("enter text \n").upper()))

for i in range(0,len(n)-1):
    
    if n[i]==n[i+1]:
          
        n.insert(i+1,chr(random.randint(65,90)) )
    

if n[len(n)-1]==n[len(n)-2]: #make sure last two chars are not same 
    n.insert(len(n)-1,chr(random.randint(65,90)) )
if len(n)%2!=0: #checking if len of text is odd then add arbitrary char at end two make possible pairs
    n.append(chr(random.randint(65,90)).upper())

print(n)

cipher_text=[]

print("length is ",len(n))
j=0
for i in range(4):
        
    if n[j] in key_col[i] and n[i+1] in key_col[i]:
        

        cipher_text.append(key_col[i][i+1])
        cipher_text.append(key_col[i][i+2])
        j=j+1

    elif n[j] in key_row[i] and n[i+1] in key_row[i]:
            cipher_text.append(key_row[i][i+1])
            cipher_text.append(key_row[i][i+2])
            j=j+1
            
    else:
            print("jjjjj")
    
    
print("text is ",cipher_text)