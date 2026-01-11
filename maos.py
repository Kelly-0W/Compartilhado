import json
import random

# extraindo informações dos dicionários
with open("cartas.json", "r", encoding="utf-8") as informaçoes:
    cards = json.load(informaçoes)

gods = cards['Deuses'] #colocando cada informação separadamente em variáveis diferentes
camps = cards['Campo']

class Gods():
    def __init__(self, name, pantheon, hand_skill, camp_skill, royal=False):
        self.name = name
        self.pantheon = pantheon
        self.hand_skill = hand_skill
        self.royal = royal
        if self.royal == True:
            self.camp_skill = camp_skill
        else:
            self.camp_skill = None
    
class Camp():
    def __init__(self, name, pantheon, skill):
        self.name = name
        self.pantheon = pantheon
        self.skill = skill

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def show_hand(self):
        print("=== Sua mão é: ===")
        for i, card in enumerate(self.hand, start=1):  # mostra a mão
            print(f"{i}º {card.name} | {card.pantheon}")
    
    def draw_card(self):
        if len(deck_gods) > 0:
            card = deck_gods.pop(0)
            self.hand.append(card)
        else:
            print("O baralho acabou!")
    
    def place_card(self):
        if not self.hand:
            print("Você não possuí cartas para jogar")
            return None
        
        self.show_hand()

        print("=== Selecione uma carta pelo Index ===")
        try:
            choice = int(input())
            chosen_card = self.hand.pop(choice - 1)
            return chosen_card
        
        except (ValueError, IndexError):
            print("Escolha inválida")
            return None

        
deck_gods = []
commom_gods = []
royal_gods = []

# separando os deuses nobres dos deuses comuns
for god in gods:
    if god.get('Nobre') is None:
        commom_gods.append(god)
    else:
        royal_gods.append(god)

# colocando 1 cópia de deus nobre no baralho e 2 cópias de deuses comuns
for god_data in royal_gods:
    god = Gods(god_data['Nome'], god_data['Panteao'], god_data['Habilidade mao'], god_data['Habilidade mesa'], royal=True)
    deck_gods.append(god)

for commom_god in commom_gods:
    for i in range(2):
        deck_gods.append(Gods(commom_god['Nome'], commom_god['Panteao'], commom_god['Habilidade mesa'], commom_god.get('Habilidade mao')))

deck_camp = []
for camp_data in camps:
    for i in range(3):
        deck_camp.append(Camp(camp_data['Nome'], camp_data['Panteao'], camp_data['Habilidade']))

for card in deck_gods:
    print(card.name, "|", card.pantheon)
for camp in deck_camp:
    print(camp.name, "|", camp.pantheon)