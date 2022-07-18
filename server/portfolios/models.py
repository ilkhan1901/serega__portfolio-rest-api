from django.db import models

class Portfolio(models.Model):
    title = models.CharField('Название',max_length=255) # название
    link = models.TextField('Ссылка',blank=True,null=True) # ссылка
    image = models.ImageField('Изображение',upload_to='portfolios') # изображение
    published = models.DateField('Дата публикации',auto_now_add=True) # дата публикации
    
    class Meta:
        verbose_name = 'Портфолио '