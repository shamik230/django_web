from django.db import models

# Create your models here.


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Имя")
    order_phone = models.CharField(max_length=20, verbose_name="Тел.")

    def __str__(self):
        return f"id: {self.pk}, {self.order_name}"