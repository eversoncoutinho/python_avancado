from django.db import models

class Categoria (models.Model):
    titulo = models.CharField(max_length=20, blank=True, null=True)    
        
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['titulo']#serve para ordenar em ordem crescente
                            # em ordem decrescente ['-titulo']

class Anuncio (models.Model):
    titulo=models.CharField(max_length=20, blank=True, null=True)
    descricao=models.TextField(("Descrição"))
    preco= models.DecimalField(("Preço"), max_digits=999, decimal_places=2)
    categoria= models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    data_da_criacao=models.DateField(("Data"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.titulo
    
