import random
import os.path

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
            case 'maxAttack':
                return self.maxAttack
            case 'maxHP':
                return self.maxHP
            case 'race':
                return self.race
            case _:
                return 'ХАХАХАХАХАХХА БАГ БАГ, НУ ВЫ ВИДЕЛИ. ТУТ БАГ'


    def shutdown(self):
        kill = self.maxHP * 10
        self.surrender = True
        self.hp -= kill
        return 'Never gonna give u up'

curr_player = None

def create_player(returning=1):
    global curr_player
    player_name = input('Как вас зовут странник - ')
    player_age = int(input('Сколько лет вашему герою - '))
    player_race = input('Какая ваша расса - ')
    player_country = input('Откуда вы - ')

    player_hp = random.randrange(1, 400)

    player_maxAttack = random.randrange(1, 120)

    curr_player = Player(player_name, player_age, player_race,
                player_hp, player_maxAttack, player_country)

    if returning == 1:
        return curr_player


def save_for_later(player):
    count = 0
    path = 'characters/'
    if not os.path.exists(path):
        os.mkdir(path)

    name = player.get_stat('name')
    race = player.get_stat('race')
    age = player.get_stat('age')
    attack = player.get_stat('maxAttack')
    hp = player.get_stat('maxHP')
    country = player.get_stat('country')
    while os.path.isfile(path + 'p' + str(count) + '.txt'):
        count+=1

    with open(path + 'p' + str(count) + '.txt' , 'a', encoding='utf-8') as f:
        f.write(name)
        f.write('\n' + race)
        f.write('\n' + str(age))
        f.write('\n' + country)
        f.write('\n' + str(attack))
        f.write('\n' + str(hp))
        f.write('\n' + str(player))


def read_player_file(player):
    with open(player) as f:
        lines = f.readlines()
        lines = list(map(lambda each:each.strip('\n'), lines))
        if len(lines) == 7:
            try:
                curr_player = Player(name=lines[0], age=int(lines[2]), race=lines[1], hp=int(lines[5]), max_attack=int(lines[4]), country=lines[3])
                return curr_player
            except ValueError:
                return 'Ваш файл персонажа повреждён. Не верный тип данных'
        else:
            return f'У вас поврежден файл персонажа. Нет достающих типов данных'