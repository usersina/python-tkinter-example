# pylint: disable=invalid-name
'''
The Anime class or entity corresponds to a database table.

TODO: Use an ORM.
'''


class Anime:
    '''
    The class that corresponds to the table of the same name.
    '''

    def __init__(self, name: str, genres: str, author: str, seasons_nr: int) -> None:
        self.id_: None | int = None
        self.name = name
        self.genres = genres
        self.author = author
        self.seasons_nr = seasons_nr

    def set_id(self, id_: int):
        '''
        ID Setter. This is used since an Anime object cannot be instantiated
        with the ID since the database is handling that.
        '''
        self.id_ = id_
        return self
