from basewindow import BaseWindow
import tkinter as tk


class Room:
    def __init__(self, room_text, connected_rooms=None):
        self.room_text = room_text
        self.connected_rooms = connected_rooms if connected_rooms is not None else []

    def __str__(self):
        return f"{self.room_text} "


class GameApp(BaseWindow):
    def __init__(self):
        super().__init__()

        self.rooms = [
            Room("Начало", ["Верх 1", "Низ 1"]),
            Room("Верх 1", ["Верх 2"]),
            Room("Верх 2", ["Конец"]),
            Room("Низ 1", ["Низ 2"]),
            Room("Низ 2", ["Конец"]),
            Room("Конец")
        ]

        self.current_room = self.rooms[0]  # начало

        self.text_box = tk.Text(self, height=15, width=50, bg="#FF4500", fg="black", insertbackground='black', bd=2,
                                relief="solid")
        self.text_box.pack(pady=10)

        self.buttons_frame = tk.Frame(self, bg="black")
        self.buttons_frame.pack(pady=10)

        self.update_text_box()
        self.create_room_buttons()

    def update_text_box(self):
        """Обновляем текстовое поле с информацией о текущей комнате."""
        self.text_box.delete("1.0", tk.END)  # чистка текста
        if not self.current_room.connected_rooms:
            self.text_box.insert(tk.END, "Победа! Игра окончена.")
            return

        self.text_box.insert(tk.END, f"\nВы находитесь в: {self.current_room}\n")
        self.text_box.insert(tk.END, "Выбор комнаты:\n")

    def create_room_buttons(self):
        """Создаем кнопки для доступных комнат."""
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()  # удаление кнопок

        for room_name in self.current_room.connected_rooms:
            button = tk.Button(self.buttons_frame, text=room_name,
                               bg="#FF4500", fg="black",
                               bd=2, relief="solid",
                               command=lambda name=room_name: self.move_to_room(name))
            button.pack(side=tk.LEFT, padx=5)

    def move_to_room(self, room_name):
        """Перемещение в выбранную комнату."""
        selected_room = next((room for room in self.rooms if room.room_text == room_name), None)

        if selected_room:
            self.current_room = selected_room
            self.update_text_box()
            self.create_room_buttons()


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()