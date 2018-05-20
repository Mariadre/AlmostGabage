from towns_person import TownsPerson


class Map:
    def __init__(self, width, height):
        from hero import Hero
        self.width = width
        self.height = height
        self.hero = Hero(6, 4, self.is_movable, self.update, self.get_message)
        self.townspeople = []

    def run(self):
        self.set_cast()
        self.hero.run()

    def is_movable(self, x, y):
        if x < 0:
            return False
        elif self.width - 1 < x:
            return False
        elif y < 0:
            return False
        elif self.height - 1 < y:
            return False

        for townsperson in self.townspeople:
            if x == townsperson.x and y == townsperson.y:
                return False

        return True

    def update(self, message=''):
        characters = {}
        for townsperson in self.townspeople:
            characters[(townsperson.x, townsperson.y)] = townsperson.icon
        characters[(self.hero.x, self.hero.y)] = self.hero.icon

        def get_top_bottom_text():
            return '+{}+\n'.format('-' * self.width)

        def get_message_border(width):
            return '#' * width + '\n'

        map_tips = []
        map_tips.append(get_top_bottom_text())
        for y in range(0, self.height):
            map_tips.append('|')
            for x in range(0, self.width):
                if (x, y) in characters:
                    map_tips.append(characters[(x, y)])
                else:
                    map_tips.append(' ')
            map_tips.append('|\n')
        map_tips.append(get_top_bottom_text())
        if message:
            map_tips.append(get_message_border(len(message) + 2))
            map_tips.append(' {}\n'.format(message))
            map_tips.append(get_message_border(len(message) + 2))

        print(''.join(map_tips))

    def set_cast(self):
        self.townspeople.append(TownsPerson(6, 1, 'K', "Death Should Not Have Taken Thee!"))
        self.townspeople.append(TownsPerson(1, 5, 'S', "I'm a soldier."))
        self.townspeople.append(TownsPerson(10, 6, 's', "No response. Looks dead."))

    def get_message(self, x, y):
        for townsperson in self.townspeople:
            if x == townsperson.x and y == townsperson.y:
                return townsperson.message
        return 'no one exists.'
