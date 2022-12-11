'''
The class responsible for accessing the database. Note that we use a ping
for every command since `pymysql` is thread safe. The better way would be
to use a connection pool instead.

NOTE: Using an ORM will better address this.
'''
import pymysql
from src.models.anime import Anime


class AnimeController:
    '''
    TODO
    '''

    def __init__(self) -> None:
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='anime_db',
        )

    def save(self, anime: Anime) -> Anime:
        '''
        FIXME SQL Injection
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute(f"\
            INSERT INTO animes(name, genres, author, seasons_nr) VALUES\
            ('{anime.name}', '{anime.genres}', '{anime.author}', {anime.seasons_nr})\
        ")
        anime.id_ = cursor.lastrowid
        self.conn.commit()
        self.conn.close()
        return anime

    def find_all(self):
        '''
        TODO
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
        FIXME SQL Injection
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute(f"\
            UPDATE animes SET \
                name='{anime.name}', genres='{anime.genres}',\
                author='{anime.author}', seasons_nr={anime.seasons_nr}\
                WHERE id={anime.id_}\
        ")
        self.conn.commit()
        self.conn.close()

    def remove(self, id_: int) -> None:
        '''
        FIXME SQL Injection
        '''
        cursor = self.conn.cursor()
        self.conn.ping()  # threadsafe
        cursor.execute(f"DELETE FROM animes WHERE id={id_}")
        self.conn.commit()
        self.conn.close()
