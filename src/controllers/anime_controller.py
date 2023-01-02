'''
The class responsible for accessing the database. Note that we use a ping
for every command since `pymysql` is thread safe. The better way would be
to use a connection pool instead.

NOTE: Using an ORM will better address this.
'''
import os
import pymysql
from src.models.anime import Anime


class AnimeController:
    '''
    The controller responsible for interacting with the `Anime` database table.
    It provides basic CRUD functionality.
    '''

    def __init__(self) -> None:
        self.conn = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS') or '',
            db=os.getenv('DB_NAME'),
        )

    def save(self, anime: Anime) -> Anime:
        '''
        Insert a row in the database.
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute("\
            INSERT INTO animes(name, genres, author, seasons_nr) VALUES\
            (%s, %s, %s, %s)\
        ", (anime.name, anime.genres, anime.author, anime.seasons_nr))
        anime.id_ = cursor.lastrowid
        self.conn.commit()
        self.conn.close()
        return anime

    def find_all(self):
        '''
        Find all rows in the database.
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute("SELECT * FROM animes")
        results = cursor.fetchall()
        self.conn.commit()
        self.conn.close()
        return results

    def update(self, anime: Anime) -> None:
        '''
        Update a row corresponding to the passed anime. Note that the anime
        argument should include all updates.
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute("\
            UPDATE animes SET name=%s, genres=%s, author=%s, seasons_nr=%s\
            WHERE id=%s\
        ", (anime.name, anime.genres, anime.author, anime.seasons_nr, anime.id_))
        self.conn.commit()
        self.conn.close()

    def remove(self, id_: int) -> None:
        '''
        Delete a database row.
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute("DELETE FROM animes WHERE id=%s", (id_,))
        self.conn.commit()
        self.conn.close()
