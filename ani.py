def get_max_salary_per_city_department(employees):
    # Dictionary to store the maximum salary record for each city-department
    max_salary_dict = {}

    for employee in employees:
        name, salary, city, department = employee
        key = (city, department)  # Unique combination of city and department
        
        # If the combination is not in the dictionary or current salary is higher
        if key not in max_salary_dict or salary > max_salary_dict[key][1]:
            max_salary_dict[key] = employee  # Update with the higher salary record

    # Extract the results from the dictionary
    return list(max_salary_dict.values())

# Input
employees = [
    ["A", 90000, "BNG", "IT"],
    ["B", 80000, "HYD", "IT"],
    ["C", 70000, "BNG", "IT"],
    ["D", 100000, "HYD", "IT"],
    ["E", 40000, "HYD", "CS"]
]

# Function Call
result = get_max_salary_per_city_department(employees)

# Output
print(result)
