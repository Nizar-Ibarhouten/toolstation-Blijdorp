from django.db import models



class Names(models.Model):

  User_names = models.CharField(max_length=100)
  
  def __repr__(self):
    return f"{self.User_names}"
    
    
  