from variables import *
from Rule import *


class Rules:
    def __init__(self, *args):
        self.production_rules = []
        for char in special_characters:
            self.production_rules.append(Rule(f'{char} -> {char}'))
        for arg in args:
            # print(arg)
            if not isinstance(arg, Rule):
                raise TypeError('That is not a Rule')
            self.production_rules.append(arg)
        for rule in self.production_rules:
            if len(rule.get_left()) > 1:
                raise TypeError('Left production consists of too many symbols')
            if terminals.index(rule.get_left()) == -1:
                raise TypeError('Left production must consist of a valid terminal')

    def __str__(self):
        text = ''
        arr = self.production_rules[2:]
        for index, production_rule in enumerate(arr):
            text += f'{index+1}. {production_rule}\n'
        return text

    def extract(self):
        for rule in self.get_rules():
            rule.extract()

    def get_rules(self):
        return self.production_rules

    def add_rule(self, rule):
        if type(rule) is not Rule:
            raise TypeError('Rule must be an instance of class Rule')
        else:
            self.production_rules.append(rule)

    def get_rules_num(self):
        return len(self.get_rules())

    def remove_rule(self, index):
        index = index - 1 + 2
        if type(index) is not int:
            raise TypeError('Index must be integer')
        if index < 0 or index > self.get_rules_num() - 1:
            raise ValueError(f'Invalid index range, choose a number between 1 and {self.get_rules_num()}')
        del self.get_rules()[index]

    def get_production(self, symbol):
        for rule in self.get_rules():
            if rule.get_left() == symbol:
                return rule.get_right()
        return None
