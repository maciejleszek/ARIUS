from app import create_app, db
from app.models.stamp import Stamp

# Tworzenie aplikacji
app = create_app()

# Dodawanie przykładowych danych
with app.app_context():
    db.create_all()  # Tworzy tabele w bazie danych

    # Przykładowe dane
    stamps = [
        Stamp(
            name="US Flag",
            description="American flag stamp from 2020.",
            price=5.75,
            year_issued=2020,
            country="USA",
            quantity_available=200,
            image_url="/assets/us.svg"
        ),
        Stamp(
            name="British Queen",
            description="Stamp commemorating the British Queen.",
            price=12.00,
            year_issued=2019,
            country="UK",
            quantity_available=150,
            image_url="/assets/british_queen.svg"
        ),
        Stamp(
            name="Australian Kangaroo",
            description="Stamp featuring a kangaroo from Australia.",
            price=8.50,
            year_issued=2018,
            country="Australia",
            quantity_available=120,
            image_url="/assets/australian_kangaroo.svg"
        )
    ]

    # Dodaj znaczniki do bazy
    db.session.add_all(stamps)
    db.session.commit()

    print("Dane testowe zostały dodane do bazy.")
