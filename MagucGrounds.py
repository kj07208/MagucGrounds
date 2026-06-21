### Welcom to the Maguc Grounds, a land of great quests!
from dataclasses import dataclass
from enum import Enum

# Global variables
character_names =["Aragorn", "Gandalf", "Legolas", "Gimli", "Frodo", "Samwise", "Boromir", "Merry", "Pippin"]
adventure_locations = ["Enchanted Forest", "Dark Caves", "Mystic Mountains", "Ancient Ruins", "Haunted Castle"]
quest_types = ["Rescue the Princess", "Defeat the Dragon", "Find the Lost Treasure", "Protect the Village", "Explore the Unknown"]


class CharactorType(Enum):
    WARRIOR = 1
    MAGE = 2
    WIZZARD = 3
    THIEF = 4
    HEALER = 5

class PlayerType(Enum):
    HUMAN = 1
    COMPUTER = 2

class SkillClass(Enum):
    BASIC = 1
    INTERMEDIATE = 2
    ADVANCED = 3


@dataclass
class Charactor:
    name: str 
    character_type: CharactorType
    player_type: PlayerType = PlayerType.COMPUTER
    health: int = 100
    xp: int = 25
    money: float = 10.0
    skill_level: int = 1
    skill_class: SkillClass = SkillClass.BASIC 

print("Welcome to the Maguc Grounds")
print("Create your charactor")
name = input("What is your name? ")
print("What is your charactor type?")
print("1. Warrior")
print("2. Mage")
print("3. Wizzard")
print("4. Thief")
print("5. Healer")
type_input = input("Enter the number of your choice: ")

charactor_type = CharactorType.WARRIOR
if type_input == "1":
    charactor_type = CharactorType.WARRIOR
elif type_input == "2":
    charactor_type = CharactorType.MAGE
elif type_input == "3":
    charactor_type = CharactorType.WIZZARD
elif type_input == "4":
    charactor_type = CharactorType.THIEF
elif type_input == "5":
    charactor_type = CharactorType.HEALER
else:
    print("Invalid choice. Please try again.")
    exit()

team: list[Charactor] = []
charactor = Charactor(name, charactor_type, PlayerType.HUMAN)
team.append(charactor)
remaining_team_members = [t for t in CharactorType if t != charactor_type]
for character_type in remaining_team_members:
    print(f"Choose your team member {character_type.name}")
    name = character_names.pop(0)
    charactor = Charactor(name, character_type, PlayerType.COMPUTER)
    team.append(charactor)

print("\nYour team has been created:")
for member in team:
    print(f"{member.name} the {member.character_type.name} has joined your team with {member.health} health, {member.xp} xp, and ${member.money:.2f} money.")

print("\nLet the adventure begin!")
print("Choose your first adventure: ")
for i, location in enumerate(adventure_locations, 1):
    print(f"{i}. {location}")
location_input = input("Enter the number of your choice: ")
if location_input in ["1", "2", "3", "4", "5"]:
    location = adventure_locations[int(location_input) - 1]
    print(f"You have chosen to adventure in the {location}.")
for item in quest_types:
    print(f"Your quest is to {item}.")
    