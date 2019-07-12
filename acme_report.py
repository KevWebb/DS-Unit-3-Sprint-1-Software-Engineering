from acme import Product
import random as rand

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products(n: int=30) -> list:
    products = []
    for _ in range(n):
        name = rand.choice(ADJECTIVES) + ' ' + rand.choice(NOUNS)
        price = rand.randint(5, 100)
        weight = rand.randint(5, 100)
        flammability = rand.uniform(0, 2.5)

        products.append(Product(name, price, weight, flammability))

    return products

def inventory_report(prods: list) -> None:
    names = set()
    total_price, total_weight, total_flam = 0,0,0

    for prod in prods:
        names.add(prod.name)
        total_price += prod.price
        total_weight += prod.weight
        total_flam += prod.flammability

    print(f'Number of Unique Names: {len(names)}')
    print(f'Average Price: {total_price / len(prods)}')
    print(f'Average Weight: {total_weight / len(prods)}')
    print(f'Average Flammability: {total_flam / len(prods)}')

if __name__ == '__main__':
    inventory_report(generate_products())
