class Coffee:
    s_water = "water"
    s_milk = "milk"
    s_beans = "coffee beans"
    s_cups = "cups"

    def __init__(self, name, water, milk, beans, price):
        self.name = name
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = 1
        self.price = price

    # ### return coffee fields in coffee requirements data structure I am using
    # coffee_requirements = [supplies, price] => supplies = [water, milk, beans, cups], money = int
    def coffee_req(self):
        return [[self.water, self.milk, self.beans, self.cups], self.price]


class CoffeeMachine:
    supplies_name = [Coffee.s_water, Coffee.s_milk, Coffee.s_beans, Coffee.s_cups]
    espresso = Coffee("espresso", 250, 0, 16, 4)
    latte = Coffee("latte", 350, 75, 20, 7)
    cappuccino = Coffee("cappuccino", 200, 100, 12, 6)
    coffees_ingredients = [espresso.coffee_req(),
                           latte.coffee_req(),
                           cappuccino.coffee_req()]

    def __init__(self, supplies, money):
        self.supplies = supplies
        self.money = money
        self.state = "menu"     # available states: menu, make_coffee, supply
        self.state_index = 0    # sub-state allowing to iterate through supply state
        # allowing to follow the flow of input questions
        self.current_question = "Write action (buy, fill, take, remaining, exit): "
        print(self.current_question)

    def input_action(self, answer):
        if self.state == "menu":
            if answer == "buy":
                self.state = "make_coffee"
                self.current_question = "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"
            elif answer == "fill":
                self.state = "supply"
                self.current_question = "Write how many ml of water you want to add:"
            elif answer == "take":
                self.take_money()
            elif answer == "remaining":
                self.display_machine_state()
            elif answer == "exit":
                exit()
        elif self.state == "supply":
            try:
                if self.supply_machine(answer, self.state_index):   # if user input negative integer
                    print("Enter only positive Integer value")
                    return None
            except ValueError:              # if user input was not expected
                print("Enter only Integer value")
                return None
            self.state_index += 1
            if self.state_index > 3:
                self.state_index = 0
                self.state = "menu"
        elif self.state == "make_coffee":
            if self.make_coffee(answer):    # if user input was not expected
                pass
            else:                           # if "back" has been typed, coffee has been made or lack of supplies
                self.current_question = "Write action (buy, fill, take, remaining, exit): "
                self.state = "menu"
        print(self.current_question)

    def supply_machine(self, answer, index):
        question = ["Write how many ml of water you want to add:",
                    "Write how many ml of milk you want to add:",
                    "Write how many grams of coffee beans you want to add:",
                    "Write how many disposable cups you want to add:",
                    "Write action (buy, fill, take, remaining, exit): "]
        if int(answer) < 0:
            return True
        self.supplies[index] += int(answer)
        self.current_question = question[index+1]

    def display_machine_state(self):
        print(f"The coffee machine has:")
        print(f"{self.supplies[0]} ml of water")
        print(f"{self.supplies[1]} ml of milk")
        print(f"{self.supplies[2]} g of coffee beans")
        print(f"{self.supplies[3]} disposable cups")
        print(f"${int(self.money)} of money\n")

    def take_money(self):
        cash = self.money
        self.money = 0
        print(f"I gave you ${cash}")

    def make_coffee(self, answer):
        try:
            answer = int(answer) - 1
        except ValueError:
            if answer == "back":
                return None
            return True
        possible = True
        for i in range(len(self.supplies)):
            if self.coffees_ingredients[answer][0][i] == 0:
                continue
            if self.supplies[i] // self.coffees_ingredients[answer][0][i] == 0:
                print(f"Sorry, not enough {self.supplies_name[i]}!")
                possible = False
        if not possible:
            return None
        else:
            print("I have enough resources, making you a coffee!")
            for i in range(len(self.supplies)):
                self.supplies[i] -= self.coffees_ingredients[answer][0][i]
            self.money += self.coffees_ingredients[answer][1]


if __name__ == '__main__':
    starting_supplies = [400, 540, 120, 9]
    starting_money = 550
    cm = CoffeeMachine(starting_supplies, starting_money)
    while True:
        cm.input_action(input())
