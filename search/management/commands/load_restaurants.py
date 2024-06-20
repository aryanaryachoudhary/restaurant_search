import os
from django.core.management.base import BaseCommand
from search.models import Restaurant

class Command(BaseCommand):
    help = 'Load restaurant data from CSV'

    def handle(self, *args, **kwargs):
        # Get the root directory of the project
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        file_path = os.path.join(project_root, 'restaurants_small.csv')
        Restaurant.load_data_from_csv(file_path)
        self.stdout.write(self.style.SUCCESS('Successfully loaded restaurant data'))
