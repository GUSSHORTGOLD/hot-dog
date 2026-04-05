print("=== GRYZNY KHOT-DOG ===")
print("=" * 30)

class HotDog:
    def __init__(self):
        self.is_dirty = True
        self.ketchup = 0
        self.mustard = 0
        self.grease = 100

    def add_ketchup(self, amount):
        self.ketchup += amount
        print(f"Polili ketchup: {amount}%")

    def add_mustard(self, amount):
        self.mustard += amount
        print(f"Polili gorchitsu: {amount}%")

    def drop_on_shirt(self):
        print("blyat! Uronil na beluyu rubashku!")
        print("Teper mozhno ne est, a srazu vybrosyat")

    def eat(self):
        print("\nKHOT-DOG POEDEN")
        print(f"Seli {self.grease}% zhira")
        print("Sovest chista, zhivot polny")

dog = HotDog()
dog.add_ketchup(50)
dog.add_mustard(50)
dog.drop_on_shirt()
dog.eat()

print("\n=== KONETS ===")
