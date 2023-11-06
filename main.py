import random

class Hero:
    def __init__(self, unit_name, hitpoint, armor, heal, attack):
        self.unit_name = unit_name
        self.hitpoint = hitpoint
        self.armor = armor
        self.heal = heal
        self.attack_amount = attack

    def __str__(self):
        return "{}\nКоличество здоровья {}\nКоличество брони {}\nУмение исцелять здоровье союзника {}\nАттака {}".format(
            self.unit_name, self.hitpoint, self.armor, self.heal, self.attack_amount)

    def choose_monster(self, length):
        number = random.randint(0, length - 1)
        random_monster = monsters[number]
        return random_monster

    def choose_hero(self, length):
        number = random.randint(0, length - 1)
        random_hero = heroes[number]
        return random_hero


class Attacker(Hero):
    def attack(self, other):
        print(self.unit_name, "атакует")
        other.hitpoint = other.hitpoint - self.attack_amount + other.armor


class Tank(Hero):
    def attack(self, other):
        print(self.unit_name, "атакует")
        other.hitpoint = other.hitpoint - self.attack_amount + other.armor


class Healer(Hero):
    def heal_ally(self, ally):
        ally.hitpoint = ally.hitpoint + self.heal

    def attack(self, other):
        print(self.unit_name, "не может атаковать")


attacker = Attacker("Арагорн", 200, 10, 0, 50)
tank = Tank("Гимли", 500, 20, 0, 30)
healer = Healer("Гендальф", 150, 5, 20, 20)
monster_1 = Attacker("Монстр 1", 100, 30, 0, 30)
monster_2 = Attacker("Монстр 2", 20, 20, 0, 30)
monster_3 = Attacker("Монстр 3", 100, 10, 0, 30)
monster_4 = Attacker("Монстр 4", 10, 10, 0, 30)
monster_5 = Attacker("Монстр 5", 50, 30, 0, 30)

heroes = [attacker, tank, healer]
monsters = [monster_1, monster_2, monster_3, monster_4, monster_5]
step = 1

while heroes and monsters:
    print("Ход атаки №:", step)


    for hero in heroes:
        if monsters:
            monster = hero.choose_monster(len(monsters))
            hero.attack(monster)
            print("Остаток здоровья", monster.unit_name, ":", monster.hitpoint)

            if monster.hitpoint <= 0:
                monsters.remove(monster)

    print("\n")
    step += 1

    if not monsters:
        break


    for monster in monsters:
        if heroes:
            hero = monster.choose_hero(len(heroes))
            monster.attack(hero)
            print("Остаток здоровья", hero.unit_name, ":", hero.hitpoint)

            if hero.hitpoint <= 0:
                heroes.remove(hero)

    print("\n")
    step += 1


if not heroes:
    print("Победа Монстров")
elif not monsters:
    print("Победа героев")
