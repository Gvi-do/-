import json

class Myrang:

    def __init__(self, file):
        self.file = file
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file, encoding='utf-8') as f:
            country = json.load(f)[self.index]
            result = f"{country['translations']['rus']['official']} = https://ru.wikipedia.org/wiki/{country['translations']['rus']['official']}"
            if self.index == len(self.file):
                raise StopIteration
            self.index += 1

            return result



for item in Myrang('Country.json'):
    print(item)


