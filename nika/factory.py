import datetime
import factory
import factory.fuzzy
from django.utils.timezone import now
import factory.django
from goods.models import *
from main.models import users, basket

class SectionFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = section_and_caterogy
    name = factory.Faker('sentence', nb_words=2)

class CategoryFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = section_and_caterogy
    parent = factory.fuzzy.FuzzyChoice(section_and_caterogy.objects.filter(parent__isnull = True))
    name = factory.Faker('sentence', nb_words=2)

class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = image
    image = factory.django.ImageField(color='blue')

class PackageFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = package
    name = factory.Faker('sentence', nb_words=2)
    cost = factory.Faker('pyint', min_value=0, max_value=10000)
    quantity = factory.Faker('pyint', min_value=0, max_value=50)
    image = factory.SubFactory(ImageFactory)


class RatingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = rating
    rating = factory.Faker('pyint', min_value=0, max_value=10)


class ProductsFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = products
    name = factory.Faker('sentence', nb_words=3)
    discription = factory.Faker('sentence', nb_words=20)
    discount = factory.Faker('pyint', min_value=0, max_value=50)
    purpose = factory.Faker('sentence', nb_words=20)
    brand = factory.Faker('sentence', nb_words=2)
    manufacturer = factory.Faker('last_name')
    best_before_date = factory.fuzzy.FuzzyDate(datetime.datetime.now().date())
    composition = factory.Faker('sentence', nb_words=10)
    rating = factory.SubFactory(RatingFactory)
    number_of_views = factory.Faker('pyint', min_value=0, max_value=20)
    
class UsersFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = users
    password = 'fsmoifejWSidfjw934253'
    username = factory.Faker('sentence', nb_words=1)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = 1
    date_joined = factory.LazyFunction(now)
    phone_number = factory.Faker('phone_number')
    email = factory.LazyAttribute(lambda a: '{}.{}@example.com'.format(a.first_name, a.last_name).lower())

class ProductHasPackagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = product_has_packages
    product = factory.SubFactory(ProductsFactory)
    package = factory.SubFactory(PackageFactory)

# def searchProduct(object):
#     return product_has_packages.objects.filter(package = object)

# class BasketFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = basket
#     user = factory.SubFactory(UsersFactory)
#     package = factory.fuzzy.FuzzyChoice(PackageFactory)
#     products = factory.fuzzy.FuzzyChoice(searchProduct(package.getter.id))
#     quantity = factory.Faker('pyint', min_value=0, max_value=50)
#     ordered = 0
# ЭТУ ШТУКУ ЗАФИКСИТЬ

class CombinateProductsPackageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = product_has_packages
    product = factory.fuzzy.FuzzyChoice(products.objects.all())
    package = factory.fuzzy.FuzzyChoice(package.objects.all())

class ProductHasSectionCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = product_has_section_and_category
    product = factory.fuzzy.FuzzyChoice(products.objects.all())
    section_and_caterogy = factory.fuzzy.FuzzyChoice(section_and_caterogy.objects.filter(parent__isnull = False))

################ ProductsWithCategoryFactory ##################

class ProductsWithCategoryFactory(ProductsFactory):
    membership = factory.RelatedFactory(
        ProductHasSectionCategoryFactory,
        factory_related_name='product',
    )

class ProductsWith2CategoryFactory(ProductsFactory):
    membership1 = factory.RelatedFactory(
        ProductHasSectionCategoryFactory,
        factory_related_name='product',
        group__name='section_and_caterogy1',
    )
    membership2 = factory.RelatedFactory(
        ProductHasSectionCategoryFactory,
        factory_related_name='product',
        group__name='section_and_caterogy2',
    )


################ ProductWithPackagesFactory ##################


class ProductsWith2PackageFactory(ProductsFactory):
    membership1 = factory.RelatedFactory(
        ProductHasPackagesFactory,
        factory_related_name='product',
        group__name='package1',
    )
    membership2 = factory.RelatedFactory(
        ProductHasPackagesFactory,
        factory_related_name='product',
        group__name='package2',
    )
