class Monster:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self,character):
        character.hp -= self.damage

class Slime(Monster):
    def __init__(self,name,hp,damage,poison):
        super().__init__(name,hp) #부모의 생성자
        self.poison = poison #자기의 생성자
    def sprayPoison(self, character):
        character.hp -= self.damage + self.poison

#kim = Character()
a = Slime('귀여운 슬라임',50,30,5)
#a.attack(kim)
#a.sprayPoison(kim)















