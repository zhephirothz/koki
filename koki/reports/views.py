from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.db.models import Q
from .models import AnalysisReport
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import openpyxl
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from filecmp import cmp
from .models import AnalysisReport, AnalysisReportLine
from datetime import date
import re


class AnalysisReportListView(ListView):
    template_name = "reports/report_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(firstname__icontains=strval)
            report_list = AnalysisReport.objects.filter(query).select_related().distinct()[:10]
        else :
            report_list = AnalysisReport.objects.all().order_by('-id')

        ctx = {
            'report_list' : report_list,
            'search': strval
        }
        return render(request, self.template_name, ctx)


class AnalysisReportDetailView(DetailView):
    template_name = "reports/report_detail.html"

    def get(self, request, pk):
        report_detail = AnalysisReport.objects.get(pk=pk)
        report_line = report_detail.analysis_report.all()

        ctx = {
            'report_detail': report_detail,
            'report_line': report_line,
        }
        return render(request, self.template_name, ctx)


class AnalysisReportUploadView(ListView):
    template_name = 'reports/report_upload.html'

    def post(self, request):
        print("POST")
        dictData = {}
        reports_file = request.FILES["reports_file"]
        MEDIA_PATH = settings.MEDIA_ROOT
        fs = FileSystemStorage(location=settings.MEDIA_ROOT) #defaults to   MEDIA_ROOT  
        filename = fs.save(reports_file.name, reports_file)
        file_url = settings.MEDIA_ROOT + '/' + filename
        reportData = {}

        file = open(file_url, "r", encoding="ISO-8859-1")
        csvreader = csv.reader(file)
        header = []
        row_count = 1

        # Get header
        header = next(csvreader)
        row_count += 1

        # Filter header max index number
        header_column_index = 0
        for h in header:
            if h == '':
                break
            header_column_index += 1

        # Set header value only row 2 and 4 (header included)
        reportData = {}
        loop_count = 0
        for row in csvreader:
            # Column count use in loop
            column_count = 0
            # Get column 2 to set header
            if row_count == 2 or row_count == 4:
                for hci in range(header_column_index):
                    index_number = (loop_count * header_column_index) + column_count
                    reportData[index_number] = row[hci]
                    column_count += 1
                loop_count += 1
            row_count += 1
            # Get only header then break
            if row_count > 4:
                break

        # Create Header data
        # loop thru reportData and insert in .create()
        # for rd in reportData:
        analysis_report_obj = AnalysisReport.objects.create(
            analysis_report_name=request.POST['reports_title'],
            sample_result_name=reportData[0],
            report_type=reportData[1],
            measure_date_time=reportData[2],
            recalculation_date_time=reportData[3],
            origin=reportData[4],
            method_name=reportData[5],
            operator_name=reportData[6],
            check_type=reportData[7],
            check_status=reportData[8],
            grade_verification_name=reportData[9],
            grade_verification_similarity=reportData[10],
            correction_type=reportData[11],
            outlier_test_type=reportData[12],
            status=reportData[13],
            sample_name=reportData[14],
            quality=reportData[15],
            # lot_no=reportData[16],
            report_no=reportData[17],
            sample_id=reportData[18],
            fc=reportData[19],
            cc=reportData[20],
            diam=reportData[21],
            stamp=reportData[22],
        )

        # Get row 5 (Analysis Line)
        analysis_line_name = []
        for row in csvreader:
            if row_count == 5:
                for line_value in row[1:]:
                    analysis_line_name.append(line_value)
            row_count += 1

            # Get Mean value by evaluate
            if row[0] == 'Mean':
                loop_count = 0
                for line_value in row[1:]:
                    lower_than_flag = False
                    greater_than_flag = False
                    if re.findall("\<", line_value):
                        # Flag lower_than = True
                        lower_than_flag = True
                    elif re.findall("\>", line_value):
                        # Flag greater_than = True
                        greater_than_flag = True

                    # Create analysis line object
                    AnalysisReportLine.objects.create(
                        analysis_report_id=analysis_report_obj,
                        analysis_name=analysis_line_name[loop_count],
                        value_text=line_value,
                        value=re.findall("\d+\.\d+", line_value)[0],
                        lower_than=lower_than_flag,
                        greater_than=greater_than_flag,
                    )

                    loop_count += 1

        dictData['report_data'] = reportData

        return render(request, self.template_name, dictData)


    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            query = Q(firstname__icontains=strval)
            report_list = AnalysisReport.objects.filter(query).select_related().distinct()[:10]
        else :
            report_list = AnalysisReport.objects.all()[:10]

        ctx = {
            'report_list' : report_list,
            'search': strval
        }
        return render(request, self.template_name, ctx)
