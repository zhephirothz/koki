from django.db import models
from customers.models import Customers


class CustomerReportTemplate(models.Model):
    template_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="Template name"
    )
    customer_id = models.ForeignKey(
        Customers,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Customer name"
    )
    
    # Report Header 
    # Flag to visible header
    company = models.BooleanField(
        default=False,
        verbose_name="company"
    )
    date_full = models.BooleanField(
        default=False,
        verbose_name="Date (Full)"
    )
    date_be = models.BooleanField(
        default=False,
        verbose_name="Date (พ.ศ.)"
    )
    date_ad = models.BooleanField(
        default=False,
        verbose_name="Date (ค.ศ.)"
    )
    product_name = models.BooleanField(
        verbose_name="Product Name"
    )
    flux_no = models.BooleanField(
        verbose_name="Flux No."
    )
    lot_no = models.BooleanField(
        default=False,
        verbose_name="Lot No."
    )
    quantity_kg = models.BooleanField(
        default=False,
        verbose_name="Quantity (Kg.)"
    )
    quantity_pole = models.BooleanField(
        default=False,
        verbose_name="Quantity (แท่ง)"
    )
    quantity_roll = models.BooleanField(
        verbose_name="Quantity (ม้วน)"
    )
    product_code = models.BooleanField(
        default=False,
        verbose_name="Product Code"
    )
    manufacturing_date = models.BooleanField(
        default=False,
        verbose_name="Manufacturing Date"
    )
    expiry_date = models.BooleanField(
        default=False,
        verbose_name="Expiry Date"
    )
    part_code_project = models.BooleanField(
        default=False,
        verbose_name="Part Code Project"
    )
    po_name = models.BooleanField(
        default=False,
        verbose_name="P/O"
    )


    def __str__(self):
        return self.template_name 
