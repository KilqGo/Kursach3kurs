class Room:
    def __init__(self, room_text, connected_rooms=None,battle_id=0):
        self.room_text = room_text
        self.battle_id = battle_id
        self.connected_rooms = connected_rooms if connected_rooms is not None else []

    def __str__(self):
        return f"{self.room_text} "
