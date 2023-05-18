from gui.main_window import MainWindow
from database.db_manager import db_init


if __name__ == '__main__':
    # Inicijalizacija baze
    db_init()
    
    # Dodavanje osnovnih vrijednosti u bazu -> DbSeed()
    # Eventualna provjera jesu li senzori aktivni

    m    my_main_window = MainWindow()
