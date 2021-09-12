Customer = {
    "name": "Janavi panchal",
    "age": "19",
    "is_verified": True
}

print(Customer['name'])
# print(Customer['birthdate'])
print(Customer.get("birthdate"))
print(Customer.get("birthdate", "25th Oct,2001"))
print(Customer.get("name"))
Customer["name"] = "Janavi"
print(Customer.get("name"))
