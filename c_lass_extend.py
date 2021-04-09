from c_lasses import NPC
#  TODO:
# Приветси пример множественного наследования

class NPC2(NPC):
    def heal(self, value, other_value):
        super(value)
        self.healthPoint = self.healthPoint + value

    def hit_damage(self, value):
        self.healthPoint = self.healthPoint - value * 2


first_npc = NPC2()

current_hp = first_npc.healthPoint

first_npc.hit_damage(5)
after_hit_hp = first_npc.healthPoint

first_npc.heal(5)
after_heal_hp = first_npc.healthPoint


print()