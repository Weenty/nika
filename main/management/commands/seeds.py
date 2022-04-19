from django.core.management.base import BaseCommand
from nika.factory import *

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
    
    
    