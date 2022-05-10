from db import database_connection
from db import initialize_database

class LedgerRepository:
    """Tämä luokka vastaa budjetin ja kirjanpidon tallennuksesta ja
    hakee tarvittavat tiedot tietokannasta.
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.connection = database_connection.get_database_connection()
        self.cursor = self.connection.cursor()

    def find_all(self):
        """Palauttaa kaikki toimeksiannot
        Returns:
            Palauttaa listan summia ja niiden kuvaukset
            """
        initialize_database.initialize_database()
        return self.cursor.execute('select * from ledger').fetchall()

    def add_transaction(self, amount, description):
        """Lisää toimeksiannon kirjanpitoon
        """
        initialize_database.initialize_database()
        self.cursor.execute('insert into ledger values (?,?,?)', (None, amount, description))
        self.connection.commit()

    def get_balance(self):
        initialize_database.initialize_database()
        """Palauttaa tämänhetkisen budjetin
        Returns:
            Palauttaa luvun, joka vastaa sen hetkistä budjettia
            """
        return self.cursor.execute('select sum(amount) from ledger').fetchone()

    def delete_db(self):
        """Poistaa tämänhetkisen tietokannan
        """
        self.cursor.execute('drop table if exists ledger')
        