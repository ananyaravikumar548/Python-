with open("file.txt","r") as f:
    content=f.readline()
    print(f.readline(), end=" ")
    content1 =f.readlines()
    print(content)
    print(content1)
    print("file closed")
