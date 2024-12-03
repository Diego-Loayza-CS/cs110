def make_rooms(words):
    rooms = []
    for word in words:
        room = word + 'room'
        rooms.append(room)
    return rooms


if __name__ == '__main__':
    some_words = ['ball', 'bath', 'bed', 'family', 'food', 'car']
    rooms = make_rooms(some_words)
    print(f'Original words: {some_words}')
    print(f'Rooms: {rooms}')
