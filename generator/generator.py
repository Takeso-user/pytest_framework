from data.data import Person
from faker import Faker

faker_pl = Faker('pl_PL')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_pl.name(),
        email=faker_pl.email(domain='gmail.com'),
        current_address=faker_pl.address().replace('\n', ' '),
        permanent_address=faker_pl.address().replace('\n', ' ')
    )
