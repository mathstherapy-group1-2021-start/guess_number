# будем считать площади фигур разными способами

def area_circe(radius):
    "radius это радиус"
    return 3.14 * radius * radius


def perimetr_circle(radius):
    "radius это радиус"
    return 2 * 3.14 * radius


def area_rectangle(a, b):
    "a и b это стороны"
    return a * b


def perimetr_rectangle(a, b):
    "a и b это стороны"
    return 2 * (a + b)


def area_square(a):
    "a это сторона"
    return a * a


def perimetr_square(a):
    "a это сторона"
    return 4 * a


ac = area_circe(1.0)
pr = perimetr_rectangle(2, 4)

print(ac)
print(pr)


class Shape:
    def area(self):
        pass

    def perimetr(self):
        pass

    def name():
        return 'shape'


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimetr(self):
        return 2 * 3.14 * self.radius

    def name():
        return 'circle'


class Rect(Shape):
    def __init__(self, a, b):
        "a и b это стороны"
        self.a = a
        self.b = b

    def area(self):
        return area_rectangle(a=self.a, b=self.b)

    def perimetr(self):
        return 2 * (self.a + self.b)

    def name():
        return 'rectangle'


class Square(Rect):
    def __init__(self, a):
        super().__init__(a, a)

    def radius_of_inner_circle(self):
        return self.a / 2

    def name():
        return 'square'


print("--- circle ---")
c1 = Circle(radius=1)
c2 = Circle(radius=2)

print(type(c1))
print(isinstance(c1, Rect))
print(isinstance(c1, Circle))
print(isinstance(c1, Shape))
print(c1.radius)
print(c2.radius)

print(c1.area())
print(c2.area())

print("\n--- rect ---")
r1 = Rect(a=1, b=2)
r2 = Rect(a=3, b=5)

print(type(r1))
print(isinstance(r1, Rect))
print(isinstance(r1, Circle))
print(isinstance(r1, Shape))
print(r1.area())
print(r2.area())

print("\n--- square ---")
s1 = Square(a=2)
print(s1.area())
print(s1.radius_of_inner_circle())

print(s1.b)


print('\n--- comfort!! ---')

shapes = [Circle(radius=1), Circle(radius=3), Rect(a=2, b=6), Square(a=3)]

for shape in shapes:
    print("\n")
    print('area = %s' % shape.area())
    if isinstance(shape, Rect):
        print('perimetr = %s' % shape.perimetr())


# class methods
print('\n--- class methods ---')

print(Shape.name())
print(Circle.name())
print(Rect.name())
print(Square.name())

# сделать иерархию классов, которая будет представлять животных, птиц и рыб
# классы должны корректно показывать способ перемещения и звуки, которые издаёт животное, птиц, или рыба
# возьмём кошку, собаку, чайку, змею, рыбу
# базовый класс такой
#


class Animal:
    def say(self):
        "возвращает строку с звуком животного (напр. мяу, гав)"
        pass

    def move(self):
        "возвращает строку со способом передвижения животного (например ползёт, летает)"
        pass


class WalkingAnimal(Animal):
    def move(self):
        return "walk"


class WalkingDomesticAnimal(WalkingAnimal):
    def __init__(self, name):
        self.name = name


class Seagull(Animal):
    def say(self):
        return "whatever seagull says"

    def move(self):
        return "fly"


class Snake(Animal):
    def say(self):
        return "hiss"

    def move(self):
        return "crawl"


class Cat(WalkingDomesticAnimal):
    def say(self):
        return "meow"


class Dog(WalkingDomesticAnimal):
    def say(self):
        return "woof"


class Fox(WalkingAnimal):
    def say(self):
        return "I\'m hungry"


print('\n\n----- animals -----')

# barsik = Cat(name='Barsik')
# print(barsik.name)
# print(barsik.say())
# print(barsik.move())

# murzik = Cat(name='Murzik')
# print(murzik.name)
# print(murzik.say())
# print(murzik.move())


# bobik = Dog(name='Bobik')
# print(bobik.name)
# print(bobik.say())
# print(bobik.move())

# barbos = Dog(name='Barbos')
# print(barbos.name)
# print(barbos.say())
# print(barbos.move())

# ludvig = Fox()
# print(ludvig.say())
# print(ludvig.move())

animals = [Seagull(), Cat('murzik'), Dog('bobik'), Fox(), Snake()]
for animal in animals:
    if (isinstance(animal, WalkingDomesticAnimal)):
        print(animal.name)
    print(animal.say())
    print(animal.move())
    print('\n')


numbers = [1.1, 2.22, 3.333, 4.4444]
for numer in numbers:
    print('%s\tmeters' % numer)
