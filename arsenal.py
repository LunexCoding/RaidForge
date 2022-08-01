class Arsenal:
    def __init__(self, path):
        self._path = path
        self._file = open(self._path, 'w+')
        self._data = None

    def load(self):
        self._file.seek(0)
        self._data = self._file.read()
        print(self._data)

    def addInArsenal(self, msg):
        self._file.write(str(msg) + f"\n{'-' * 15}\n")


g_arsenal = Arsenal('data/user.txt')
