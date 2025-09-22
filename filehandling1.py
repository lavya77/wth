file = open("lav2.txt","w")
file.write("Hello, this is my second file\n")
file.close()

# lav2.txt never existed it created lav2.txt when i opened in write mode and wrote soem lines.
# running again the same code wont write same lines again. as it overwrittees..
file = open("lav2.txt","r")
content=file.read()
print(content)
file.close()

#with (auto-closes file)
with open("lav2.txt","a") as f:
    f.write("Adding another line safely!!\n")

file = open("lav2.txt","r")
content=file.read()
print(content)
file.close()
