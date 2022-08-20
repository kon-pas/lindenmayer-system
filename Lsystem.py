import turtle
from Rules import *
from variables import *


class Lsystem:
    def __init__(self, **kwargs):
        self.angle = kwargs.get('angle')
        if self.angle is None:
            self.angle = DEFAULT_ANGLE
        self.start = kwargs.get('start')
        if self.start is None:
            self.start = terminals[0]
        self.distance = kwargs.get('distance')
        if self.distance is None:
            self.distance = DEFAULT_DISTANCE
        self.rules = kwargs.get('rules')
        if self.rules is None:
            self.rules = Rules()
        self.name = 'Nameless'
        self.steps = kwargs.get('steps')
        if self.steps is None:
            self.steps = DEFAULT_STEPS
        self.actions = {
            '+': {'forward': None, 'angle': -1 * self.angle},
            '-': {'forward': None, 'angle': self.angle},
        }
        for terminal in terminals:
            if terminal not in special_characters:
                self.define_action(symbol=terminal, distance=self.distance)

    def set_angle(self, angle):
        if type(angle) is not int:
            raise TypeError('Angle must be integer')
        else:
            self.angle = angle

    def get_angle(self):
        return self.angle

    def set_start(self, start):
        if terminals.index(start) == -1:
            raise TypeError('Starting symbol must be a terminal')
        else:
            self.start = start

    def get_start(self):
        return self.start

    def set_distance(self, distance):
        if type(distance) is not int:
            raise TypeError('Distance must be integer')
        if distance < 0:
            raise TypeError('Distance cannot be negative')
        else:
            self.distance = distance

    def get_distance(self):
        return self.distance

    def set_rules(self, rules):
        if type(rules) is not Rules:
            raise TypeError('Rules must be an instance of class Rules')
        else:
            self.rules = rules

    def get_rules(self):
        return self.rules

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_steps(self):
        return self.steps

    def set_steps(self, steps):
        self.steps = steps

    def define_action(self, **kwargs):
        symbol = kwargs.get('symbol')
        if terminals.index(symbol) == -1:
            raise ValueError('No such terminal found')
        else:
            self.actions[symbol] = {'distance': kwargs.get('distance'), 'angle': kwargs.get('angle')}

    def commit(self, name):
        self.set_name(name)
        systems.append(self)

    def draw(self):
        def flatten(seq):
            def _flatten(_seq):
                for element in _seq:
                    if isinstance(element, (list, tuple)):
                        _flatten(element)
                    else:
                        flat.append(element)
            flat = []
            _flatten(seq)
            return flat

        def encourage_turtle(symbol):
            if self.actions.get(symbol) is not None:
                distance = self.actions.get(symbol).get('distance')
                if distance is not None:
                    t.forward(distance)
                angle = self.actions.get(symbol).get('angle')
                if angle is not None:
                    t.right(angle)

        t = turtle.Turtle()
        turtle.hideturtle()
        t.hideturtle()
        drawing_area = turtle.Screen()
        drawing_area.setup(width=1920, height=1080)

        self.rules.extract()
        word = [self.start]
        for _ in range(self.get_steps()):
            new_word = word
            for i in range(len(word)):
                new_word[i] = self.rules.get_production(word[i])
            word = flatten(new_word)
        turtle.tracer(0, 0)
        while word:
            encourage_turtle(word.pop(0))
        turtle.update()
        turtle.exitonclick()


def init_default_systems():
    Lsystem(
        start='F',
        distance=11,
        angle=90,
        rules=Rules(Rule('F -> F+F-F-F+F')),
        steps=4
    ).commit('Koch curve')
    Lsystem(
        start='F',
        distance=2,
        angle=120,
        rules=Rules(Rule('F -> F-G+F+G-F'), Rule('G -> GG')),
        steps=8
    ).commit('Sierpinski triangle')
    Lsystem(
        start='F',
        distance=2,
        angle=60,
        rules=Rules(Rule('F -> G-F-G'), Rule('G -> F+G+F')),
        steps=8
    ).commit('Sierpinski triangle using a Sierpinski arrowhead curve')
    Lsystem(
        start='F',
        distance=10,
        angle=90,
        rules=Rules(Rule('F -> F+G'), Rule('G -> F-G')),
        steps=12
    ).commit('Dragon curve')


def print_systems():
    if systems:
        for index, system in enumerate(systems):
            print(f'{index+1}. {system.get_name()}')
    else:
        print('No L-Systems saved yet!')


def get_system(index):
    if type(index) is not int:
        raise TypeError('Index must be type of integer')
    if index < 1 or index > len(systems):
        raise ValueError(f'Invalid index range, choose a number between 1 and {len(systems)}')
    return systems[index-1]
