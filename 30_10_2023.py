list=[1]
fi=1
li=list.len-1
print("Before modifying,")
for i in list:
    print(i)
curr=0
for i in range(1,3):
    curr=list[fi-i]
    curr=curr-1
    list.insert(fi-i,curr)
    fi+=1
for i in range(1,3):
    curr=list[li-i]
    curr=curr-1
    list.insert(fi-i,curr)
    fi+=1
print("After modifying,")
for i in list:
    print(i) 
