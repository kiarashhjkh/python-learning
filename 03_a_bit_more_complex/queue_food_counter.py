from typing import ItemsView

orders = []
completed_orders = []
total_revenue = 0
next_order_ID = 1

menu = {
    1: {"name": "Burger", "time": 10, "price": 15},
    2: {"name": "Pizza", "time": 15, "price": 15},
    3: {"name": "Fries", "time": 5, "price": 5},
    4: {"name": "Hotdog", "time": 10, "price": 10},
    5: {"name": "Chicken Sandwich", "time": 12, "price": 12},
    6: {"name": "Chicken Nuggets", "time": 8, "price": 9},
    7: {"name": "Cheeseburger", "time": 12, "price": 18},
    8: {"name": "Cola", "time": 2, "price": 3},
    9: {"name": "Orange Juice", "time": 2, "price": 4},
    10: {"name": "Water", "time": 1, "price": 2},
    11: {"name": "Milkshake", "time": 5, "price": 6},
    12: {"name": "Coffe", "time": 3, "price": 4},
}


def show_menu():
    print("====Menu====")

    for item_number, item in menu.items():
        print(f"{item_number}.{item['name']} | ${item['price']}")


def add_order():
    global next_order_ID

    customer = input("Enter customer name: ")
    selected_item = []
    total_bill = 0
    total_prep_time = 0

    show_menu()

    while True:
        try:
            item_id = int(input("Enter item ID: "))

            if item_id == 0:
                break

            if item_id not in menu:
                print("Invalid item ID!")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0!")
                continue

        except ValueError:
            print("Please enter valid numbers!")
            continue

        item = menu[item_id]

        selected_item.append({"name": item["name"], "quantity": quantity, "price": item["price"], "time": item["time"]})

        total_bill += item["price"] * quantity
        total_prep_time += item["time"] * quantity

        print(quantity, item["name"], "added to order.")

    if len(selected_item) == 0:
        print("No items selected!. no orders were made.")
        return

    order = {
        "id": next_order_ID,
        "customer": customer,
        "items": selected_item,
        "bill": total_bill,
        "prep_time": total_prep_time,
    }

    orders.append(order)

    print("====Order====")
    print("Order ID:", next_order_ID)
    print("Customer:", customer)

    for item in selected_item:
        print(f"{item['name']} | Quantity: {item["quantity"]} | Subtotal: ${item['price'] * item["quantity"]}")

    print("Total Bill: $", total_bill, sep="")
    print("Estimated Prep Time: ", total_prep_time)

    next_order_ID += 1


def show_orders():
    if len(orders) == 0:
        print("There are no pending orders.")
        return
    print("====pending orders=====")

    for order in orders:
        print(
            f"Order ID: {order['id']} | Customer: {order['customer']} | Bill: {order['bill']} | Prep Time: {order['prep_time']} min")

        for item in order["items"]:
            print(f" {item["name"]} x {item["quantity"]}")


def estimate_time():
    if len(orders) == 0:
        print("There are no pending orders.")
        return

    try:
        order_id = int(input("Enter order ID: "))
    except ValueError:
        print("Invalid order ID!")
        return

    waiting_time = 0

    for order in orders:
        if order["id"] == order_id:
            total_time = waiting_time + order["prep_time"]

            print("Waiting Time:", waiting_time, "minutes")
            print("Preparation Time:", order["prep_time"], "minutes")
            print("Estimated Time:", total_time, "minutes")
            return

        waiting_time += order["prep_time"]

    print("Order not found.")


def cancel_order():
    if len(orders) == 0:
        print("There are no orders to be cancelled.")
        return

    try:
        order_id = int(input("Enter order ID for cancellation: "))
    except ValueError:
        print("Invalid order ID!")
        return

    for i in range(len(orders)):
        if orders[i]["id"] == order_id:
            cancelled_order = orders.pop(i)

            print("Order cancelled successfully!")
            print("Cancelled order bill: $", cancelled_order["bill"], sep="")
            return

    print("Order not found.")


def complete_order():
    global total_revenue

    if len(orders) == 0:
        print("There are no pending orders.")
        return

    order = orders.pop(0)

    print("====Order completed====")
    print("Order ID:", order["id"])
    print("Customer:", order["customer"])

    for item in order["items"]:
        print(f" {item["name"]} x {item["quantity"]}")

    print("Total Revenue:", order["bill"], sep="")

    completed_orders.append(order)
    total_revenue += order["bill"]

    print("Order is completed.")
    print("Total Revenue: $", total_revenue, sep="")

def show_rev():
    print("====Revenue====")
    print("Total Revenue: $", total_revenue, sep="")
    print("Completed orders:", len(completed_orders))


def main():
    while True:
        print("=====Restaurant system======")
        print("1. Show menu")
        print("2. Add order")
        print("3. Show orders")
        print("4. Estimate prep time")
        print("5. Cancel order")
        print("6. Complete next order")
        print("7. Show revenue")
        print("0. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                show_menu()
            case "2":
                add_order()
            case "3":
                show_orders()
            case "4":
                estimate_time()
            case "5":
                cancel_order()
            case "6":
                complete_order()
            case "7":
                show_rev()
            case "0":
                print("System closed.")
                break
            case _:
                print("Invalid choice!")

main()