class Animal:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def info(self):
        print(f'Age: {self.age}')
        print(f'Name: {self.name}')
        print(f'Speed: {self.speed}')


class Tiger(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, speed)

    def show_info(self):
        super().show_info()
        print('i love meat')
        print('tiger')


class Crocodile(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, speed)

    def info(self):
        super().info()
        print('i love water')
        print('crocodile')


class Kangoroo(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, speed)

    def info(self):
        super().info()
        print('i like jump')
        print('Kangoroo')


tiger = Tiger('alex', 12, 24)
tiger.info()
crocodile = Crocodile('sasha', 20, 20)
crocodile.info()
kangoroo = Kangoroo('pasha', 13, 25)
kangoroo.info()