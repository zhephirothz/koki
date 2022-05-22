from django.db import models
from products.models import Products


class AnalysisReport(models.Model):

    analysis_report_name = models.CharField(
        max_length=255,
        verbose_name="Analysis Report name"
    )
    # Row 1 in sample report
    sample_result_name = models.CharField(
        max_length=255,
        verbose_name="Sample Result Name"
    )
    report_type = models.CharField(
        max_length=255,
        verbose_name="Type"
    )
    measure_date_time = models.CharField(
        max_length=255,
        verbose_name="Measure Date Time"
    )
    recalculation_date_time = models.CharField(
        max_length=255,
        verbose_name="Recalculation Date Time"
    )
    origin = models.CharField(
        max_length=255,
        verbose_name="Origin"
    )
    method_name = models.CharField(
        max_length=255,
        verbose_name="Method Name"
    )
    operator_name = models.CharField(
        max_length=255,
        verbose_name="Operator Name"
    )
    check_type = models.CharField(
        max_length=255,
        verbose_name="Check Type"
    )
    check_status = models.CharField(
        max_length=255,
        verbose_name="Check Status"
    )
    grade_verification_name = models.CharField(
        max_length=255,
        verbose_name="Grade Verification Name"
    )
    grade_verification_similarity = models.CharField(
        max_length=255,
        verbose_name="Grade Verification Similarity"
    )
    correction_type = models.CharField(
        max_length=255,
        verbose_name="Correction Type"
    )
    outlier_test_type = models.CharField(
        max_length=25,
        verbose_name="Outlier Test Type"
    )
    status = models.CharField(
        max_length=25,
        verbose_name="Status"
    )

    # Row 3 in sample report
    sample_name = models.CharField(
        max_length=255,
        verbose_name="Sample Name"
    )
    quality = models.CharField(
        max_length=255,
        verbose_name="Quality"
    )
    lot_no = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Lot No."
    )
    report_no = models.CharField(
        max_length=255,
        verbose_name="Report No."
    )
    sample_id = models.CharField(
        max_length=255,
        verbose_name="Sample Id."
    )
    fc = models.CharField(
        max_length=255,
        verbose_name="FC"
    )
    cc = models.CharField(
        max_length=255,
        verbose_name="CC"
    )
    diam = models.CharField(
        max_length=255,
        verbose_name="Diam"
    )
    stamp = models.CharField(
        max_length=255,
        verbose_name="Stamp"
    )

    # To store report upload date
    upload_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Upload Date"
    )

    class Meta:
        ordering = [
            '-pk',
            '-upload_date'
        ]

    def __str__(self):
        return self.sample_result_name


class AnalysisReportLine(models.Model):
    analysis_report_id = models.ForeignKey(
        AnalysisReport,
        related_name="analysis_report",
        on_delete=models.CASCADE
    )
    # 1, 2, 3, ... or Mean/SD/RSD
    analysis_type = models.CharField(
        max_length=25,
        blank=True,
        null=True
    )

    analysis_name = models.CharField(
        max_length=25
    )
    value_text = models.CharField(
        max_length=50,
        verbose_name="Value (Text)"
    )
    value = models.FloatField(
        verbose_name="Value",
        help_text="Use only number for calculation purpose"
    )
    lower_than = models.BooleanField(
        verbose_name='Lower than',
        default=False,
    )
    greater_than = models.BooleanField(
        verbose_name="Greater than",
        default=False,
    )


    class Meta:
        unique_together = [[
            'analysis_report_id',
            'analysis_type'
        ]]


# class AnalysisReport(models.Model):
    # reportfile = models.FileField(
        # upload_to=''
    # )
