import getch
from maps import Map


class Hero:
    operations = {'up': 119, 'left': 97, 'right': 115, 'down': 122,
                  'talk': 116, 'quit': 3}

    def __init__(self, x, y, is_movable, update, get_message):
        self.x = x
        self.y = y
        self.icon = '^'
        self.is_movable = is_movable
        self.update = update
        self.get_message = get_message

    def run(self):
        print('---------------------------------')
        print('w: up, a: left, s: right, z: down')
        print('t: talk, ctrl+c: quit')
        print('---------------------------------')
        self.update()

        while True:
            key = ord(getch.getch())
            if key == Hero.operations['quit']:     # ctrl+c: quit
                print('bye!')
                exit()
            elif key == Hero.operations['up']:     # w: up
                self.icon = '^'
                if self.is_movable(self.x, self.y - 1):
                    self.y -= 1
            elif key == Hero.operations['left']:   # a: left
                self.icon = '<'
                if self.is_movable(self.x - 1, self.y):
                    self.x -= 1
            elif key == Hero.operations['right']:  # s: right
                self.icon = '>'
                if self.is_movable(self.x + 1, self.y):
                    self.x += 1
            elif key == Hero.operations['down']:   # z: down
                self.icon = 'v'
                if self.is_movable(self.x, self.y + 1):
                    self.y += 1
            elif key == Hero.operations['talk']:   # t: talk
                self.talk()
                continue
            else:
                continue

            # print(self.icon, 'x:', self.x, 'y:', self.y)  # for debugging
            self.update()

    def talk(self):
        if self.icon == '^':
            self.update(self.get_message(self.x, self.y - 1))
        elif self.icon == '<':
            self.update(self.get_message(self.x - 1, self.y))
        elif self.icon == '>':
            self.update(self.get_message(self.x + 1, self.y))
        elif self.icon == 'v':
            self.update(self.get_message(self.x, self.y + 1))
        else:
            pass


m = Map(14, 7)
m.run()
