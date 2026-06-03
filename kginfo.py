import random
class Kginfo:
    def __init__(self, name, health, kga_type, speed, moves):
        self.name = name
        self.max_health = health # backup for new game
        self.kga_type = kga_type
        self.health = health 
        self.speed = speed
        self.moves = moves
        #self.move_types = move_types 

        self.status = None #freeze, burn, paralysis, confusion
        self.attack_stage = 1.0
        self.defense_modifier = 1.0
        self.speed_modifier = 1.0
        self.crit_chance = 0 #stat boost perm

    # THIS IS THE STAGE MULTIPLIER --------
    def stage_multiplier(self, damage):
        stage_multipliers = {
                -4: 0.25, -3: 0.4, -2: 0.5, -1: 0.75,
                0: 1.00,
                1: 1.25, 2: 1.5, 3: 2, 4: 2.5

        }
        stage = max(-4, min(4, self.attack_stage))
        mod = stage_multipliers[stage]
        return mod*damage


    # THIS IS THE CRIT CALC ---------
    def crit_calc(self, stage_damage):
        chance = self.crit_chance + 0.05
        if random.random() < chance:
            crit_multiplier = 1.5
            print(f"WTF, {self.name}, got a CRITICAL HIT")
            return int(stage_damage*crit_multiplier)
        else:
            return int(stage_damage)
    
    # THIS IS THE TYPE CALC-------
    def type_calc(self, target, move_name):
        from data import element_type
        if move_name in element_type:
            attack_type = move_name.lower()
        else:
            attack_type = self.kga_type.lower()
                    
        

        multiplier = element_type[attack_type].get(target.kga_type, 1.0)
        if multiplier == 0:
            print("no effect dork")
        elif multiplier > 1.5:
                print(f"{move_name} was ultra big ball effective")
        elif multiplier > 1:
                print(f"{move_name} was super effective")
        elif multiplier == 1.0:
                print("")
        elif multiplier < 1:
                print(f"{move_name} was not very effective")
        elif multiplier < 0.5:
             print(f"{move_name} was garbage")
                
        return multiplier

    
    
# -------- THIS IS THE GOD FUNCTION ---------
    def calc_and_dealdamage(self, target, damage, move_name):
        stage_damage = self.stage_multiplier(damage)
        crit_damage = self.crit_calc(stage_damage)
        type_damage = self.type_calc(target, move_name)
        new_damage = int(crit_damage*type_damage)



        final_damage = new_damage
        target.health = target.health - final_damage
        if target.health < 0:
            target.health = 0 
        return final_damage
    
# TO DO: redo main.py and make it more readable and more robust
# Bugs: speed issues, hopefully goes after redoing. 
# new issue is that works fine for comp but for person too much text
# hopefully redoing main and making it extremely robust should solve it

