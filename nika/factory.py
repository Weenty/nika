from datetime import datetime
import factory  
import factory.django
from random import randint
from faker import Faker
from goods.models import products, caterogy, section, package, image
from main.models import users, basket
fake = Faker()

class SectionFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = section
    name = factory.Sequence(lambda n: "section #%s" % n)

class CaterogyFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = caterogy
    name = factory.Sequence(lambda n: "сaterogy #%s" % n)

    @factory.post_generation
    def section(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for section in extracted:
                self.section.add(section)


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = image
    image = factory.django.ImageField(color='blue')

class PackageFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = package
    name = factory.Faker('sentence', nb_words=2)
    cost = fake.pydecimal(3,3)
    quantity = randint(1, 50)
    image = factory.SubFactory(ImageFactory)


class ProductsFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = products
    name = factory.Faker('sentence', nb_words=3)
    discription = factory.Faker('sentence', nb_words=20)
    discount = randint(0,50)
    purpose = factory.Faker('sentence', nb_words=20)
    brand = factory.Faker('sentence', nb_words=2)
    manufacturer = factory.Faker('last_name')
    best_before_date = factory.LazyFunction(datetime.now)
    composition = factory.Faker('sentence', nb_words=10)
    rating = randint(0,10)
    number_of_views = randint(0,20)
    package = factory.Iterator(package.objects.all())

    @factory.post_generation
    def сaterogy(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.сaterogy.add(group)



class BasketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = basket
    products = factory.SubFactory(ProductsFactory)
    quantity = randint(0, 50)
    ordered = 0
    
class UsersFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = users
    password = 'fsmoifejWSidfjw934253'
    username = factory.Faker('sentence', nb_words=1)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = 1
    date_joined = factory.LazyFunction(datetime.now)
    phone_number = factory.Faker('phone_number')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())
    basket = factory.SubFactory(BasketFactory)