from django.db import models



class Names(models.Model):

  User_names = models.CharField(max_length=100)
  
  
  def __repr__(self):
    return f"{self.User_names}"
    
    
class hardwareproducts(models.Model):

  Naam = models.CharField(max_length=100)
  Gewicht  = models.CharField(max_length=100)
  Prijs_inc_btw = models.CharField(max_length=100)
  Kwantiteit = models.CharField(max_length=100)
  Beschrijving = models.CharField(max_length=100)
  

  def __repr__(self):
    return f"{self.Naam,self.Gewicht,self.Prijs_inc_btw,self.Kwantiteit,self.Beschrijving}"
    