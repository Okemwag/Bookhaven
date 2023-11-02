from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Books'


class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
    
    class Meta:
        ordering = ['due_back']
        verbose_name_plural = 'Book Instances'
        permissions = (
            ('can_mark_returned', 'Set book as returned'),
        )
        
        
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    reviewer = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.book.title} ({self.reviewer.username})'
    
    
    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Reviews'