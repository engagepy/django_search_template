from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from product.models import Category, Tag, Manufacturer, Product

class Command(BaseCommand):
    help = 'Load demo data into the models'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of demo data entries to create for each model')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        # Demo data for Category
        categories = ['Electronics', 'Fashion', 'Home', 'Toys', 'Automotive', 'Health & Beauty']
        for name in categories:
            Category.objects.create(name=name)

        # Demo data for Tag
        tags = ['New', 'Sale', 'Featured', 'Bestseller']
        for name in tags:
            Tag.objects.create(name=name)

        # Demo data for Manufacturer
        manufacturers = ['Apple', 'Samsung', 'Sony', 'LG', 'Nike', 'Adidas']
        for name in manufacturers:
            Manufacturer.objects.create(name=name)

        # Demo data for Product
        for _ in range(total):
            product_name = f"Product {get_random_string(10)}"
            product_description = f"Description for {product_name}"
            category = Category.objects.order_by('?').first()
            manufacturer = Manufacturer.objects.order_by('?').first()

            product = Product(name=product_name, description=product_description, category=category, manufacturer=manufacturer)
            product.save()

            tags = Tag.objects.order_by('?')[:2]
            product.tags.set(tags)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} demo data entries for each model'))
