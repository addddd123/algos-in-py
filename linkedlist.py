class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.start=None
    def insertfirst(self,value):
        newnode=node(value)
        if self.start==None:
            self.start=newnode
            
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
        

    def display(self):
        print("\n")
        tem=self.start
        while tem.next!=None:
           print(tem.data,end=" ") 
           
           tem=tem.next
        print(tem.data,end=" ") 
    def deletefirst(self):
        print("\ndeleted first el see below \n")
        temp=self.start
        temp=temp.next
        self.start=temp
    def delete_last(self):
        
        print("\ndeleted last see last \n")
        temp=self.start
        while temp.next.next!=None:
            temp=temp.next
            
        temp.next=None
    def addatbegning(self,get_data):
        a=node(get_data)
        temp=self.start
        a.next=temp
        self.start=a
    def reverse(self):
        temp=self.start
        prev=None
        while temp.next!=None:
            n=temp.next
            temp.next=prev
            prev=temp
            temp=n #
        self.start=prev
        
    def insertatpostion(self,data,positon):
        temp=self.start
        k=0
        positon-=1
        while k!=positon:
            temp=temp.next
            print("kk ",k)
            
            k+=1
       
        save=temp.next
        obj=node(data)
        temp.next=obj
        
        obj.next=save

ll=linklist()

for i in range(10):
        ll.insertfirst(i)
ll.display()
ll.deletefirst()
ll.display()
ll.delete_last()
ll.display()

ll.addatbegning(1000)
ll.display()
ll.reverse()
print("\n\n afteer reverse ")
ll.display()
ll.insertatpostion("9999",3)
ll.display()
