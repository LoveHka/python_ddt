import random
from gc import get_count


class Card:
    names = ["2", "3", "4", "5", "6", "7", "8",
             "9", "10", "Валет", "Дама", "Король", "Туз"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    def __init__(self, suit, card):
        self.suit = suit # Запоминаем масть при рождении
        self.card = card # Запоминаем вид карты при рождении
        index = Card.names.index(card)
        self.value = Card.values[index]

    def show_card(self):
        print(self.card, self.suit) # Значение не показываем!

class Deck:
    def __init__(self):
        self.cards = []

    def create52(self):
        suits = ["Черви", "Бубны", "Пики", "Крести"]
        names = Card.names # Имена взяли из класса карт
        for suit in suits: # Для каждой масти
            for name in names: # Для каждого имени карты
                new_card = Card(suit, name)
                self.cards.append(new_card)

    def show_deck(self):
        for card in self.cards:
            card.show_card()

    def shuffle_cards(self):
        random.shuffle(self.cards) # Перемешиваем карты !!!1 УРАААААА

    def get_card(self):
        return self.cards.pop() # Берем последнюю (верхнюю карту)
                                # Сразу удаляем ее из колоды

new_desk = Deck()       # Создали колоду
new_desk.create52()
#new_desk.shuffle_cards()
# Берем из перемешанной колоды верхнюю карту
some_card = new_desk.get_card()

print("Мы взяли:")
some_card.show_card()
print("Попробуй найти её в колоде:")
new_desk.show_deck()
