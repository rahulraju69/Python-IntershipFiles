'''
ordered dict is one of the obj in collection which allows you to store elements in the given ordered
'''
import collections
d1=collections.orderedDict()
d1["empid"]=1001
d1["ename"]="Rahul"
d1["emSal"]=30000
for k in d1.items():
    print(k)