try:
    import io
    file1=open("rahul1.txt","r")
    file1.write("this is a sample txt")
    file1.close()
except Exception as e:
    print("exception raised.....",e)
else:
    print("data written to the file succesfully")
    