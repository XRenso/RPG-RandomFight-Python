import random


class Player(object):

    def __init__(self, name, age, race, hp, max_attack, country):
        self.chance = random.randrange(0, 101)
        self.surrender = False
        self.name = name
        self.age = age
        self.race = race
        self.hp = hp
        self.maxHP = hp
        self.maxAttack = max_attack
        self.country = country

    def get_damage(self, damage):
        self.hp -= damage

        return f"{self.name} тебе нанесли урон в размере {damage} едениц урона. \nУ тебя осталось {self.hp} хп"

    def dead(self):
        if self.hp <= 0 and not self.surrender:
            return True
        elif self.hp > 0 and not self.surrender:
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
                return f"Поздравляю. \nВы увеличили свое здоровье на {heal}"

            elif self.chance > 0 and self.chance != 100 and can_u_heal >= 0.5:
                heal = random.randrange(1, self.maxHP - self.hp)
                self.hp += heal
                self.chance = 0
                return f"Поздравляю. \nВы увеличили свое здоровье на {heal}"
            elif can_u_heal < 0:
                damage = random.randrange(1, self.maxHP - self.hp)
                self.hp -= damage
                self.chance += random.randrange(5, 21)
                return f"О НЕЕЕЕТ. \nТы получил мать его критический промах. \nШприц порвал твою артерию. \nТы полуил {damage} урона"

            else:
                self.chance += random.randrange(1, 21)
                return 'Сегодня не твой день. \nЯ думаю в следущий раз повезет'

        elif self.hp == self.maxHP:
            return 'Вы и так здоровы. \nЖаль, но вы пропускаете ход'

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
                return  self.race
            case _:
                return  'ХАХАХАХАХАХХА БАГ БАГ, НУ ВЫ ВИДЕЛИ. ТУТ БАГ'


    def shutdown(self):
        kill = self.maxHP * 10
        self.surrender = True
        self.hp -= kill
        return 'Never gonna give u up'

curr_player = None

def create_player():
    global curr_player
    player_name = input('Как вас зовут странник - ')
    player_age = int(input('Сколько лет вашему герою - '))
    player_race = input('Какая ваша расса - ')
    player_country = input('Откуда вы - ')

    player_hp = random.randrange(1, 400)

    player_maxAttack = random.randrange(1, 120)

    curr_player = Player(player_name, player_age, player_race,
                player_hp, player_maxAttack, player_country)

    return curr_player
