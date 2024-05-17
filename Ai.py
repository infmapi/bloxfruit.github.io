import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.inventory = {}

    def add_fruit(self, fruit, quantity=1):
        if fruit in self.inventory:
            self.inventory[fruit] += quantity
        else:
            self.inventory[fruit] = quantity

    def remove_fruit(self, fruit, quantity=1):
        if fruit in self.inventory:
            self.inventory[fruit] -= quantity
            if self.inventory[fruit] <= 0:
                del self.inventory[fruit]

    def display_inventory(self):
        print(f"Inventory for {self.name}:")
        for fruit, quantity in self.inventory.items():
            print(f"{fruit}: {quantity}")

    def increase_score(self, points):
        self.score += points
        if self.score >= 950:
            print("All hacks stopped!")

# Example usage:
if __name__ == "__main__":
    player1 = Player("Player1")
    while player1.score < 1000:
        fruit = random.choice(["Mera Mera no Mi", "Gomu Gomu no Mi", "Suna Suna no Mi"])
        player1.add_fruit(fruit)
        player1.increase_score(random.randint(50, 200))

    player1.display_inventory()
    print("Final Score:", player1.score)
