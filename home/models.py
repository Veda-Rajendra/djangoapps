from django.db import models
import uuid

# Create your models here.
class book(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,help_text='unique id')
    
    book_name=models.CharField(max_length=100,help_text='Book Name',null=True)
    author_name=models.ForeignKey('author',on_delete=models.SET_NULL,help_text='book author',null=True)
    timestamp=models.DateField(auto_now=True,blank=True)
    date=models.DateField(auto_now=True,null=True)
    
    def __str__(self):
        return self.book_name

class author(models.Model):
    #id=models.AutoField(primary_key=True)
    author_name=models.CharField(max_length=100,help_text='Author Name',null=True)
    numChoice=(
        ('1','one'),
        ('2','two'),
        ('3','three'),
        ('4','four'),
    )
    date_of_birth=models.DateField('birth',null=True,blank=True)
    book_number=models.IntegerField(help_text='Book number',null=True)

    def __str__(self):
        return self.author_name

class genre(models.Model):
    
    name=models.CharField(max_length=100,help_text='Book Name',null=True)
    book_author=models.CharField(max_length=100,help_text='Book author',null=True)

    def __str__(self):
        return self.name +'-'+ self.book_author
