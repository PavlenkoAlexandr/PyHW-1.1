class Animal:
    weight = 1 #kg
    compare_list = []

    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
        Animal.compare_list.append(self)

    def make_noise(self, noise):
        print(f'{self.kind} {self.name} говорит: "{noise}".')

    def feed(self, food_weight):
        self.weight += food_weight

    def harvest(self, product, number, measurement):
        print(f'Собран ресурс {product} в количестве {number} {measurement}')


goose_1 = Animal('Гусь', 'Серый')
goose_1.weight = 3
goose_1.make_noise('Га-га-га')
goose_1.feed(0.1)

print('')

goose_2 = Animal('Гусь', 'Белый')
goose_2.weight = 2
goose_2.make_noise('Га-га-га')
goose_2.feed(0.1)
goose_2.harvest('Яйцо', 1, 'шт.')

print('')

cow = Animal('Корова', 'Манька')
cow.weight = 500
cow.make_noise('Му-у-у-у')
cow.feed(5)
cow.harvest('Молоко', 10, 'л.')

print('')

sheep_1 = Animal('Овца', 'Барашек')
sheep_1.weight = 120
sheep_1.make_noise('Ме-е-е-е')
sheep_1.feed(2)
sheep_1.harvest('Шерсть', 6, 'кг.')

print('')

sheep_2 = Animal('Овца', 'Кудрявый')
sheep_2.weight = 100
sheep_2.make_noise('Ме-е-е-е')
sheep_2.feed(1)
sheep_2.harvest('Шерсть', 5, 'кг.')

print('')

chicken_1 = Animal('Кура', 'Ко-Ко')
chicken_1.weight = 1
chicken_1.make_noise('Ко-ко-ко')
chicken_1.feed(0.1)
chicken_1.harvest('Яйцо', 1, 'шт.')

print('')

chicken_2 = Animal('Кура', 'Кукареку')
chicken_2.weight = 2
chicken_2.make_noise('Ку-ка-ре-ку')
chicken_2.feed(0.1)

print('')

goat_1 = Animal('Коза', 'Рога')
goat_1.weight = 100
goat_1.make_noise('Ме-е-е-е')
goat_1.feed(1)
goat_1.harvest('Молоко', 5, 'л.')

print('')

goat_2 = Animal('Коза', 'Копыта')
goat_2.weight = 80
goat_2.make_noise('Ме-е-е-е')
goat_2.feed(1)
goat_2.harvest('Молоко', 4, 'л.')

print('')

duck = Animal('Утка', 'Кряква')
duck.weight = 3
duck.make_noise('Кря-кря-кря')
duck.feed(0.1)
duck.harvest('Яйцо', 1, 'шт.')

print('')

def weight_count():
    weight_sum = sum([animal.weight for animal in Animal.compare_list])
    return weight_sum

print(f'Общий вес животных {weight_count():.2f} кг.\n')

def weight_compare():
    weight_max = max([animal.weight for animal in Animal.compare_list])
    animal = [animal.name for animal in Animal.compare_list if animal.weight == weight_max]
    return animal

print(f'Самое тяжелое животное: {weight_compare()[0]}')