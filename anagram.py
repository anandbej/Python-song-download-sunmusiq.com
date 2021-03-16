str1="hello"
str2="hell"
l1 = list(str1);
l2 = list(str2);
x=0;

for i in range(len(l1)):
    if l1[i] not in l2:
        x=x+1


for j in range(len(l2)):
    if l2[j] not in l1:
        x=x+1

print str1
print str2
print x
