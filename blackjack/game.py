import random

# Какие у нас будут карты
cards = ["[2]", "[3]", "[4]", "[5]",
         "[6]", "[7]", "[8]", "[9]", "[10]",
         "[В]", "[Д]", "[К]", "[Т]" ]
# Какие у карт значения (соответствует списку с картами)
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

n = 3 # Число игроков
players = [0] * n # Создаем список из n игроков и каждому даем пока ноль карт
players_cards = [ [] for _ in range(n)] # Список из n списков для карт игроков
passed = [False] * n            # Список для обозначения позиции игроков


while True:

    if False not in passed: # Если среди игроков нет тех, кто пропустил
        max = max(players)
        winners = []
        for i in range(n):
            print("У игрока", i + 1, " - ", players[i], "Очков")
            if players[i] == max:   # Если счет игрока максимальный, добавляем его в список победителей
                winners.append(i+1)

        print(f"Победили игроки: ", winners)
        break


    for i in range(n):
        if not passed[i]: # Если не пропустил

            turn = input(f"Игрок {i+1}, Взять или пропуск?")
            if turn == "взять":
                # Берем случайное число от нуля до количества карт минус один
                rand = random.randint(0, len(cards) - 1)
                players[i] += values[rand]              # Добавляем игроку очки
                players_cards[i].append(cards[rand])    # Добавляем игроку карту
                cards.pop(rand)                         # Удаляем карту из колоды
                values.pop(rand)                        # Удаляем очки из списка
                if players[i] > 21:
                    print("Вы выбыли!")
                    players[i] = 0
                    passed[i] = True


            elif turn == "Пропуск":
                passed[i] = True

            print("Ваши карты: ", players_cards[i])


