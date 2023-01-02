import sqlite3
from sqlite3 import Error

class DBFacade:

    SCRATCH_BALLS = "scratch_balls"
    SCRATCH_PENIS = "scratch_penis"

    def __init__(self) -> None:
        try: 
            self.__connection = sqlite3.connect("database/bot_db.db")
            self.__cursor = self.__connection.cursor()
        except Error as e:
            print(e)

        
    def create_tables(self) -> None:
        """
        Create tables if there are none
        """
        # Create scratch balls table
        self.__cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {DBFacade.SCRATCH_BALLS}(
                    person TEXT PRIMARY KEY,
                    times INTEGER NOT NULL,
                    last_scratch TEXT
                )
            """
        )
        # Create scratch penis table
        self.__cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {DBFacade.SCRATCH_PENIS}(
                    person TEXT PRIMARY KEY,
                    times INTEGERNOT NULL,
                    last_scratch TEXT
                )
            """
        )
        self.__connection.commit()


    def add_person_to_balls(self, person: str) -> None:
        """
        Adds a new player to "scratch balls" table
        """
        self.__cursor.execute(
            f"""
            INSERT INTO {DBFacade.SCRATCH_BALLS}(person, times, last_scratch)
            VALUES ('{person}', 0, '0')
            """
        )
        self.__connection.commit()

    
    def add_person_to_penis(self, person: str) -> None:
        """
        Adds a new player to "scratch penis" table
        """
        self.__cursor.execute(
            f"""
            INSERT INTO {DBFacade.SCRATCH_PENIS}(person, times, last_scratch)
            VALUES ('{person}', 0, '0')
            """
        )
        self.__connection.commit()


    def delete_person_from_balls(self, person: str) -> None:
        """
        Delete person from "scratch balls" table
        """
        self.__cursor.execute(
            f"""
            DELETE FROM {DBFacade.SCRATCH_BALLS} WHERE person='{person}'
            """
        )
        self.__connection.commit()


    def delete_person_from_penis(self, person: str) -> None:
        """
        Delete person from "scratch penis" table
        """
        self.__cursor.execute(
            f"""
            DELETE FROM {DBFacade.SCRATCH_PENIS} WHERE person='{person}'
            """
        )
        self.__connection.commit()