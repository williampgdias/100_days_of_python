states_of_america = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
    "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana"
]

# print(states_of_america[50])

# NESTED LISTS
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
#                "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])

print(dirty_dozen[0][1])