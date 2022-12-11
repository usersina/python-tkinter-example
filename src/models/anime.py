# pylint: disable=invalid-name
'''
The Anime object or entity that corresponds to a database column.
TODO: Use an ORM
'''


from typing import Self


class Anime:
    '''
    Default constructor.
    '''

    def __init__(self, name: str, genres: str, author: str, seasons_nr: int) -> None:
        self.id_: None | int = None
        self.name = name
        self.genres = genres
        self.author = author
        self.seasons_nr = seasons_nr

    def set_id(self, id_: int) -> Self:
        '''
        ID Setter
        '''
        self.id_ = id_
        return self
