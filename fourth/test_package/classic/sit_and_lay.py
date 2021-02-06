from ..fourth_package import output

# разные названия методов
class Sitter:
    def sit(self):
        output("sit")


class Layer:
    def lay(self):
        output("lay")


class SitterLayer(Sitter, Layer):
    pass
