import io 
import json
import uuid

def write_json_file(file, data):
    """Takes a file and a python data structure as inputs.
    Writes data to a json file. Returns nothing"""
    with io.open(file,"w",encoding="utf8") as f:
        json.dump(data, f, indent=2)

def read_json_file(file):
    """Takes a json file as input.
    Reads the file and returns a python object."""
    with io.open(file, "r", encoding="utf8") as f:
        data = f.read()
        return json.loads(data)

def get_user_data():
    """Takes no arguments. Gets input from the user 
    and returns data stripped of white space in the form of a list."""
    data = input(
 "Enter up to 10 pairs of items to learn separated by commas.\n\
 Do not enter a comma after the last entry.\n\
 Example: uno, one, dos, two, Me llemo Emily., My name is Emily.\n")
    data = data.split(',')
    data = [i.strip() for i in data]
    return data

def split_list(user_data):
    """Takes user data and returns two lists. the target items and the native items."""
    target = []
    native = []
    for i in range(len(user_data)):
        if i % 2 == 0:
            target.append(user_data[i])
        else:
            native.append(user_data[i])
    return target, native

def check_lesson_titles(data):
    """Takes the lesson data and creates a list
    of all lesson titles. Asks the user to input a title repeatedly
    until the user produces a title that does not already exist.
    Returns the lesson title"""
    while True:
        title = input('Enter a title for the lesson: ')
        if len(data) == 0:
            return title
        else:
            titles = [data[i][0]['title'] for i in range(len(data))]
            if title in titles:
                print(f'{title} already exists. Please choose a different title.')
                continue                  
            return title

def view_lesson(lesson):
    title = lesson[0]['title']
    print(title.upper())
    print('=' * len(title), '\n')
    for i in range(len(lesson[1])):
        target = lesson[1][i]["target"]
        native = lesson[1][i]["native"]
        length = 50 - (len(target) + len(native))
        print(f'{target} {"." * length} {native}')
    print()

def creeate_lesson(target, native, title):
    lesson = [
        {
            'date_visited': 'not visited',
            'times_viewed': 0,
        },
        []
    ]
    lesson[0]['title'] = title
    for i in range(len(target)):
        vocabulary = {
            'difficult': False,
            'easy': False
        }
        id = uuid.uuid4()
        id = str(id)
        vocabulary['id'] = id
        vocabulary['target'] = target[i]
        vocabulary['native'] = native[i]
        lesson[1].append(vocabulary)
    return lesson

def get_input(choices):
    inputs = []
    messages = []
    for i in range(len(choices)):
        inputs.append(choices[i][0])
        messages.append(choices[i][1])
    for i in range(len(inputs)):
        print(f"{inputs[i]}   {messages[i]}")
    while True:
        user_input = input('Choose an option: ')
        if user_input in inputs:
            return user_input
        continue

def main():
    lesson_data = read_json_file('lesson_data.json')
    while True:
        while True:
            user_data = get_user_data()
            # check that the list contains target native pairs. (an even number of entries)
            if len(user_data) % 2 != 0:
                print(
    '\none of your entries is missing a pair or you entered a comma after the final entry\n\
    Please enter the data again.')
                continue
            break
        target, native = split_list(user_data)
        title = check_lesson_titles(lesson_data)
        lesson = creeate_lesson(target, native, title)
        view_lesson(lesson)    
        choices = [['s', 'Save Lesson'], ['r', 'Re-enter Lesson Data'], ['q', 'Quit']]
        user_input = get_input(choices)
        if user_input == 's':
            lesson_data.append(lesson)
            write_json_file('lesson_data.json', lesson_data)
            print(f'{title} has been saved.')
            break
        if user_input == 'r':
            continue                
        if user_input == 'q':
            print('The lesson data entered has not been saved.')
            break

if __name__ == '__main__':
    main()
