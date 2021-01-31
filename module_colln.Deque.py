'''
it is a obj of collection where inserting and deleting is posssible from both head and tail sides.
it is also called as double ended queue
'''
import collections
q=collections.deque([10,20,30,40,50])
print(q)
q.append(60)
print("after append:",q)
q.appendleft(5)#it will append only left
print("append in begginging:",q)
q.pop()
print("it always pop from tail:",q)
q.popleft()
print("it will remove at first",q)