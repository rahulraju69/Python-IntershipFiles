def semister():
    sem=1
    print("its 1st sem")
    yield sem #it will return and remember
    sem+=1
    print("its 2st sem")
    yield sem  # it will return and remember
    sem += 1
    print("its 3st sem")
    yield sem  # it will return and remember
    sem += 1
    print("its 4st sem")
    yield sem  # it will return and remember
    sem += 1

s=semister()
print(next(s))
print(next(s))
print(next(s))
print(next(s))