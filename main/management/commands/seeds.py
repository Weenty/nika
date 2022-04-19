from django.core.management.base import BaseCommand
from goods.models import section
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
            ten_section = SectionFactory.create_batch(10)
            category = CaterogyFactory(section=ten_section)
            print(category)
            # SectionFactory.create()
            # CaterogyFactory.create()
            # PackageFactory.create()
            # ProductsFactory.create()
            # UsersFactory.create()
