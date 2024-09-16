from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    
    class Meta:
        db_table = 'clients'  # Custom table name

    def __str__(self):
        return self.name
