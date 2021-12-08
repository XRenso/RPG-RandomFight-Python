# # from typing import AsyncGenerator, Match
# # import asyncio
import random

# # class BorchMan(object):
# #     def __init__(self, name = "Undefind", lang = "Undefing", worker = "BOMJ", age = "Undefind", workYears = "no info"):
# #         self.name = name
# #         self.lang = lang
# #         self.worker = worker
# #         self.age = age
# #         self.workingYears = workYears
# #         return None

# #     def getSomething(self, *whatGet):
# #        what_u_want = {
# #            1: "Name:" + self.name,
# #            2: "Lang:" + self.lang,
#            3: "Work:" + self.worker,
#            4: self.age,
#            5: self.workingYears
#        }
#        for i in whatGet:
#         if i in what_u_want:
#             print( what_u_want[i])
#         else:
#             raise ValueError("Невернные данные")


# some_worker = BorchMan("John", "RU", "Borch")

# some_worker.getSomething(1,2,3)


class Enemy(object):
    def __init__(self, name, age, race, MaxAttack, country):
        self.name = name
        self.age = age
        self.race = race
        self.maxAttack = MaxAttack
        self.country = country

    def get_damage(self, damage):
        self.hp -= damage
        print(
            f"Вы нанесли урон {self.name} в размере {damage} едениц урона. \nУ {self.name} осталось {self.hp} хп")
    # def endDIE(self, heroName):
    #     print(f"Вы победили {self.name} из {self.country}. Мои поздравления {heroName}")

    def dead(self):
        if self.hp <= 0:
            return True
        elif self.hp > 0:
            return False

    def attack(self):
        attack = random.randrange(self.maxAttack+1)
        return attack

    def health(self):
        chance = random.randrange(self.maxAttack + self.hp)
        triplet = self.maxAttack + self.hp
        if chance == triplet:
            if self.hp > self.age:
                regen = random.randrange(self.hp - self.age)
                self.hp += regen
                print(f"Существо {self.name} срегинирировало {regen} хп")

            elif self.age > self.hp:
                regen = random.randrange(self.age - self.hp)
                self.hp += regen
                print(f"Существо {self.name} срегинирировало {regen} хп")
        else:
            print(f"{self.name} не удалось срегенирировать хп. Оно пропускает ход")


class Player(object):
    def __init__(self, name, age, race, MaxAttack, country):
        self.name = name
        self.age = age
        self.race = race
        self.maxAttack = MaxAttack
        self.country = country

    def get_damage(self, damage):
        self.hp -= damage
        print(
            f"{self.name} тебе нанесли урон в размере {damage} едениц урона. \nУ тебя осталось {self.hp} хп")

    def dead(self):
        if self.hp <= 0:
            return True
        elif self.hp > 0:
            return False

    def attack(self):
        attack = random.randrange(self.maxAttack+1)
        return attack

    def health(self):
        chance = random.randrange(self.maxAttack + self.hp)
        triplet = self.maxAttack + self.hp
        if chance == triplet:
            if self.hp > self.age:
                regen = random.randrange(self.hp - self.age)
                self.hp += regen
                print(f"Вы, {self.name} ,срегинирировали {regen} хп")

            elif self.age > self.hp:
                regen = random.randrange(self.age - self.hp)
                self.hp += regen
                print(f"Вы, {self.name} ,срегинирировали {regen} хп")
        else:
            print('Сегодня не ваш день, вам не повезло. Вы пропускаете ход')


monster_name = ['Урлук', 'Вельзиву', 'Батон', 'Борщ']