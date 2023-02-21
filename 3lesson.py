import random
class Cat:
    def __init__(self, name="Cat", home=None):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.home = home

    def get_home(self):
        self.home = House()

    def eat(self):
        self.satiety += 5
        self.home.food -= 5


    def chill(self):
        self.gladness += 10
        self.home.mess += 5


    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        self.days_indexes(day)
        dice = random.randint(1, 2)
        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                print("So I will clean the house")
                self.eat()
            else:
                print("Let`s chill!")
                self.chill()
        elif dice == 1:
            print("Let`s chill!")
            self.chill()
        elif dice == 2:
            print("Cleaning time!")
            self.eat()


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
                "Java developer":
                    {"salary": 50, "gladness_less": 10},
                "Python developer":
                    {"salary": 40, "gladness_less": 3},
                "C++ developer":
                    {"salary": 45, "gladness_less": 25},
                "Rust developer":
                    {"salary": 70, "gladness_less": 1},
            }

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

stray = Cat(name="Stray")
for day in range(1, 800):
    if stray.live(day) == False:
         break
