import io 
import json
import pyperclip as pc

# to run in interactive mode type python -i <file-name>

listinfo = pc.paste()

with io.open("foe.txt","w",encoding="utf8") as f:
    f.write(listinfo)

with io.open("foe.txt","r",encoding="utf8") as f:
    data = f.read()
data = data.splitlines()


newdata = []

for i in data:
    if i != "":
        newdata.append(i)
new_data = [i.strip() for i in newdata]

print(new_data)

