# Базовый класс Животное
class Animal:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Надклассы для каждой группы животных
class TerrestrialAnimal(Animal):  # Наземные животные
    pass

class AquaticAnimal(Animal):  # Водные животные
    pass

class AerialAnimal(Animal):  # Воздушные животные
    pass


class Mammal(TerrestrialAnimal):
    pass


class Tiger(Mammal):
    def move(self):
        print("Тигр бежит")

class Elephant(Mammal):
    def move(self):
        print("Слон идет")

class Giraffe(Mammal):
    def move(self):
        print("Жираф шествует")


class Bird(AerialAnimal):
    pass

# Конкретные классы птиц
class Penguin(Bird, TerrestrialAnimal, AquaticAnimal):  # Пингвин также может быть наземным и водным животным
    def move(self):
        print("Пингвин ходит и плавает")

class Duck(Bird, AquaticAnimal):  # Утка также может быть водным животным
    def move(self):
        print("Утка летает и плавает")


class Insect(TerrestrialAnimal):
    pass

# Конкретные классы насекомых
class Ant(Insect):
    def move(self):
        print("Муравей бегает")

class Butterfly(Insect, AerialAnimal):  # Бабочка также может быть воздушным животным
    def move(self):
        print("Бабочка летает")


class Fish(AquaticAnimal):
    pass

# Конкретные классы рыб
class Salmon(Fish):
    def move(self):
        print("Лосось плывет")

class Shark(Fish):
    def move(self):
        print("Акула плывет быстро")


class Reptile(TerrestrialAnimal):
    pass

# Конкретные классы рептилий
class Snake(Reptile):
    def move(self):
        print("Змея ползет")

class Crocodile(Reptile, AquaticAnimal):  # Крокодил также может быть водным животным
    def move(self):
        print("Крокодил ходит и плавает")


def main():
    animals = [
        Tiger(),
        Elephant(),
        Giraffe(),
        Penguin(),
        Duck(),
        Ant(),
        Butterfly(),
        Salmon(),
        Shark(),
        Snake(),
        Crocodile()
    ]

    for animal in animals:
        animal.move()

if __name__ == "__main__":
    main()



