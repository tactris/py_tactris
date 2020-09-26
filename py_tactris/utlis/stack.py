class SmartStack:
    def __init__(self, size):
        self.size = size
        self._data = []

    def append(self, elem):
        self._data.append(elem)
        if len(self._data) > self.size:
            return self._data.pop(0)

    def remove(self, elem):
        self._data.remove(elem)

    def clear(self):
        self._data = []

    def __iter__(self):
        return iter(self._data)

    def __bool__(self):
        return bool(self._data)
