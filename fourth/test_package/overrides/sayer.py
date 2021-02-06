from test_package import fourth_package

# Одинаковые названия методов
class SayerA:
    def say(self):
        fourth_package.output("a")


class SayerB:
    def say(self):
        fourth_package.output("b")


class SayerAB(SayerA, SayerB):
    pass


class SayerBA(SayerB, SayerA):
    pass
