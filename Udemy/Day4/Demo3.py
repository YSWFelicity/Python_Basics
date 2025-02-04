states_of_america = ["Delaware", "NJ", "WA"]
# change the first index to "PA"
states_of_america[0] = "PA"

print(states_of_america[0])
print(states_of_america[-1])

# add one more index of element 
states_of_america.append("CA")
print(states_of_america)

states_of_america.extend(["Angelaland", "Jack"])
print(states_of_america)