from itertools import groupby 
import re

f1= open('access.log' , 'r')

d=set() 
for line in f1.readlines(): 
    result = re.findall(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]' , line)
    d.update(result) 



dop=[]
for item in d:
    result = re.search(r'[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.[1-2]?[0-9]?[0-9]\.', item)
    dop.append(result.group(0))

Groups = {}
for k,v in zip(dop, d):
    Groups.setdefault(k, []).append(v)

for Group in Groups:
    print()
    print(Group)
    for ip in Groups[Group]:
        print(ip)
