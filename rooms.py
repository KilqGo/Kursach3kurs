class Room:
    def __init__(self, room_text, connected_rooms=None):
        self.room_text = room_text
        self.connected_rooms = connected_rooms if connected_rooms is not None else []

    def __str__(self):
        return f"{self.room_text} "


def main():

    rooms = [
        Room("Начало",  ["Верх 1", "Низ 1"]),
        Room("Верх 1",  ["Верх 2"]),
        Room("Верх 2",  ["Конец"]),
        Room("Низ 1",  ["Низ 2"]),
        Room("Низ 2",  ["Конец"]),
        Room("Конец")
    ]

    current_room = rooms[0]  # начало

    while True:
        if not current_room.connected_rooms:
            print("Победа!")
            break

        print(f"\nВы находитесь в: {current_room}")

        # проверка доступных
        print("Выбор комнаты:")
        for i, room_name in enumerate(current_room.connected_rooms):
            print(f"{i + 1}. {room_name}")

        choice = input("Выбор номера комнаты: ")

        if choice.isdigit() and 1 <= int(choice) <= len(current_room.connected_rooms):
            selected_room_name = current_room.connected_rooms[int(choice) - 1]
            current_room = next((room for room in rooms if room.room_text == selected_room_name), current_room)
            print(f"Перемещение в {current_room}.")
        else:
            print("Ошибка ввода.")
            continue

if __name__ == "__main__":
    main()