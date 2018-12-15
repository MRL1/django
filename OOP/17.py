# 请写一个小游戏，人狗大站，
# 2个角色，人和狗，游戏开始后，生成2个人，3条狗，互相混战，
# 人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。
class Role():
    '''
    总结：
        1.人和狗都有攻击的动作，但是他们的初始状态不同（血量和攻击力），所以可以建一个父类将攻击的方式放在里面
        2.相同的都可以放在父类里，子类自有的属性放在子类中定义
    '''

    def attack(self, enemy):
        # 血量=满血量-攻击力
        enemy.life_value -= self.agressivity


class People(Role):
    agressivity = 10  # 攻击力
    life_value = 100  # 满血量

    def __init__(self, name):
        self.name = name


class Dogs(Role):
    agressivity = 15
    life_value = 80

    def __init__(self, name):
        self.name = name


p1 = People('tom')
p2 = People('sem')

d1 = Dogs('niker')
d2 = Dogs('geeker')
d3 = Dogs('chaox')

print(p1.agressivity)

print(p1.life_value)
#p1.attack(d1)
d2.attack(p1)
print(p1.life_value)
