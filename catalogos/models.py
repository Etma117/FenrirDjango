from django.db import models

# Create your models here.
class Laptops(models.Model):
    marca = models.CharField(max_length=20)
    linea= models.CharField(max_length=40)
    modelo= models.CharField(max_length=40)
    NS = models.CharField(max_length=20, null=False, help_text="Numero de serie del producto")
    existencias= models.CharField(max_length=40)      
    #def __str__(self):
    #    return '%s - %s - %s' % (self.NS, self.marca, self.linea, self.modelo)
      
class SwPropietario(models.Model):
    RFC = models.CharField(max_length=50)
    nombre = models.CharField(max_length=30)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    email = models.EmailField()
    calle = models.CharField(max_length=50)
    colonia = models.CharField(max_length=40)
    municipio = models.CharField(max_length=40)
    numeroContacto= models.CharField(max_length=40)
    CP = models.CharField(max_length=5)
    edad = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=30)
    presupuesto = models.CharField(max_length=100)
    
    def __str__(self):
        return '%s - %s - %s' % (self.nombre, self.apPaterno, self.apMaterno)
    
                
class PlacasBase(models.Model):
    marca = models.CharField(max_length=20)
    linea= models.CharField(max_length=40)
    modelo= models.CharField(max_length=40)
    NS = models.CharField(max_length=20, null=False, help_text="Numero de serie del producto")
    
    def __str__(self):
        return "%s" % (self.nombre)
        
class Procesadores(models.Model):
    marca = models.CharField(max_length=20)
    linea= models.CharField(max_length=40)
    modelo= models.CharField(max_length=40)
    NS = models.CharField(max_length=20, null=False, help_text="Numero de serie del producto")
    
    def __str__(self):
        return "%s - %s" % (self.numero, self.vehiculo)
    