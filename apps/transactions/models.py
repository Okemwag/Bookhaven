from django.db import models
from catalogue.models import Book
from django.utils import timezone

# Create your models here.

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_due = models.DateTimeField()
    date_returned = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.book.title} ({self.borrower.username})'
    
    
    class Meta:
        ordering = ['-date_borrowed']
        verbose_name_plural = 'Transactions'
        permissions = (
            ('can_mark_returned', 'Set book as returned'),
        )