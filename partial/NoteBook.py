from collections import UserDict, UserList
from typing import Generator, Optional


class Tag:
    def __init__(self, value: str) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value


class Note():
    def __init__(self, text: str, id:int, tags: list[str]) -> None:
        self.text = text
        self.id = id
        self.tags = [Tag(tag) for tag in tags]
    
    def __str__(self) -> str:
        tags = []
        for tag in self.tags:
            tags.append(str(tag.value))
        note_tags =', '.join(tags)
        return f'ID:{self.id} Note: {self.text}\nTags: {note_tags}'

class NoteBook(UserList):
    """
    Desrcibes object fo personal book with notes
    """
    def set_ID(self):
        return len(self.data) + 1

    def add_note(self, text:str, *tags:str) -> None:
        '''Method for adding note to list'''
        id = self.set_ID()
        new_note = Note(text, id, tags)
        self.data.append(new_note)
        print('New note was added')

    def find_note(self, subtext:str) -> None:
        '''Method to find notes by text or ID'''
        notes_list = []
        for note in self.data:
            if subtext in note.text  or subtext == str(note.id):
                notes_list.append(note)
        for note in notes_list:
            print(str(note))

    def del_note(self, id: int) -> None:
        """Method to delete note by ID"""
        try:
            id = int(id)
        except ValueError:
            raise ValueError('Input a number')
        del_note = None
        for note in self.data:
            if id == note.id:
                del_note = self.data.pop(id-1)
                print(f'Note ID={id} was deleted')
        if not del_note:
            print('ID={id} is not valide')

    def change_note(self, id: int, new_text: str) -> None:
        '''Method searches for a note by ID and changes its text'''
        try:
            id = int(id)
        except ValueError:
            raise ValueError('Input a number')
        for note in self.data:
            if id == note.id:
                note.text = new_text

    def add_note_tags(self, id: int, *tags:list[str]) -> None:
        '''Method add tags to tags-list in note by ID'''
        try:
            id = int(id)
        except ValueError:
            raise ValueError('Input a number')
        for note in self.data:
            if id == note.id:
                note.tags.extend([Tag(tag) for tag in tags])
                print('Tags was added')

    def find_by_tag(self, tag:str) -> None:
        '''Method to find notes by tag'''
        notes_list = []
        for note in self.data:
            note_tags = [tag.value for tag in note.tags]
            if tag in note_tags:
                notes_list.append(note)
        for note in notes_list:
            print(str(note))