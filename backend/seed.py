from app import create_app, db
from app.models.coin import Coin

# Tworzenie aplikacji
app = create_app()

# Dodawanie przykładowych danych
with app.app_context():
    db.create_all()  # Tworzy tabele w bazie danych

    # Przykładowe dane
    coins = [
        Coin(
            name="US Flag",
            description="American flag coin from 2020.",
            price=5.75,
            year_issued=2020,
            country="USA",
            quantity_available=200,
            image_url="/assets/us.svg"
        ),
        Coin(
            name="British Queen",
            description="Coin commemorating the British Queen.",
            price=12.00,
            year_issued=2019,
            country="UK",
            quantity_available=150,
            image_url="/assets/british_queen.svg"
        ),
        Coin(
            name="Australian Kangaroo",
            description="Coin featuring a kangaroo from Australia.",
            price=8.50,
            year_issued=2018,
            country="Australia",
            quantity_available=120,
            image_url="/assets/australian_kangaroo.svg"
        )
    ]

    # Dodaj znaczniki do bazy
    db.session.add_all(coins)
    db.session.commit()

    print("Dane testowe zostały dodane do bazy.")
