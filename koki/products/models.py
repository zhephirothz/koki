from django.db import models


class Products(models.Model):
    lot_no = models.CharField(
        max_length=50,
        primary_key=True,
        unique=True,
        verbose_name="Lot NO."
    )
    product_name = models.CharField(
        max_length=255,
        verbose_name="Product name"
    )
    product_code = models.CharField(
        max_length=255,
        verbose_name="Product code"
    )
    part_code = models.CharField(
        max_length=255,
        verbose_name="Part code"
    )

    def __str__(self):
        return self.lot_no
