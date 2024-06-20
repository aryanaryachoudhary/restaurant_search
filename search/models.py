from django.db import models
import json

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.JSONField()
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def load_data_from_csv(file_path):
        import csv
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items = json.loads(row['items'])
                Restaurant.objects.create(
                    name=row['name'],
                    location=row['location'],
                    items=items,
                    lat_long=row['lat_long'],
                    full_details=row['full_details']
                )
