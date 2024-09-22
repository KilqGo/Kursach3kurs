class Room:
    def __init__(self, room_text, connected_rooms=None):
        self.room_text = room_text
        self.connected_rooms = connected_rooms if connected_rooms is not None else []

    def __str__(self):
        return f"{self.room_text} "
