import random

class Warrior:
    def __init__(self, name):
        """Инициализация бойца с именем, здоровьем, броней и выносливостью."""
        self.name = name
        self.health = 100
        self.armor = 50
        self.endurance = 50

    def attack(self, opponent):
        """Метод атаки: атакующий теряет 10 очков выносливости, противник теряет здоровье и броню."""
        if self.endurance > 0:
            damage = random.randint(10, 30)
            opponent.health -= damage
            self.endurance -= 10
            print(f"{self.name} атакует! У {opponent.name} теряет {damage} здоровья. {self.name} теряет 10 выносливости.")
        else:
            print(f"{self.name} атакует с ослаблением из-за низкой выносливости!")
            damage = random.randint(0, 10)
            opponent.health -= damage
            print(f"{self.name} наносит ослабленный урон! У {opponent.name} теряет {damage} здоровья.")

    def defend(self, opponent):
        """Метод защиты: защитник теряет здоровье и броню в зависимости от атаки."""
        if self.armor > 0:
            damage_health = random.randint(0, 20)
            damage_armor = random.randint(0, 10)
            self.health -= damage_health
            self.armor -= damage_armor
            print(f"{self.name} защищается! Теряет {damage_health} здоровья и {damage_armor} брони.")
        else:
            # Если броня закончилась, только здоровье
            damage_health = random.randint(10, 30)
            self.health -= damage_health
            print(f"{self.name} защищается! Броня закончилась, теряет {damage_health} здоровья.")

    def is_alive(self):
        """Проверка, жив ли боец (здоровье больше 10)."""
        return self.health > 10


# Создаем два экземпляра класса Warrior
warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

# Игра продолжается, пока кто-то не проиграет
while warrior1.is_alive() and warrior2.is_alive():
    # Случайным образом выбираем действия для обоих воинов
    action1 = random.choice(["attack", "defend"])
    action2 = random.choice(["attack", "defend"])

    if action1 == "attack" and action2 == "attack":
        # Оба атакуют
        warrior1.attack(warrior2)
        warrior2.attack(warrior1)
    elif action1 == "attack" and action2 == "defend":
        # Воин 1 атакует, воин 2 защищается
        warrior1.attack(warrior2)
        warrior2.defend(warrior1)
    elif action1 == "defend" and action2 == "attack":
        # Воин 1 защищается, воин 2 атакует
        warrior1.defend(warrior2)
        warrior2.attack(warrior1)
    else:
        # Оба защищаются
        warrior1.defend(warrior2)
        warrior2.defend(warrior1)

    # Печатаем состояние здоровья после хода
    print(f"{warrior1.name}: здоровье = {warrior1.health}, броня = {warrior1.armor}, выносливость = {warrior1.endurance}")
    print(f"{warrior2.name}: здоровье = {warrior2.health}, броня = {warrior2.armor}, выносливость = {warrior2.endurance}")

# Конец игры
if warrior1.is_alive():
    print(f"{warrior1.name} победил!")
else:
    print(f"{warrior2.name} победил!")

# Спрашиваем, убить ли противника
kill = input(f"Убить {warrior2.name} (если победил {warrior1.name}) или {warrior1.name} (если победил {warrior2.name})? (да/нет): ").lower()

if kill == "да":
    print(f"{warrior1.name if warrior1.is_alive() else warrior2.name} решает убить противника.")
else:
    print(f"{warrior1.name if warrior1.is_alive() else warrior2.name} решил пощадить противника.")
git init