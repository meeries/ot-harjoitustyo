from repositories.ledger_repository import LedgerRepository

class LedgerService:
    """Luokka, joka vastaa sovelluslogiikasta
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.ledger_repository = LedgerRepository()

    def deposit(self, amount, description):
        """Lisää kirjanpitoon talletuksen; summan ja kuvauksen talletukselle.
        Varmistaa, että annettu summa ei ole negatiivinen.
        """
        if int(amount) >= 0:
            self.ledger_repository.add_transaction(amount, description)
            print("Deposit added!")
        else:
            print("Please insert a positive number")

    def withdrawal(self, amount, description):
        """Lisää kirjanpitoon noston; summan ja kuvauksen nostolle.
        Varmistaa, että annettu summa ei ole negatiivinen, ja että budjetissa on varaa nostaa summa.
        """
        if int(amount) >= 0:
            if self.get_balance() - int(amount) > 0:
                self.ledger_repository.add_transaction(-int(amount), description)
                print("Withdrawal added!")
            else:
                print("Not enough balance for withdrawal.")
        else:
            print("Please insert a positive number")

    def get_balance(self):
        """Kutsuu ledger-repositorion tämänhetkisen budjetin palauttavaa metodia
        ja muuttaa sen kokonaisluvuksi
        Returns:
            tämänhetkinen budjetti kokonaislukuna"""
        return int(self.ledger_repository.get_balance()[0])

    def check_ledger(self):
        """Kutsuu ledger-repositorion tämänhetkisen kirjanpidon palauttavaa metodia
        ja muuttaa sen sanakirjaksi
        Returns:
            tämänhetkinen kirjanpito sanakirjana"""
        return [dict(x) for x in self.ledger_repository.find_all()]

    def delete_database(self):
        """Poistaa tämänhetkisen tietokannan
        """
        self.ledger_repository.delete_db()
        