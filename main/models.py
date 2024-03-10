from django.db import models



    
class Books(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.CharField(max_length=50)

    def __str__(self):
        
        return self.title
    

