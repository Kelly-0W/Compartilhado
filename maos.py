import json
import random

# extraindo informações dos dicionários
with open("cartas.json", "r", encoding="utf-8") as informaçoes:
    cards = json.load(informaçoes)

gods = cards['Deuses'] #colocando cada informação separadamente em variáveis diferentes
camps = cards['Campo']

deck_gods = []
commom_gods = []
royal_gods = []
market = []

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
        self.occupied_by = None

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.places = []
        
    # mostra a mão
    def show_hand(self):
        print("=== Sua mão é: ===")
        for i, card in enumerate(self.hand, start=1):  # mostra a mão
            print(f"{i}º {card.name} | {card.pantheon}")
    
    # compra carta
    def draw_from_deck(self):
        if len(deck_gods) > 0:
            card = deck_gods.pop(0)
            self.hand.append(card)
        else:
            print("O baralho acabou!")
    
    def draw_from_market(self):
        if not market:
            print("O mercado está vazio")
            return

        print("=== Mercado ===")
        for i, card in enumerate(market, start=1):
            print(f"{i}º {card.name} | {card.pantheon}")
        
        try:
            choice = int(input("Escolha a carta pelo indice:\n"))
            chosen_card = market.pop(choice - 1)
            self.hand.append(chosen_card)
            print(f"Você pegou o {chosen_card.name}")
        
        except(ValueError, IndexError):
            print("Entrada inválida")
    
    # coloca as cartas de campo no começo do jogo
    def start_camp(self):
        for i in range(4):
            if deck_camp:
                index = random.randrange(len(deck_camp))
                sorted_camp = deck_camp.pop(index)
                self.places.append(sorted_camp)

    # mostra os campos
    def show_camps(self):
        print("=== Seu campo ===")
        for i, camp in enumerate(self.places, start=1):
            status = camp.occupied_by.name if camp.occupied_by else "Vazio"
            print(f'{i}º {camp.name} | {camp.pantheon} | Ocupado: {status}')
    
    # coloca carta
    def place_card(self):
        if not self.hand: # verifica se tem carta na mão
            print("Você não possuí cartas para jogar")
            return None
        
        self.show_hand()

        print("=== Selecione uma carta pelo Index ===")
        try:
            choice = int(input())
            chosen_card = self.hand[choice - 1] # escolhe a carta pelo indice dela

            print("\nEm qual campo vai colocar a carta? (Digite o número)")
            self.show_camps()

            place_choice = int(input())
            target_camp = self.places[place_choice - 1]

            # verifica se o deus é do mesmo panteão do campo
            if chosen_card.pantheon != target_camp.pantheon:
                print(f"Você não pode colocar um deus {chosen_card.pantheon} em um campo {target_camp.pantheon}")
                return None
            
            if target_camp.occupied_by is not None:
                print("Você não pode colocar uma carta em um campo já ocupado")
                return None
            
            self.hand.pop(choice - 1)
            target_camp.occupied_by = chosen_card
            print(f"Você colocou a carta de {chosen_card.name} no campo {target_camp.name}")
            return chosen_card
        
        except (ValueError, IndexError):
            print("Escolha inválida")
            return None

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

def refil_market():
    while len(market) < 3 and deck_gods:
        market.append(deck_gods.pop(0))

for card in deck_gods:
    print(card.name, "|", card.pantheon)
for camp in deck_camp:
    print(camp.name, "|", camp.pantheon)