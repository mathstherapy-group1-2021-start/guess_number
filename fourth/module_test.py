from test_package.classic.sit_and_lay import SitterLayer
from test_package.overrides.sayer import SayerAB


ab = SayerAB()
ab.say()

sl = SitterLayer()
sl.sit()
sl.lay()