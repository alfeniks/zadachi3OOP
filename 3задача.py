import random

class Warrior:
    def __init__(self, name):
        """Инициализация бойца с именем и здоровьем 100."""
        self.name = name
        self.health = 100

    def attack(self, opponent):
        """Метод для атаки на другого бойца."""
        opponent.health -= 20
        print(f"{self.name} атакует! У {opponent.name} осталось {opponent.health} здоровья.")

    def is_alive(self):
        """Проверка, жив ли боец."""
        return self.health > 0


# Создаем два экземпляра класса Warrior
warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

# Сражение до тех пор, пока кто-то не победит
while warrior1.is_alive() and warrior2.is_alive():
    # Случайным образом выбираем, кто атакует
    attacker, defender = random.choice([(warrior1, warrior2), (warrior2, warrior1)])
    
    # Атакуем
    attacker.attack(defender)

# Определяем победителя
if warrior1.is_alive():
    print(f"{warrior1.name} победил!")
else:
    print(f"{warrior2.name} победил!")
