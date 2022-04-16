from django.core.management.base import BaseCommand
from nika.factory import SectionFactory, CaterogyFactory, PackageFactory, ProductsFactory, UsersFactory, ImageFactory, BasketFactory

class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--all',
            default=50,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['all']):
            SectionFactory.create()
            CaterogyFactory.create()
            PackageFactory.create()
            ImageFactory.create()
            BasketFactory.create()
            ProductsFactory.create()
            UsersFactory.create()
