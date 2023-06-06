import io 
import json
import pyperclip as pc

# to run in interactive mode type python -i <file-name>

def get_pasted_info():
    user_move = input("copy data to the clipboard, press any key to continue")
    listinfo = pc.paste()

    with io.open("lesson-data.json","w",encoding="utf8") as f:
        f.write(listinfo)

    with io.open("lesson-data.json","r",encoding="utf8") as f:
        data = f.read()
    data = data.splitlines()
    return data 

def create_dict(vocab):
    i = 0
    new_dict = {}
    while i < len(vocab):
        new_dict[vocab[i]] = vocab[i + 1]
        i+=2
    return new_dict     

def get_data(file):
    with io.open(file, "r", encoding="utf8") as f:
        data = f.read()
        data = json.loads(data)
        return data
    
def main():
    while True:
        user_data = get_pasted_info()
        lesson_info = create_dict(user_data)
        open_data = get_data("lesson-data.json")
        lesson_titles = [i.lower() for i in open_data]
        while True:
            title = input("enter the title of the lesson ").lower
            if title in lesson_titles:
                print(f"the lesson is already there choose another title ")
                continue
            break
        

