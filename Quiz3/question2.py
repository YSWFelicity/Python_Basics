def make_dictionary(filename):
    contents = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                each_line = line.split(",")
                if len(each_line) == 2:
                    contents[each_line[0].strip()] = each_line[1].strip()
        return contents
    except FileNotFoundError:
        print("File doesn't exist")
        return contents

print(make_dictionary("try1.txt"))
