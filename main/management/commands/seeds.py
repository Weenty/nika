from django.core.management.base import BaseCommand
<<<<<<< HEAD
from nika.factory import *
=======
from goods.models import section
from nika.factory import SectionFactory, CaterogyFactory, PackageFactory, ProductsFactory, UsersFactory, ImageFactory, BasketFactory
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--all', type=int, help='Number of fake records for the database')
        parser.add_argument('--section', type=int, help='Number of fake section for the database')
        parser.add_argument('--category', type=int, help='Number of fake category for the database')
        parser.add_argument('--package', type=int, help='Number of fake package for the database')
        parser.add_argument('--products', type=int, help='Number of fake products for the database')
        parser.add_argument('--users',type=int, help='Number of fake users for the database')
        parser.add_argument('--productcategory',type=int, help='Number of fake relationship Product with Caterorys for the database')
        parser.add_argument('--productpackage', type=int, help='Number of fake relationship Products with Package for the database')

    def handle(self, *args, **options):
<<<<<<< HEAD
        if options['all']:
            for _ in range(options['all']):
                SectionFactory.create()
                CategoryFactory.create()
                PackageFactory.create()
                ProductsFactory.create()
                ProductHasSectionCategoryFactory.create()
                ProductsWith2PackageFactory.create()
                UsersFactory.create()
                # ProductsWith2CategoryFactory.create()
                # ProductsWithCategoryFactory.create()
        if options['category']:
            for _ in range(options['category']):
                SectionFactory.create()
        if options['section']:
            for _ in range(options['section']):
                CategoryFactory.create()
        if options['package']:
            for _ in range(options['package']):
                PackageFactory.create()
        if options['products']:
            for _ in range(options['products']):
                ProductsFactory.create()
        if options['productcategory']:
            for _ in range(options['productcategory']):
                ProductHasSectionCategoryFactory.create()
        if options['productpackage']:
            for _ in range(options['package']):
                ProductsWith2PackageFactory.create()
        if options['users']:
            for _ in range(options['users']):
                UsersFactory.create()
    
    
    
=======
        for _ in range(options['all']):
            ten_section = SectionFactory.create_batch(10)
            category = CaterogyFactory(section=ten_section)
            print(category)
            # SectionFactory.create()
            # CaterogyFactory.create()
            # PackageFactory.create()
            # ProductsFactory.create()
            # UsersFactory.create()
>>>>>>> fa624badf8fe4786d7c2ec3ce20398ac2f1a89aa
