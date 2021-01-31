import collections
#creating named tuple
student=collections.namedtuple("student",["name","Branch","avg"])
s1=student("rahul","cse",98.88)
print(s1)
print(s1.name)
for i in s1:
    print(i)