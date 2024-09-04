class Room:
    def __init__(self, room_id, room_text, right_room=None):
        self.room_id = room_id
        self.room_text = room_text
        self.right_room = right_room

    def __str__(self):
        return self.room_text


def main():
    # комнаты
    room1 = Room(1, "Начало")
    room2 = Room(2, "Верх_1")
    room3 = Room(3, "Низ_1")
    room4 = Room(4, "Верх_2")
    room5 = Room(5, "Низ_2")
    room6 = Room(6, "Конец")

    # связи между комнатами
    room1.right_room = (room2, room3)  # разветвление на комнаты 2 и 3
    room2.right_room = room4  # путь из комнаты 2 в комнату 4
    room3.right_room = room5  # путь из комнаты 3 в комнату 5
    room4.right_room = room6  # путь из комнаты 4 в комнату 6
    room5.right_room = room6  # путь из комнаты 5 в комнату 6

    # начальная позиция
    current_room = room1

    while True:
        print(f"\nВы находитесь в: {current_room}")

        # проверяем, есть ли доступные комнаты
        if isinstance(current_room.right_room, tuple):
            print("Выберите комнату для перемещения:")
            print("1. Верх")
            print("2. Низ")
            choice = input("Введите номер комнаты: ")

            if choice == '1':
                current_room = current_room.right_room[0]  # перемещение в комнату 2
                print("Вы идёте наверх.")
            elif choice == '2':
                current_room = current_room.right_room[1]  # перемещение в комнату 3
                print("Вы идёте вниз.")
            else:
                print("Ошибка.")
                continue

        if current_room.right_room:
            print(f"Вы можете переместиться в: {current_room.right_room}")
            choice = input("Введите '1' для перемещения вперед: ")

            if choice.lower() == '1':
                current_room = current_room.right_room
                print(f"Вы переместились в {current_room}.")

                if current_room.room_id == 6:
                    print("Конец.")
                    break
            else:
                print("Ошибка.")


if __name__ == "__main__":
    main()