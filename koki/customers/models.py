from django.db import models


class Customers(models.Model):
    customer_code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Customer code"
    )
    customer_name = models.CharField(
        max_length=255,
        verbose_name="Customer name"
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Is active?"
    )

    def __str__(self):
        return self.customer_name
