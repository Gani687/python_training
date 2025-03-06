str = "Hello world and Hello Earth" 
#print frequency of each words
c=str.split()
dict={}
for i in c:
    cou=0
    
    for j in c:
        if i==j:
            cou+=1
            
    if i not in dict:
        dict[i] = cou
            

print(dict)
