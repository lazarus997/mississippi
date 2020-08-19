str = input("Enter a string : ")
count = {}
for x in str :
    if x in count.keys() :
        count[x]+=1
    else :
        count[x]=1
count=sorted(count.items(),key=lambda x:x[1],reverse=True)
for x in count :
    print (x[0],'=',x[1])
    
      
      


    
    
