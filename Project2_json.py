import json

try:
    data = {
        "name": "Manasa",
        "email": "manasa.sangadala@gmail.com",
        "city": "Pileru"
    }

    json_data = json.dumps(data, indent=4)

    print("User Details:\n")
    print(json_data)

    with open("user_data.json", "w") as file:
        file.write(json_data)

    print("\nJSON data saved successfully!")

except Exception as e:
    print("Error:", e)
