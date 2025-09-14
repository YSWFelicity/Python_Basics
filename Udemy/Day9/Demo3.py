# Dictionary就是对应Java的HashMap(Key, Value)
programming_dictionary = {
    "Bug": "An error",
    "Function": "a piece of code",
    "Loop": "The action of doing",
}

print(programming_dictionary["Function"])

# 这里是加一个dictionary内容
programming_dictionary["Loop"] = "The action of"

# 新的dictionary重新打印出来
# print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
