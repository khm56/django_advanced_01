from django.db import models
from stores.models import Store

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, default=1, on_delete=models.CASCADE)
    is_empty= models.BooleanField(default=True)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.name