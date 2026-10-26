import os
os.chdir("D:\\")
print(os.getcwd())
try:
    with open ("data1.txt","a") as fa:
        fa.write("new content into a new file")
        fa.write(input("Enter some new text: "))
        fa.close
except FileNotFoundError:
    print("unable to create file!")
    
