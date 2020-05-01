import random

deck = ["Ace", 2, 3, 4, 5, 7, 8, 9, 10, "Jack", "Queen", "King"]

dealer_cards = []
player_cards = []


def add(deck, hand):
    card = random.choice(deck)
    hand.append(card)

def set_Game(dealer, player, deck):
    add(deck, player)
    add(deck, dealer)
    add(deck, player)
    add(deck, dealer)
    return


set_Game(dealer_cards, player_cards, deck)




def show_cards(hand):
    total = 0
    print("Player:", end=" ")
    for i in hand:
        temp = i
        
        if temp == "Jack" or i == "Queen" or i == "King":
            print("[" + i + "]", end=" ")
            temp = 10
        elif temp == "Ace":
            print("["+i+"]", end=" ")
            choice = input(
                "Do you want your ace to be a 1 or 11?\nEnter 1 or 11: ")
            if choice == "11":
                temp = 11
            else:
                temp = 1
        else:
            print("["+str(i)+"]", end=" ")
        total += temp
    print(end="\n")
    return total


def show_dealer_cards(hand):
    total = 0
    print("Dealer:", end=" ")
    for i in hand:
        temp = i
        if temp == "Jack" or i == "Queen" or i == "King":
            print("[" + i + "]", end=" ")
            temp = 10
        elif temp == "Ace":
            print("["+i+"]", end=" ")
            choice = input(
                "Do you want your ace to be a 1 or 11?\nEnter 1 or 11: ")
            if choice == "11":
                temp = 11
            else:
                temp = 1
        else:
            print("["+str(i)+"]", end=" ")
        total += temp
    print(end="\n")
    return total


p_value = show_cards(player_cards)
d_value = show_dealer_cards(dealer_cards)


while (p_value <= d_value and p_value < 21) or (p_value >= d_value and d_value < 21):
    add(deck, player_cards)
    p_value = show_cards(player_cards)
    if p_value > 21:
        print("Player Busts!")
        break

    if d_value < 21 and d_value <= p_value:
        add(deck, dealer_cards)
        d_value = show_dealer_cards(dealer_cards)
    if d_value > 21:
        print("Deal Busts!")
        break
       


