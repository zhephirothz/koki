from django.db import models


class StandardSpec(models.Model):
    spec_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Spec name"
    )
    remark = models.TextField(
        blank=True,
        null=True,
        verbose_name="Remark 1",
    )
    remark2 = models.TextField(
        blank=True,
        null=True,
        verbose_name="Remark 2"
    )
    remark3 = models.TextField(
        blank=True,
        null=True,
        verbose_name="Remark 3"
    )

    # class Meta:
        # ordering = "spec_name"

    def __str__(self):
        return self.spec_name


class StandardSpecLine(models.Model):
    standard_spec_id = models.ForeignKey(
        StandardSpec,
        related_name="standard_spec",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=10,
        verbose_name="name"
    )
    # standard_name for make key unique
    standard_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Standard name"
    )
    value_text = models.CharField(
        max_length=25,
        blank=True,
        verbose_name="Value (Text)"
    )
    value = models.CharField(
        max_length=25,
        blank=True,
        verbose_name="Value",
        help_text="Use only number for calculation purpose"
    )

    class Meta:
        # ordering = "name"
        unique_together = ('standard_spec_id', 'name')

    def __str__(self):
        return self.name

