import random

name = ['Урлук', 'Вельзиву', 'Батон', 'Борщ', 'Багет',
                'Монстрищее', 'Взрыватель', 'ок', 'ЕссБОЙ', 'Уничтожитель5000']

race = ['Еда', 'Эльф', 'Гном', 'Человек', 'Робот', 'Киборг',
                'Призрак', 'Насекомое', 'Животное', 'Друид', 'Демон', 'Вирус']



country = ['Евразия', 'Остазия', 'Луна', 'Бумбаза',
                   'Угинара', 'Мастараза', 'БАЗА', 'Марс', 'Земля', 'Завод']




class Enemy(object):
    def __init__(self, name, age, race, hp, max_attack, country):
        self.name = name
        self.age = age
        self.chance = random.randrange(1, 101)
        self.race = race
        self.hp = hp
        self.maxHP = hp
        self.maxAttack = max_attack
        self.country = country

    def get_damage(self, damage):
        self.hp -= damage

        return f"Вы нанесли урон {self.name} в размере {damage} едениц урона. \nУ {self.name} осталось {self.hp} хп"

    # def endDIE(self, heroName):
    #     print(f"Вы победили {self.name} из {self.country}. Мои поздравления {heroName}")

    def dead(self):
        if self.hp <= 0:
            return True
        elif self.hp > 0:
            return False

    def attack(self):
        attack = random.randrange(self.maxAttack + 1)
        return attack

    def health(self):

        if self.hp < self.maxHP:
            can_u_heal = random.randrange(-5, self.chance + 1)
            if self.chance != 0:
                can_u_heal = round(can_u_heal / self.chance)
            if self.chance == 100:
                heal = random.randrange(1, self.maxHP - self.hp)
                self.hp += heal
                self.chance = 0
                return f"Вот как бывает. {self.name} увеличило свое здоровье на {heal}"

            elif self.chance > 0 and self.chance != 100 and can_u_heal >= 0.5:
                heal = random.randrange(1, self.maxHP - self.hp)
                self.hp += heal
                self.chance = 0
                return f"Вот эта фортуна\nне для тебя..... \n{self.name} повысило хп на {heal}"
            elif can_u_heal < 0:
                damage = random.randrange(1, self.maxHP - self.hp)
                self.hp -= damage
                self.chance += random.randrange(5, 21)
                return f"О ДАААА. \n{self.name} получило чертов критический промах. \nШприц порвал его вены. \nОно получило {damage} урона"

            else:
                self.chance += random.randrange(1, 21)
                return 'Сегодня не твой день. \nЯ думаю в следущий раз повезет'

    def get_stat(self, whatUwant):
        match whatUwant:
            case 'name':
                return self.name
            case 'age':
                return self.age
            case 'country':
                return self.country
            case 'hp':
                return self.hp
            case 'race':
                return self.race
            case 'maxHP':
                return self.maxHP


def create_monster():
    random.shuffle(name)

    random.shuffle(race)
    age = random.randrange(3000)
    hp = random.randrange(1, 400)

    monster_maxAttack = random.randrange(1, 100)

    random.shuffle(country)

    monster = Enemy(random.choice(name), age,
                    random.choice(race), hp, monster_maxAttack, random.choice(country))

    return monster