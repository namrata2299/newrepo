from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    book_publication = models.CharField(max_length=30)
    book_qty= models.IntegerField()
    book_price = models.FloatField()

    class Meta:
        db_table="book_details"