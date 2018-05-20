import getch


class KeyCodeLogger:
    def run(self):
        while True:
            key = ord(getch.getch())
            if key == 3:  # Ctrl+C
                print('quit')
                break
            print('key input: {}'.format(key))


logger = KeyCodeLogger()
logger.run()
