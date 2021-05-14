from django.db import models

# Create your models here.
class Dados(models.Model):
    casos_confirmados =  models.IntegerField()
    mortes = models.IntegerField()
    recuperados = models.IntegerField()
    pais = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s %s %s' % (self.casos_confirmados, self.mortes, self.recuperados, self.pais)

    class Meta:
        db_table = 'dados'
        
