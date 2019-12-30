from abc import abstractmethod
from typing import Dict, List
from classes.file import File
import copy

class RenameFiles:
    __original: Dict[str, File] = {}
    modified: Dict[str, File] = {}

    def __init__(self, rename_files: List[File]):
        for rename_file in rename_files:
            self.add_file(rename_file)

    def add_file(self, rename_file: File):
        self.__original.update({str(rename_file.id): rename_file})
        self.modified = copy.deepcopy(self.__original)

    def change_rename_path(self, path: str):
        for key, file in self.modified.items():
            file.path = path

    def max_length_path(self) -> int:
        max_length = 0
        for key, file in self.original_files().items():
            length = len(str(file))
            max_length = (max_length, length)[max_length < length]

        return max_length

    def original_files(self):
        return self.__original

    @abstractmethod
    def rename(self):
        pass