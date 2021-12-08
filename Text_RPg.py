# # from typing import AsyncGenerator, Match
# # import asyncio
import random
last_action = 'Пока ничего не произошло'
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
    global last_action
    def __init__(self, name, age, race, hp, MaxAttack, country):
        self.name = name
        self.age = age
        self.race = race
        self.hp = hp
        self.maxAttack = MaxAttack
        self.country = country

    def get_damage(self, damage):
        self.hp -= damage
        
        last_action =    f"Вы нанесли урон {self.name} в размере {damage} едениц урона. \nУ {self.name} осталось {self.hp} хп"
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
                last_action = f"Существо {self.name} срегинирировало {regen} хп"

            elif self.age > self.hp:
                regen = random.randrange(self.age - self.hp)
                self.hp += regen
                last_action = f"Существо {self.name} срегинирировало {regen} хп"
        else:
            last_action = f"{self.name} не удалось срегенирировать хп. Оно пропускает ход"

    def get_stat(self, whatUwant):
        if whatUwant == 'name':
            return self.name
        elif whatUwant == 'age':
            return self.age
        elif whatUwant == 'country':
            return self.country
        elif whatUwant == 'hp':
            return self.hp


class Player(object):
    global last_action
    def __init__(self, name, age, race, hp, MaxAttack, country):
        self.name = name
        self.age = age
        self.race = race
        self.hp = hp
        self.maxAttack = MaxAttack
        self.country = country

    def get_damage(self, damage):
        self.hp -= damage
        
        last_action = f"{self.name} тебе нанесли урон в размере {damage} едениц урона. \nУ тебя осталось {self.hp} хп"

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
                last_action = f"Вы, {self.name} ,срегинирировали {regen} хп"

            elif self.age > self.hp:
                regen = random.randrange(self.age - self.hp)
                self.hp += regen
                last_action = f"Вы, {self.name} ,срегинирировали {regen} хп"
        else:
            last_action = 'Сегодня не ваш день, вам не повезло. Вы пропускаете ход'

    def get_stat(self, whatUwant):
        if whatUwant == 'name':
            return self.name
        elif whatUwant == 'age':
            return self.age
        elif whatUwant == 'country':
            return self.country
        elif whatUwant == 'hp':
            return self.hp


monster_name = ['Урлук', 'Вельзиву', 'Батон', 'Борщ', 'Багет',
                'Монстрищее', 'Взрыватель', 'ок', 'ЕссБОЙ', 'Уничтожитель5000']
random.shuffle(monster_name)

monster_age = random.randrange(3000)

monster_race = ['Еда', 'Эльф', 'Гном', 'Человек', 'Робот', 'Киборг',
                'Призрак', 'Насекомое', 'Животное', 'Друид', 'Демон', 'Вирус']
random.shuffle(monster_race)

monster_hp = random.randrange(1, 400)

monster_maxAttack = random.randrange(1, 100)

monster_country = ['Евразия', 'Остазия', 'Луна', 'Бумбаза',
                   'Угинара', 'Мастараза', 'БАЗА', 'Марс', 'Земля', 'Завод']
random.shuffle(monster_country)

monster = Enemy(random.choice(monster_name), monster_age,
                monster_race, monster_hp, monster_maxAttack, random.choice(monster_country))


player_name = input('Как вас зовут странник - ')
player_age = int(input('Сколько лет вашему герою - '))
player_race = input('Какая ваша расса - ')
player_country = input('Откуда вы - ')


player_hp = random.randrange(1, 400)

player_maxAttack = random.randrange(1, 120)

player = Player(player_name, player_age, player_race,
                player_hp, player_maxAttack, player_country)


ruletka = random.randrange(2)
first_move = None
second_move= None
if ruletka == 1:
    first_move = 'Enemy'
    second_move = 'Player'
elif ruletka == 0:
    first_move = 'Player'
    second_move = 'Enemy'


step = 0

while True:
    
    print(f"Ваш враг - {monster.get_stat('name')} \nСтрана врага - {monster.get_stat('country')} \nВозраст врага - {monster.get_stat('age')}")

    print(f"\n\n\n\nВы - {player.get_stat('name')} \nВаша страна - {player.get_stat('country')} \nВаш возрас - {player.get_stat('age')}")

    print(f"\n\n\n\n {last_action}")

    if step == 0 and first_move == 'Enemy':
        if monster.get_stat('hp') == monster_hp:
            player.get_damage(monster.attack())
        elif monster.get_stat('hp') != monster_hp:
            monster.health()

        step += 1

    elif step == 0 and first_move == 'Player':
        action = int(input('1)Атака \n2)Вылечиться \nЧто делаем - '))
        
        if action == 1:
            monster.get_damage(player.attack())
        elif action == 2:
            player.health()

        step += 1
    elif step == 1 and second_move == 'Player':
        action = int(input('1)Атака \n2)Вылечиться \nЧто делаем - '))
        
        if action == 1:
            monster.get_damage(player.attack())
        elif action == 2:
            player.health()
        step = 0
    if step == 1 and first_move == 'Enemy':
        if monster.get_stat('hp') == monster_hp:
            player.get_damage(monster.attack())
        elif monster.get_stat('hp') != monster_hp:
            monster.health()
        
        step = 0

