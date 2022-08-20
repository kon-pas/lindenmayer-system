from Lsystem import *


if __name__ == "__main__":
    rule_1 = Rule('F', 'F+G')
    rule_2 = Rule('G -> GGFG')
    rules = Rules(rule_1, rule_2)
    rules.add_rule(Rule('G', 'G-G'))
    rules.remove_rule(2)
    system = Lsystem(
        rules=rules,
        distance=50,
        angle=38,
        start='F',
        steps=10
    )
    system.define_action(symbol='G', distance=50, angle=-5)
    system.commit("Mój L-system!")
    system.draw()

    # init_default_systems()
    # print_systems()
    # system = get_system(4)
    # system.draw()
  







