

# Selles koodiplokis luuakse klass Destination , mis haldab nime. riigi nime, hinnagut ja hinda . Muutujad algavad self objektiga.
class Destination:
    def __init__(self, name, country, rating, price):
        # Muutujad: nimi (tekst), riik (tekst), hinnang (liikuvkomakohaga arv), hind (täisarv)
        self.name = name
        self.country = country
        self.rating = rating
        self.price = price

    # Defineerib klassile destination meetodi nimega display_info ja prindib välja.
    def display_info(self):
        print(f"Sihtkoht: {self.name} ({self.country}), Hinnang: {self.rating}, Hind: {self.price}€")

# Koodiplokk klass nimega TourPackage esindab reispaketti. init abil määratakse klassi omadused. []-tühi nimekiri kuhu hiljem saab määrata sihtkoha.
class TourPackage:
    def __init__(self, name):
        self.name = name
        self.destinations = []  # Massiiv sihtkohtade hoidmiseks

    # Defineerib klass TourPackge meetodi add_destination, mille abil saab määrata sihtkoha reisipaketti
    def add_destination(self, destination):
        self.destinations.append(destination)

    # Koodiplokk defineerib TourPackage klassi meetodi ,mis kuvab terve reisipaketi info. Kasutatakse for tsüklit ja kuvatakse sihtkoha detailid.
    # f stringiga prinditakse välja reisipaketi nimi 
    # For tüskliga tsüklitakse välja sihtkohade ni
    def show_package_info(self):
        print(f"Turismipakett: {self.name}")
        for destination in self.destinations:
            destination.display_info()

# Muutujad, määratakse eelarve summa ja boolean kontrollib kas on eelarve sõbralik. Hetkel on määratud tõeväärtus false.
budget = 1000  # Eelarve täisarvuna
is_budget_friendly = False  

# Sihtkohad , kolm objekti mis esindavad kolme erinevat sihtkohta. Sihtkoht sisaldab asukoha nime hinnagut ja hinda.
paris = Destination("Pariis", "Prantsusmaa", 4.7, 300)
rome = Destination("Rooma", "Itaalia", 4.5, 400)
barcelona = Destination("Barcelona", "Hispaania", 4.8, 350)

# Luuakse objekt europe_tour klassist TourPackage mis esindab nimega "Euroopa Avastus"
europe_tour = TourPackage("Euroopa Avastus")

# Kasutatakse for tsüklit et lisada sihtkohad europe-tour reisipaketti.
for destination in [paris, rome, barcelona]:
    europe_tour.add_destination(destination)

# Kuvatakse europe_tour reisipaketi info.
europe_tour.show_package_info()

# Arvutatakse reisipaketi europe_toru kogusumma ja kontrollitakse kas eelarve jääb reisipaketi piiresse, seejärel pinditakse kas sobib või ei sobi.
total_cost = sum(destination.price for destination in europe_tour.destinations)
if total_cost <= budget:
    is_budget_friendly = True
    print("See pakett sobib sinu eelarvesse!")
else:
    print("See pakett ületab sinu eelarve.")

# Prinditakse reispaketi kogumaksumus ja kas see vastab kasutaja eelarvele. 
print(f"Paketi kogumaksumus: {total_cost}€")
print(f"Eelarve-sõbralik: {'Jah' if is_budget_friendly else 'Ei'}")
