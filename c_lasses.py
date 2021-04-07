import random

# Шаблон
class NPC(object):
    healthPoint = 100
    x_coord = random.randint(0, 64)
    y_coord = random.randint(0, 64)
    mob_name = 'Name 1'
    skin = 567

    def __init__(self, health=100):
        self.healthPoint = health

    def hit_damage(self, value):
        self.healthPoint = self.healthPoint - value


first_npc = NPC(120)
second_npc = NPC(500)

third_npc = second_npc

is_equal = first_npc == second_npc
is_equal2 = third_npc == second_npc

first_hp = first_npc.healthPoint
second_hp = second_npc.healthPoint

first_npc.hit_damage(70)
second_npc.hit_damage(250)


first_hp_2 = first_npc.healthPoint
second_hp_2 = second_npc.healthPoint

second_npc.healthPoint = 1000

second_hp_3 = second_npc.healthPoint

print()
