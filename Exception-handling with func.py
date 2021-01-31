def show_sal(sal):
    try:
        return (sal)*12
    except Exception as e:
        print("exception raised..",e)
ctc=show_sal(int(input("enter the sal:")))
print("CTC:",ctc)

#ctc1=show_sal("not finalized") #exception raised
#print("CTC1",ctc1)