import random
import os
import Enemy_config as En_conf
import Player_config as Pl_conf



last_action_player = 'Пока ничего не произошло'

last_action_monster = 'Пока ничего не произошло'









monster = En_conf.create_monster()

player = Pl_conf.create_player()

ruletka = random.randrange(2)
first_move = None
second_move = None

def whoIsFirst():
    global first_move,second_move
    if ruletka == 1:
        first_move = 'Enemy'
        second_move = 'Player'
    elif ruletka == 0:
        first_move = 'Player'
        second_move = 'Enemy'



step = 0


def start_battle(main_hero, enemy_battle):
    global last_action_player, last_action_monster, first_move, second_move, step, end
    whoIsFirst()
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

# пример работы
# status = start_battle(player, monster)
#
# match status:
#     case 1:
#         input('Воу ты победил, Нажми Enter  для завершения')
#
#     case 2:
#         input('Чтож раз никто так никто. Нажми Enter')
#
#     case 0:
#         input('Я разачорован. Нажми Enter ')