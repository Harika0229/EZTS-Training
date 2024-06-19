import os
#To write to  the file
with open("harika.txt",'w') as f:
    f.write("I am harika")
    f.close()
    
#To read from the file
with open("harika.txt",'r') as f:
    print(f.read())
    f.close()
    s=f.read()
    f.close()
    
#To replace the text in the file
s=s.replace("harika","neelima")
with open("harika.txt",'w')as f:
    f.write(s)
    f.close()
    
#To read at specific positions
with open("harika.txt",'r+b') as f:
    print(f.tell())
    f.seek(-35,2)
    f.write(b"#")
    print(f.read().decode('utf-8'))
    f.close()
    
#To delete the file
os.remove("harika.txt")

    
