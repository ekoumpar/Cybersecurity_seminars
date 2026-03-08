# 0. Initiallize customer data
customers = [
    {"name": "Άννα", "email": "anna@example.com", "age": 28},
    {"name": "Κώστας", "email": "kostas@example.com", "age": 35},
    {"name": "Ιωάννα", "email": "ioanna@example.com", "age": 22}
]

# 1. Anonymization Function
def anonymize_customers(customers):
    anonymous_customers = []
    for c in customers:
        anonymous_customers.append({
            "customer_id": "USER" + str(customers.index(c) + 1),
            "age": c["age"]
        })
    return anonymous_customers

# 2. Mapping Function
def map_function(customers, anonymous_customers):
    mapping_table = []
    for i in range(len(customers)):
        mapping_table.append({
            "customer_id": anonymous_customers[i]["customer_id"],
            "name": customers[i]["name"],
            "email": customers[i]["email"]
        })
    return mapping_table


# 3. Show anonymized data and mapping table
print("Original Customers:")
for c in customers:
    print(c)

anonymous_customers = anonymize_customers(customers)
print("\nAnonymous Customers:")
for ac in anonymous_customers:
    print(ac)

mapping_table = map_function(customers, anonymous_customers)
print("\nMapping Table:")
for map in mapping_table:
    print(map)


# 4. Value of Anonymized Data for GDPR Compliance
#
# Personal data anonymization helps to comply with GDPR regulations and to
# protect personal information by masking  any identifiable data.
# It reduces the risk of personal data leaks and ensures that even if data
# is exposed, individuals cannot be easily identified. Also, promotes data 
# processing without compromising privacy.