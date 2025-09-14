capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
    "China": "Beijing"
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dij"],
#     "Germany": ["Berlin", "Stuttgart"]
# }

# Print Lille
# print(travel_log["France"][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][0])
