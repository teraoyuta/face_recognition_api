from django.db import models

# Create your models here.

class Face(models.Model):
    user_name = models.CharField(max_length=100)
    block_width = models.IntegerField()
    block_height = models.IntegerField()
    vector = models.BinaryField()

    class Meta:
        db_table = 'faces'
