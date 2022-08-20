class Rule:
    def __init__(self, *args):
        self.arrow = '->'
        for arg in args:
            if not type(arg) is str:
                raise TypeError('All arguments should be type of string')
        if len(args) == 1:
            production_rule = args[0]
            arrow_position = production_rule.find(self.arrow)
            if arrow_position == -1:
                raise ValueError('Production rule does not contain an arrow')
            elif arrow_position != -1:
                self.left = production_rule[:arrow_position].replace(" ", "")
                self.right = production_rule[arrow_position + len(self.arrow):].replace(" ", "")
        if len(args) == 2:
            self.left = args[0].replace(" ", "")
            self.right = args[1].replace(" ", "")

    def __str__(self):
        return f'{self.left} -> {self.right}'

    def print(self):
        print(str(self))

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def set_both(self, left, right):
        self.left = left
        self.right = right

    def get_both(self):
        return self.left, self.right

    def extract(self):
        if type(self.get_right()) is str:
            self.set_right(list(self.get_right()))
