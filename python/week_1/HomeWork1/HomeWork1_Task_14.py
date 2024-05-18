# Kreirati program za procjenu cijene stana. Na ukupnu cijenu najviše utiču sledeći
# parametrI: njegova veličina, lokacija (5 puta više nego veličina) i dostupnost parkinga (10
# puta više nego lokacija). Cijena kvadrata je 1200e. Fiksna cijena učešća je 1000e. Sve
# vrijednosti varijabli se mogu pretvoriti u numeričke. (parking ima = 1, parking nema = 0;
# zona 1 = 3, zona 2 =2, zona 3 = 1)


def flat_price(area, location, parking):
    price_squremeter = 1200
    fixed_price = 1000

    location_factor = 5
    parking_factor = 10

    price = (
        (area * price_squremeter)
        + (location * location_factor * price_squremeter)
        + (parking * parking_factor * location_factor * price_squremeter)
        + fixed_price
    )
    return price


location = {"zone1": 3, "zone2": 2, "zone3": 1}

flat_area = float(input("Enter area of the flat (m^2): "))
enter_location = input("Enter location of the flat (zone1/zone2/zone3): ").lower()
parking = int(input("Is there parking? (1 - yes, 0 - no): "))

location_factor = location.get(enter_location, 0)
price = flat_price(flat_area, location_factor, parking)

print("Price of the flat:", price, "eura.")
