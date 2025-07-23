'''data = {
    1: {'name': 'Rice', 'Price': 60},
    2: {'name': 'milk', 'Price': 40},
    3: {'name': 'solt', 'Price': 20},
    4: {'name': 'sugur', 'Price': 30},
    5: {'name': 'eggs', 'Price': 70},
    6: {'name': 'cooking', 'Price': 100},
    7: {'name': 'bread', 'Price': 40},
    8: {'name': 'soap', 'Price': 50},
    9: {'name': 'salt', 'Price': 60},
    10: {'name': 'mandi', 'Price': 60}
}

# Print the list of items
for i in data:
    print(f'{i}. {data[i]["name"].ljust(15, " ")} : {data[i]["Price"]}')

# User input
items = list(map(int, input('Enter item numbers (space separated): ').split()))

total = 0
ids = set()

for i in items:
    if i not in ids:
        count = items.count(i)
        price = data[i]['Price']
        total += price * count
        print(f'{data[i]["name"]} - {count} * {price} = {price * count}')
        ids.add(i)

print('Total bill:', total)
'''

#-----------------------------------------------------------------------------------------------------------------
import random

print("===== Welcome to Python Zomato =====")

users = []
menu = [
    {"id": 1, "item": "Pizza", "price": 200, "rating": 4.5, "reviews": []},
    {"id": 2, "item": "Burger", "price": 120, "rating": 4.0, "reviews": []},
    {"id": 3, "item": "Fried Rice", "price": 150, "rating": 3.9, "reviews": []}
]
delivery_boys = ["Raj", "Amit", "Rekha", "Shiva"]
orders = []

logged_in = False
current_user = None

while not logged_in:
    print("\n1. Register\n2. Login")
    choice = input("Select option: ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")

        # Check if username already exists
        exists = False
        i = 0
        while i < len(users):
            if users[i]["username"] == username:
                exists = True
                break
            i += 1

        if exists:
            print("Username already exists. Try another.")
        else:
            users.append({"username": username, "password": password, "orders": []})
            print("Registered successfully. Please login now.")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        i = 0
        while i < len(users):
            if users[i]["username"] == username and users[i]["password"] == password:
                logged_in = True
                current_user = users[i]
                print("Login successful! Welcome", username)
                break
            i += 1
        if not logged_in:
            print("Invalid credentials.")

while True:
    print("\n===== Main Menu =====")
    print("1. View Menu")
    print("2. Sort Menu by Rating")
    print("3. Sort Menu by Price")
    print("4. Add Food Item")
    print("5. Add Review/Rating")
    print("6. Place Order")
    print("7. View Order History")
    print("8. Logout")

    option = input("Select an option: ")

    if option == "1":
        print("\n--- Food Menu ---")
        i = 0
        while i < len(menu):
            print(menu[i]["id"], "-", menu[i]["item"], "| ₹", menu[i]["price"], "| ⭐", menu[i]["rating"])
            j = 0
            while j < len(menu[i]["reviews"]):
                print("   -", menu[i]["reviews"][j])
                j += 1
            i += 1

    elif option == "2":
        print("\n--- Menu Sorted by Rating ---")
        sorted_menu = sorted(menu, key=lambda x: x["rating"], reverse=True)
        i = 0
        while i < len(sorted_menu):
            print(sorted_menu[i]["id"], "-", sorted_menu[i]["item"], "| ₹", sorted_menu[i]["price"], "| ⭐", sorted_menu[i]["rating"])
            i += 1

    elif option == "3":
        print("\n--- Menu Sorted by Price (Low to High) ---")
        sorted_menu = sorted(menu, key=lambda x: x["price"])
        i = 0
        while i < len(sorted_menu):
            print(sorted_menu[i]["id"], "-", sorted_menu[i]["item"], "| ₹", sorted_menu[i]["price"], "| ⭐", sorted_menu[i]["rating"])
            i += 1


    elif option == "4":
        name = input("Enter item name: ")
        price = int(input("Enter price: "))
        rating = float(input("Enter rating (0.0 to 5.0): "))
        new_id = len(menu) + 1
        menu.append({"id": new_id, "item": name, "price": price, "rating": rating, "reviews": []})
        print("Item added successfully!")

    elif option == "5":
        item_id = int(input("Enter item ID to review: "))
        comment = input("Enter your review: ")
        i = 0
        found = False
        while i < len(menu):
            if menu[i]["id"] == item_id:
                menu[i]["reviews"].append(current_user["username"] + ": " + comment)
                found = True
                break
            i += 1
        if found:
            print("Review added.")
        else:
            print("Item not found.")

    elif option == "6":
        print("\n--- Place Order ---")
        order_cart = []
        total = 0
        while True:
            item_id = int(input("Enter item ID to add to cart (0 to finish): "))
            if item_id == 0:
                break

            i = 0
            added = False
            while i < len(menu):
                if menu[i]["id"] == item_id:
                    order_cart.append(menu[i])
                    total += menu[i]["price"]
                    print(menu[i]["item"], "added.")
                    added = True
                    break
                i += 1

            if not added:
                print("Invalid ID.")

        if len(order_cart) > 0:
            print("Order placed!")
            delivery = delivery_boys[random.randint(0, len(delivery_boys) - 1)]
            current_user["orders"].append({"items": order_cart, "total": total, "delivery": delivery})
            print("Delivery assigned to:", delivery)
        else:
            print("No items selected.")

    elif option == "7":
        print("\n--- Your Order History ---")
        if len(current_user["orders"]) == 0:
            print("No orders yet.")
        else:
            i = 0
            while i < len(current_user["orders"]):
                order = current_user["orders"][i]
                print("Order", i+1, "| Delivered by:", order["delivery"], "| Total: ₹", order["total"])
                j = 0
                while j < len(order["items"]):
                    print("  -", order["items"][j]["item"], "| ₹", order["items"][j]["price"])
                    j += 1
                i += 1

    elif option == "8":
        print("Logged out.")
        break

    else:
        print("Invalid option.")