from uuid import uuid4
import os

class File:
    id: uuid4()
    name: str
    extension: str
    path: str

    def __init__(self, file: str, identifier: str = None):
        filename = os.path.basename(file)
        splitted = os.path.splitext(filename)

        self.id = identifier if identifier else uuid4()
        self.name = splitted[0]
        self.extension = splitted[1][1:]
        self.path = os.path.dirname(os.path.abspath(file))

    def __str__(self):
        return self.path + '/' + self.name + '.' + self.extension