from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Empresa(models.Model):
    nome_da_empresa = models.CharField(max_length=255, default='Empresa')
    demanda_contratada = models.DecimalField(max_digits=5, decimal_places=2, default='000') #inserção dos dados de descrição
    demanda_registrada = models.DecimalField(max_digits=5, decimal_places=2, default='000') 
    consumo_ponta = models.DecimalField(max_digits=10, decimal_places=2, default='000')
    consumo_Fora_ponta = models.DecimalField(max_digits=10, decimal_places=2, default='000')
    #image = models.FileField(default=None,blank=True, upload_to='images')

    def __str__(self):
        return self.nome_da_empresa #define oque esta retornando da busca
    """


    slug = models.SlugField(blank=True, default='000')
  
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Empresa, self).save()
  
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

    """