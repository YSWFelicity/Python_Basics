def name_processor(names):
    newList = []
    for name in names:
        words = name.split(' ')
        if len(words) > 1:
            newName = words[len(words)-1]+", "+words[0]
        else:
            newName = words[0]
        newList.append(newName)
    return newList
