

# Turismi sihtkohtade andmete haldamiseks klass Destination
class Destination:
    def __init__(self, name, country, rating, price):
        # Muutujad: nimi (tekst), riik (tekst), hinnang (liikuvkomakohaga arv), hind (täisarv)
        self.name = name
        self.country = country
        self.rating = rating
        self.price = price

    # Meetod sihtkoha info printimiseks
    def display_info(self):
        print(f"Sihtkoht: {self.name} ({self.country}), Hinnang: {self.rating}, Hind: {self.price}€")

# Turismipaketi klass, mis sisaldab sihtkohti
class TourPackage:
    def __init__(self, name):
        self.name = name
        self.destinations = []  # Massiiv sihtkohtade hoidmiseks

    # Sihtkoha lisamine paketti
    def add_destination(self, destination):
        self.destinations.append(destination)

    # Paketi info kuvamine
    def show_package_info(self):
        print(f"Turismipakett: {self.name}")
        for destination in self.destinations:
            destination.display_info()

# Muutujad
budget = 1000  # Eelarve täisarvuna
is_budget_friendly = False  # Tõeväärtus, kas pakett sobib eelarvesse

# Sihtkohad
paris = Destination("Pariis", "Prantsusmaa", 4.7, 300)
rome = Destination("Rooma", "Itaalia", 4.5, 400)
barcelona = Destination("Barcelona", "Hispaania", 4.8, 350)

# Turismipakett
europe_tour = TourPackage("Euroopa Avastus")

# Sihtkohtade lisamine paketti tsükliga
for destination in [paris, rome, barcelona]:
    europe_tour.add_destination(destination)

# Kuvame turismipaketi info
europe_tour.show_package_info()

# Tingimuslause, et kontrollida, kas pakett on eelarve-sõbralik
total_cost = sum(destination.price for destination in europe_tour.destinations)
if total_cost <= budget:
    is_budget_friendly = True
    print("See pakett sobib sinu eelarvesse!")
else:
    print("See pakett ületab sinu eelarve.")

# Prindime lõpptulemused
print(f"Paketi kogumaksumus: {total_cost}€")
print(f"Eelarve-sõbralik: {'Jah' if is_budget_friendly else 'Ei'}")
