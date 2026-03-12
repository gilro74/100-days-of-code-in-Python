my_first_dictionary = {
    "idea":" A thought.",
    "Intellect":" Where curiosity becomes knowledge."
}

print(my_first_dictionary["Intellect"])

travel_log ={
    "France":["Paris","Dubai","PLK"]
}
#Accessing elemnts in nested lists and dictionaries
print(travel_log["France"][1])
nested_list =["A","B",["C","D"]]
print(nested_list[2][0])


travel_history ={
    "France": {
        "no_times_visited ": 8,
        "cities_visited" : ["Paris","Dubai","PLK"]
    },
    "South Africa": "Mzansi"
}

print(travel_history["France"]["cities_visited"][2])