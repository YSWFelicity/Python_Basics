def make_dictionary(filename):
    contents = {}
    try:
        file=open(filename,"r"); 
        for line in file.readlines():   #iterate over each line of file
            entry=line.split(",");     #split each line at , and get result as list
            if(len(entry)==2):          #if entry has only two elements
                contents[entry[0].strip()]=entry[1].strip();    #add key-value pair to dictionary
    except Exception:       #if Exception thrown while opening file
        print("File doesn't exist");
    
    return contents;

print(make_dictionary("demo.txt")); #test with sample file