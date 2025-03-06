D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

D_union={**D1,**D2}
print(D_union)

D_intersection={}
for i,j in D1.items():
    for a,b in D2.items():
        if i == a:
            D_intersection[i]=j
            
print(D_intersection)

res={}
for key,value in D1.items():
    if key not in D2:
        res[key]=value
print(res)

D_merge={}
for key1,val1 in D1.items():
    for key2,val2 in D2.items():
        if key1==key2:
            D_merge[key1]=val1+val2
            D_merge[key2]=val1+val2
        else:
            D_merge[key1]=val1
            D_merge[key2]=val2
print(D_merge)