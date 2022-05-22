from django.db import models


class StandardSpec(models.Model):
    spec_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Spec name"
    )
    # spec_list = models.ManyToManyField(
        # StandardSpecLine
    # )
    # remark = models.TextField(
        # verbose_name="Remark"
    # )

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
    value_text = models.CharField(
        max_length=25,
        verbose_name="Value (Text)"
    )
    value = models.CharField(
        max_length=25,
        verbose_name="Value",
        help_text="Use only number for calculation purpose"
    )

    # class Meta:
        # ordering = "name"

    def __str__(self):
        return self.name

# class SpecSolder(models.Model):
    # spec_name = models.CharField(
        # max_length=255,
        # unique=True
    # )

    # sn_value = models.CharField(
        # max_length=25,
        # verbose_name="Sn"
    # )
    # ag_value = models.CharField(
        # max_length=25,
        # verbose_name="Ag"
    # )
    # cu_value = models.CharField(
        # max_length=25,
        # verbose_name="Cu"
    # )
    # pb_value = models.CharField(
        # max_length=25,
        # verbose_name="Pb"
    # )
    # al_value = models.CharField(
        # max_length=25,
        # verbose_name="Al"
    # )
    # as_value = models.CharField(
        # max_length=25,
        # verbose_name="As"
    # )
    # bi_value = models.CharField(
        # max_length=25,
        # verbose_name="Bi"
    # )
    # cd_value = models.CharField(
        # max_length=25,
        # verbose_name="Cd"
    # )
    # fe_value = models.CharField(
        # max_length=25,
        # verbose_name="Fe"
    # )
    # sb_value = models.CharField(
        # max_length=25,
        # verbose_name="Sb"
    # )
    # zn_value = models.CharField(
        # max_length=25,
        # verbose_name="Zn"
    # )
    # au_value = models.CharField(
        # max_length=25,
        # verbose_name="Au"
    # )
    # in_value = models.CharField(
        # max_length=25,
        # verbose_name="In"
    # )
    # ni_value = models.CharField(
        # max_length=25,
        # verbose_name="Ni"
    # )
    # ge_value = models.CharField(
        # max_length=25,
        # verbose_name="Ge"
    # )
    # p_value = models.CharField(
        # max_length=25,
        # verbose_name="P"
    # )
    # s_value = models.CharField(
        # max_length=25,
        # verbose_name="S"
    # )
    # ni_co_value = models.CharField(
        # max_length=25,
        # verbose_name="Ni + CO"
    # )
    # sn_sb_value = models.CharField(
        # max_length=25,
        # verbose_name="Sn + Sb"
    # )
    # remark = models.CharField(
        # max_length=500,
        # verbose_name="Remark"
    # )

    # # Reference
    # solidus_temperature = models.CharField(
        # max_length=25,
        # verbose_name="Solidus temperature"
    # )
    # liquidus_temperature = models.CharField(
        # max_length=25,
        # verbose_name="Liquidus temperature"
    # )
    # specific_gravity = models.CharField(
        # max_length=25,
        # verbose_name="Specific gravity"
    # )
    # iso_alloy_no = models.CharField(
        # max_length=25,
        # verbose_name="ISO alloy No."
    # )


# class SpecFlux(models.Model):
    # flux_name = models.CharField(
        # max_length=255,
        # verbose_name="Flux name"
    # )
    # halide_content = models.CharField(
        # max_length=255,
        # verbose_name="Halide content"
    # )
    # specific_gravity_20c = models.CharField(
        # max_length=255,
        # verbose_name="Specific Gravity @ 20C"
    # )
