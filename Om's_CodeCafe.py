class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cafe:
    def __init__(self):
        self.menu = [
            MenuItem("☕ Coffee", 50),
            MenuItem("🍔 Burger", 80),
            MenuItem("🍟 Fries", 40),
            MenuItem("🥤 Cold Drink", 30),
            MenuItem("🧋 Cold Coffee", 80),
            MenuItem("🍜 Masala Maggi", 40),
            MenuItem('🥪 Veg Sandwich', 60),
            MenuItem("🧀🥪 Cheese Sandwich", 80)
        ]
        self.order = []

    def show_menu(self):
        print("📋 Menu:")

        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item.name} - ₹{item.price}")

    def take_order(self):
        while True:
            try:
                choice = int(input("Enter item number to order (0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.menu):
                    self.order.append(self.menu[choice - 1])
                    print(f"✅ {self.menu[choice - 1].name} added to your order.")
                else:
                    print("❌ Invalid item number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    def show_bill(self):
        if not self.order:
            print("⚠️ No items ordered.")
            return
        total = 0
        print("\n🧾 Your Bill:")
        for item in self.order:
            print(f"- {item.name} - ₹{item.price}")
            total += item.price
        print(f"Total Amount: ₹{total}")

# Main Program
if __name__ == "__main__":
    cafe = Cafe()
    cafe.show_menu()
    cafe.take_order()
    cafe.show_bill()




