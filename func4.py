'''func with variable no of args
"*" meanswe can give n number of values
'''
def studentExam(name,*marks):
    print("student marks:",name)
    print("marks:",marks)
    print("total:",sum(marks))
    print("average",len(marks))
studentExam("rahul",50,60,65,80)