class BillingSystem:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        self.items.append({'name': name, 'quantity': quantity, 'price': price})

    def generate_bill(self):
        total_amount = 0
        bill = ""

        bill += "==============================\n"
        bill += "         BILLING SYSTEM       \n"
        bill += "==============================\n"
        bill += "{:<20} {:<10} {:<10}\n".format("Item", "Quantity", "Price")
        bill += "------------------------------\n"

        for item in self.items:
            item_total = item['quantity'] * item['price']
            total_amount += item_total
            bill += "{:<20} {:<10} {:<10}\n".format(item['name'], item['quantity'], item_total)

        bill += "------------------------------\n"
        bill += "Total Amount: {:<20}\n".format(total_amount)
        bill += "==============================\n"

        return bill

# Main program
billing_system = BillingSystem()

while True:
    choice = input("Do you want to add an item to the bill? (yes/no): ").lower()
    if choice == 'yes':
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        billing_system.add_item(name, quantity, price)
    elif choice == 'no':
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

if billing_system.items:
    print(billing_system.generate_bill())
else:
    print("No items added to the bill.")
