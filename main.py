import random
import time

adjective_list = ["Scary","Hairy","Large","Ugly","Evil","Magical","Angry","Trigger-happy","Dirty", "Drunk","Trashy", "Morbidly Obese", "Virgin", "Gassy", "Nerdy", "Small", "Well Rested"]
character_list = ["Podcaster", "Guy in an Afflication T-shirt","Stoner","Pastor", "Hobo", "Rabbit","Zebra", "Karen", "Bob Dylan", "Gary Busey", "Al Roker", "Boomer", "Millennial", "Gen-Zer", "Internet Explorer User", "Person with a petition clipboard"]
expression_list = ["All of a sudden","Just like a movie","OH NO","Sweet Jesus","Holy Smokes","GEEEEZUS","I'm getting bored writing prompts"]
base_attack_dict = {"punch":3, "kick":5,"sword":7,"gun":15}
enemy_attack_dict = {"punch":10, "kick":20,"sword":30,"gun":40}
enemy_dict = {}

class player:
    def __init__(self,name,health,base_attack,base_defense,base_attack_dict):
        self.name = name
        self.health = 100
        self.base_attack = 2
        self.base_defense = 2
        self.base_attack_dict = base_attack_dict

class enemy:
    def __init__(self,name,health,base_attack,base_defense,enemy_attack_dict):
        self.name = adjective_list.pop(random.randint(0,len(adjective_list)-1)) + " " + character_list.pop(random.randint(0,len(character_list)-1))
        self.health = random.randint(80,100)
        self.base_attack = max(1,5*(1-(self.health/100)))
        self.base_defense = 5 - self.base_attack
        self.enemy_attack_dict = enemy_attack_dict
    
    def remove_damage(self,damage):
        self.health = self.health - damage

def enemy_creation():
    for i in range(1,6):
        enemy_holder = enemy("name",0,0,0,enemy_attack_dict)
        enemy_dict["enemy_{0}".format(i)] = {"name": enemy_holder.name, "health": enemy_holder.health, "base_attack":enemy_holder.base_attack,"base_defense":enemy_holder.base_defense, "enemy_attack_dict":enemy_holder.enemy_attack_dict}
    return(enemy_dict)

def attack(enemy,user_name,player_kill_count):
    print("\n\n\n{}, {} enters and is ready to fight.\n".format(expression_list[random.randint(0,len(expression_list)-1)],enemy_dict[enemy]['name']))
    while enemy_dict[enemy]["health"] > 0 and user_name.health > 0:
        selected_attack_power, selected_attack_name = attack_selection(base_attack_dict,"player" )
        selected_attack = selected_attack_power * user_name.base_attack
        enemy_dict[enemy]["health"] = enemy_dict[enemy]["health"] - selected_attack
        print("\nYou've damaged {} by {} with {}. Their health is now {}\n".format(enemy_dict[enemy]['name'],selected_attack,selected_attack_name,enemy_dict[enemy]["health"]))
        if enemy_dict[enemy]["health"] > 0:
            selected_attack_power, selected_attack_name = attack_selection(base_attack_dict,"bot" )
            selected_attack = selected_attack_power * enemy_dict[enemy]["base_attack"]
            user_name.health = user_name.health - selected_attack
            print("\n{} damaged you by {} with {}. Your health is now {}".format(enemy_dict[enemy]['name'], selected_attack, selected_attack_name,user_name.health))
        else:
            if enemy_dict[enemy]["health"]<= 0 and user_name.health > 0:
                print("\nYou have Defeated {}".format(enemy_dict[enemy]['name']))
                time.sleep(4)
                user_name.health = user_name.health - enemy_dict[enemy]["health"]
                print("\n You have harvested {} HP from {} and your health is now {}.".format(enemy_dict[enemy]["health"]*-1,enemy_dict[enemy]['name'],user_name.health))
                time.sleep(4)
                del enemy_dict[enemy]
                player_kill_count = 1
                return(player_kill_count)
            else:
                print("You have been killed. You are a complete failure and your grave will remain unmarked.")
                player_kill_count = - 1
                return(player_kill_count,player_death)

def attack_selection(base_attack_dict,mode):
    if mode == "player":
        selected_attack_initial = input("\nPlease type name of attack, (punch,kick,sword,gun) : " )
    else:
        enemy_attack_list = ["punch", "kick","sword","gun"]
        selected_attack_initial = enemy_attack_list[random.randint(0,len(enemy_attack_list)-1)]
    if selected_attack_initial == "gun":
          selected_attack_power = base_attack_dict[selected_attack_initial] * (random.randint(1,7)/10)
    elif selected_attack_initial == "sword":
        selected_attack_power = base_attack_dict[selected_attack_initial] * (random.randint(5,10)/10)
    elif selected_attack_initial == "kick":
        selected_attack_power = base_attack_dict[selected_attack_initial] * (random.randint(7,10)/10)
    elif selected_attack_initial == "punch":
        selected_attack_power = base_attack_dict[selected_attack_initial]
    else:
        print("MISS")
        selected_attack_power = 0
    return selected_attack_power, selected_attack_initial

def run_game(round):
    player_kill_counter = 0
    player_death = 0
    if round == 0:
        enemy_dict = enemy_creation()
        print("\n\n\n\n\nTHE ULTIMATE EVERYDAY NORMAL GUY FIGHT SIM")
        user_name = input("\nPlease enter your fighter's name:  ")
        user_name = player(user_name,100,3,3,base_attack_dict)
        print(user_name.health)
        print("\n\n\n\n\n\n\nWelcome to the Matrix, %s. You're probably a little confused." % user_name.name)
        time.sleep(2)
        print("\nYou fell asleep at your computer again. And the matrix army needs you, %s, to fight its biggest enemies." % user_name.name)
        time.sleep(5)
        print("\nThe hit list is as follows:")
        for i in range(1,6):
            print("\n\t" + enemy_dict["enemy_{0}".format(i)]['name'])
        time.sleep(5)
        #print(enemy_dict)
        round = 1
        while player_kill_counter != 5 and player_death == 0:
            round_enemy = "enemy_{0}".format(round)
            player_kill_counter = attack(round_enemy,user_name,player_kill_count)
            if player_kill_counter == 1:
                round += 1
            else:
                player_death = 1

        if player_kill_count == 5:
            print("\n\n\nYou are the hero of The Matrix, {}. Go now and prosper.".format(user_name.name))
            play_again()
        else:
            print("\n\n\nYou lost.")
            play_again()

def play_again():
    choice = input("\n\nPlay Again? (y|n): ")
    if choice == "y":
        player_kill_count = 0
        player_death = 0
        round = 0
        run_game(round)
    else:
        print("\n Thank you for playing")

            
player_kill_count = 0
player_death = 0
round = 0
run_game(round)