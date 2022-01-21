import random
import os
import Enemy_config as En_conf

last_action_player = 'Пока ничего не произошло'

last_action_monster = 'Пока ничего не произошло'


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
                return f"О ДАААА. \n{self.name} поулчило чертов критический промах. \nШприц порвал его вены. \nОНо полуил {damage} урона"

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


class Player(object):

    def __init__(self, name, age, race, hp, MaxAttack, country):
        self.chance = random.randrange(0, 101)
        self.surrender = False
        self.name = name
        self.age = age
        self.race = race
        self.hp = hp
        self.maxHP = hp
        self.maxAttack = MaxAttack
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


random.shuffle(En_conf.name)

random.shuffle(En_conf.race)

random.shuffle(En_conf.country)

monster = Enemy(random.choice(En_conf.name), En_conf.age,
                random.choice(En_conf.race), En_conf.hp, En_conf.monster_maxAttack, random.choice(En_conf.country))

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
second_move = None
if ruletka == 1:
    first_move = 'Enemy'
    second_move = 'Player'
elif ruletka == 0:
    first_move = 'Player'
    second_move = 'Enemy'


step = 0


def start_battle(main_hero, enemy_battle):
    global last_action_player, last_action_monster, first_move, second_move, step, end

    end = 'Maybe'

    while True:

        enemy_move = random.randrange(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            f"\nВаш враг - {enemy_battle.get_stat('name')} \nРасса врага - {enemy_battle.get_stat('race')} \nСтрана врага - {enemy_battle.get_stat('country')} \nВозраст врага - {enemy_battle.get_stat('age')} \nЗдоровье врага - {enemy_battle.get_stat('hp')}")

        print(
            f"\n\nВы - {main_hero.get_stat('name')} \nВаша страна - {main_hero.get_stat('country')} \nВаш возраст - {main_hero.get_stat('age')} \nВаше здоровье - {main_hero.get_stat('hp')}")

        print(
            f"\n\n\nВаше последнее действие: \n{last_action_player}  \n\nПоследние действие врага : \n{last_action_monster}")

        if enemy_battle.dead() is True or main_hero.dead():
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nИгра окончена')

            if enemy_battle.dead() is True and main_hero.dead():
                print(
                    f"\n\nСегодня никто не ушел живым. \n{enemy_battle.get_stat('name')} и {main_hero.get_stat('name')} не вернуться домой")
                return 2

            elif enemy_battle.dead() is True and not main_hero.dead():
                print(
                    f"\n\nВы вернулись с поля битвы, оставив {enemy_battle.get_stat('name')} мертвым на поле сражения. \nДальнейшая судьба {main_hero.get_stat('name')} неизвестна")
                return 1

            elif not enemy_battle.dead() and main_hero.dead() is True:
                print(
                    f"\n\nВы сегодня не вернетесь домой. Вы проиграли.\n{enemy_battle.get_stat('name')} ушел в неизвестность, дальнейшая его судьба неизвестна. \nЧто будет с {main_hero.get_stat('name')} никто не знает")
                return 0


        elif end == 'Never gonna give u up':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nВы сдались как вы могли. \nВы поступили подло и дали {enemy_battle.get_stat('name')} возможность прославиться на вашем поражении."
                  f"\nПускай теперь все знают {main_hero.get_stat('name')}, как {main_hero.get_stat('race')} проиграл рассе {enemy_battle.get_stat('race')}")
            return 0

        elif step == 0 and first_move == 'Enemy':
            if enemy_battle.get_stat('hp') == enemy_battle.get_stat('maxHP') or enemy_move == 1:
                last_action_monster = main_hero.get_damage(enemy_battle.attack())
            elif enemy_battle.get_stat('hp') != enemy_battle.get_stat('maxHP') and enemy_move == 0:
                last_action_monster = enemy_battle.health()

            step += 1

        elif step == 0 and first_move == 'Player':
            action = int(input('\n1)Атака \n2)Вылечиться \n3)Сдаться \nЧто делаем - '))

            if action == 1:
                last_action_player = enemy_battle.get_damage(main_hero.attack())
            elif action == 2:
                last_action_player = main_hero.health()
            elif action == 3:
                end =  main_hero.shutdown()
            step += 1
        elif step == 1 and second_move == 'Player':
            action = int(input('\n1)Атака \n2)Вылечиться \n3)Сдаться \nЧто делаем - '))

            if action == 1:
                last_action_player = enemy_battle.get_damage(main_hero.attack())
            elif action == 2:
                last_action_player = main_hero.health()
            elif action == 3:
                end = main_hero.shutdown()
            step = 0

        if step == 1 and second_move == 'Enemy':
            if enemy_battle.get_stat('hp') == enemy_battle.get_stat('maxHP') or enemy_move == 1:
                last_action_monster = main_hero.get_damage(enemy_battle.attack())
            elif enemy_battle.get_stat('hp') != enemy_battle.get_stat('maxHP') and enemy_move == 0:
                last_action_monster = enemy_battle.health()

            step = 0


### 0 - игрок умер
### 1 -враг умер
### 2 - погибли оба

status = start_battle(player, monster)

match status:
    case 1:
        input('Воу ты победил, нажми любую кнопку для завершения')

    case 2:
        input('Чтож раз никто так никто. Нажми любую конпку')

    case 0:
        input('Я разачорован. Нажми любую кнопку')