from django.core.management.base import BaseCommand
from nika.factory import *



class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--all', type=int, help='Number of fake records for the database')
        parser.add_argument('--s', type=int, help='Number of fake section for the database')
        parser.add_argument('--c', type=int, help='Number of fake category for the database')
        parser.add_argument('--pa', type=int, help='Number of fake package for the database')
        parser.add_argument('--p', type=int, help='Number of fake products for the database')
        parser.add_argument('--pc',type=int, help='Number of fake relationship Product with Caterorys for the database')
        parser.add_argument('--pp', type=int, help='Number of fake relationship Products with Package for the database')



    def handle(self, *args, **options):
        if options['all']:
            for _ in range(options['all']):
                SectionFactory.create()
                # PackageFactory.create()
                # ProductHasPackagesFactory.create()
                # CombinateProductsPackageFactory.create()
                # BasketFactory.create() ЗАФИКСИТЬ
                # ProductHasSectionCategoryFactory.create()
                # ProductsWith2CategoryFactory.create()
                # ProductsWithCategoryFactory.create()
            for _ in range(options['all']):
                CategoryFactory.create()

            for _ in range(options['all']):
                PackageFactory.create()
                ProductsFactory.create()

            for _ in range(options['all']):
               CombinateProductsPackageFactory.create()

            for _ in range(options['all']):
                ProductHasSectionCategoryFactory.create()


        elif options['c']:
            for _ in range(options['c']):
                SectionFactory.create()
        elif options['s']:
            for _ in range(options['s']):
                CategoryFactory.create()
        elif options['pa']:
            for _ in range(options['pa']):
                PackageFactory.create()
        elif options['p']:
            for _ in range(options['p']):
                ProductsFactory.create()
        elif options['pc']:
            for _ in range(options['pc']):
                ProductHasSectionCategoryFactory.create()
        elif options['pp']:
            for _ in range(options['pp']):
                CombinateProductsPackageFactory.create()