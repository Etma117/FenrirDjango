from django.db import models

# Create your models here.
class Productos(models.Model):
    marca = models.CharField(max_length=20)
    nombre= models.CharField(max_length=40)
    categoria = models.CharField(max_length=20)
    modelo= models.CharField(max_length=40)
    descripcion= models.CharField(max_length = 100)
    NS = models.CharField(max_length=20, null=False, help_text="Numero de serie del producto")
    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    #imagen = models.ImageField(upload_to='productos/', null=True, blank=True)      
    #def __str__(self):
    #    return '%s - %s - %s' % (self.NS, self.marca, self.linea, self.modelo)
