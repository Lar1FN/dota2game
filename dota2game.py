import random

end = '''
 ________ __    __ ________        ________ __    __ _______
|        |  \  |  |        \      |        |  \  |  |       |
 \$$$$$$$| $$  | $| $$$$$$$$      | $$$$$$$| $$\ | $| $$$$$$$|
   | $$  | $$    $| $$  \         | $$  \  | $$$$\ $| $$  | $$
   | $$  | $$$$$$$| $$$$$         | $$$$$  | $$\$$ $| $$  | $$
   | $$  | $$  | $| $$_____       | $$_____| $$ \$$$| $$__/ $$
    \$$   \$$   \$$\$$$$$$$$       \$$$$$$$$\$$   \$$\$$$$$$$
    '''

start = '''
..  ..  ........... ... ..................  ..  ......  ..  ..............  ..................  ..
  ..  .:!YYJJJJJYY7:?Y!.7YJJYYYJYYYJYYYY^ ..  :^JYYJ^...  .^YJJ?:~YYYYJJY?:. !YJYYYYJJJYYYJYY!..  ..
..  ..!JY5Y5YYYYYY5?Y5? ?555YYY555YY55Y5!   :^JJY5Y5YY^... ~5YJ5JJYYYY55Y5Y?.7555YYY555YYY5557  ..
  ..  !JPBBYY5Y7YJY5BJ?.J#B5?~5#BY?!5BPJ! :^JJYP##PJY55Y:  ~GBPY?J77!JBBY5YY.?#B5J~Y#BYJ~YBGJ?..  ..
..  ...^7PB55J55J7YGGJ7 ?5?^:.5#GJ7 :~YY~.JJYP##PJ!!YJJ5!^ ~B#PY5555Y5J5#BJJ.75J^: J#B?J :~JJ7  ..
  ..  :~~!JGGP5J55J7~:...:.  .5#GJ7   :^.:YP##GJ?!~~!?JY5Y:~B#PYYYJJYY5#YYPJ..::  .J#BJJ   :^...  ..
..  . !555Y7JPGPPJ55J~^ .    .5#GJ7 ..   :P###PJ5555JYPPY5:~B#5Y~::::7PGPPJY..  .  J#BJJ     .  ..
 .... 7PGJ55Y7YGGPPJ5P? ....~!5#GJJ!: .. :P##BPYJJJJY5B#YY^~B#YY7~.  ^7J##JJ. .. ^!Y#BJY!^..........
..... 7BGJYJ555JP##PJJ! ....JYG#BJ5P! .. :P#G?5P!..~Y5B#YY^~B#YY55:  7JP##JY.... ?JG##J5P? .........
..... ^?!.~?????YYJ?!. ... .!JYYY?7?~ ....7YY?7?^  :7YYY??.:JYJ???.  ~?YYY?!.....~?YYY???! ........
  ..  ..  ......          .      ...  .      ...  .       ..  ..   .      .    .      ..  ..  ..  ..
..  ..  ..  ..   ~7777777~.!777^ .  . .7777: .  ..:7777: .  . ^777!.^777777777! ~777~.  ..  ..  ..
  ..  ..  ..  .~7JYYYYYY5J7JYY5!  ...77JJJYJ?:..  ^YYY5??:..^7?YYYY.~YYYYYYYYYY7JYYY? ..  ..  ..  ..
..  ..  ..  .. 7J5PPYJ7!7JJ5PY?7 ..7??J55Y?JYJ?: .^5PJ?JYJ????5PP?J.~YJYJ?7777JJ5P5?J.  ..  ..  ..
  ..  ..  ..  .?PGYY!^...~?5YJ7^.???J5PPYJ7J?J5~. ^PGGPJ?YY?5PGGG?J:~?5?JJJJJJJ7Y5Y!^ ..  ..  ..  ..
..  ..  ..  .. ?GP7?. .?JJJYYYJ~.?J5PPYJ!^:!???YJ:^PGGGPPPPPGGPPG?J.!PGJJYJJJYJ ~7~...  ..  ..  ..
  ..  ..  ..  .?GP7J:..?JJJJJJY!.YPGG57YJYYJJYJJY^^PG5J77PG5J!?PG?J:!PGGPYJ!~~~:7JJY7 ..  ..  ..  ..
..  ..  ..  .. ?GP7YY?:~7JJ5GY7!.YGGG5?JJJJ?YPGJJ~:PGJJ!^~~^~^7PG?J.!PGYJ7~:::7JJJJJJ.  ..  ..  ..
  ..  ..  ..  .7PPYY?YYY?JJPG5?7.YGP?Y57^^!YYPGJJ^^PGY?YY:  ~JYPG?J:!GG?JYYYYJJJPGP7J...  ..  ..  ..
..  ..  ..  .. .:?P5?J??7!^J5Y?~.JP5??J~  :?Y55JJ^:Y5Y??J^  ~?555??.~55J?????!?^?55?7.  ..  ..  ..
  ..  ..  ..  .. .:::::::. .:::. .:::::.  .:::::: .:::::. ...:::::...:::::::::. .:::. ..  ..  ..  ..

'''
class Hero:
    def __init__(self, name, attack, defense, hp):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = 25

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage > 0:
            enemy.hp -= damage
            print(f"{self.name} наносит {damage} единиц урона {enemy.name}")
        else:
            print(f"{self.name} не наносит урона {enemy.name}")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (атака: {self.attack}, защита: {self.defense}, здоровье: {self.hp})"


class Game:
    def __init__(self, player_hero, computer_hero):
        self.player_hero = player_hero
        self.computer_hero = computer_hero

    def play(self):
        print(start)
        print(f"Вы играете за {self.player_hero}")
        print(f"Компьютер играет за {self.computer_hero}")

        while self.player_hero.is_alive() and self.computer_hero.is_alive():
            print(f"Ход {self.player_hero.name}")
            self.player_turn()
            if not self.computer_hero.is_alive():
                break
            print(f"Ход {self.computer_hero.name}")
            self.computer_turn()

        if self.player_hero.is_alive():
            print("Вы победили!")
        else:
            print("Вы проиграли!")

    def player_turn(self):
        while True:
            print("Выберите действие:")
            print("1. Атаковать")
            print("2. Защищаться")
            choice = input("Введите номер действия: ")
            if choice == "1":
                self.player_hero.attack_enemy(self.computer_hero)
                break
            elif choice == "2":
                self.player_hero.defense += 2
                print(f"{self.player_hero.name} укрепляет свою защиту")
                break
            else:
                print("Неправильный выбор, повторите попытку")

    def computer_turn(self):
        choice = random.choice(["attack", "defense"])
        if choice == "attack":
            self.computer_hero.attack_enemy(self.player_hero)
        else:
            self.computer_hero.defense += 2
            print(f"{self.computer_hero.name} укрепляет свою защиту")


heroes = ["Anti-Mage", "Axe", "Bane", "Bloodseeker", "Crystal Maiden", "Drow Ranger", "Tinker", "Juggernaut",
          "Mirana", "Shadow Fiend"]

player_hero = Hero(random.choice(heroes), random.randint(5, 10), random.randint(1, 5), 100)
computer_hero = Hero(random.choice(heroes), random.randint(5, 10), random.randint(1, 5), 100)

game = Game(player_hero, computer_hero)
game.play()
print(end)
