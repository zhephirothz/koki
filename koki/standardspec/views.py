from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
import openpyxl
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from filecmp import cmp
from .models import StandardSpec, StandardSpecLine
from datetime import date
import re


class StandardSpecReportListView(ListView):
    template_name = "standardreports/standard_report_list.html"

    def get(self, request):
        report_list = StandardSpec.objects.all()

        ctx = {
            'report_list' : report_list,
        }
        return render(request, self.template_name, ctx)


class StandardSpecReportDetailView(DetailView):
    template_name = "standardreports/standard_report_detail.html"

    def get(self, request, pk):
        report_detail = StandardSpec.objects.get(pk=pk)
        report_line = report_detail.standard_spec.all()

        ctx = {
            'report_detail': report_detail,
            'report_line': report_line,
        }
        return render(request, self.template_name, ctx)


class StandardSpecReportUploadView(ListView):
    template_name = 'standardreports/standard_report_upload.html'

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
        # row_count += 1
        print(header)

        for row in csvreader:
            standardspec_obj = {}
            # Try to get an objects by spec_name
            try:
                standardspec_obj = StandardSpec.objects.get(spec_name__exact=row[0])
            except:
                pass

            # Try to create objects 
            # Check duplicate if fail then stop this method
            if not standardspec_obj:
                try:
                    standardspec_obj = StandardSpec.objects.create(
                        spec_name=row[0],
                        remark=row[20],
                        remark2=row[21],
                        remark3=row[22]
                    )
                except:
                    return False

            # Set value to standardSpecLine by standardspec_obj.id
            for row_count, row_data in enumerate(row):
                # Not get data from column 0
                if row_count != 0:
                    # print('-----')
                    # print(row_data)
                    # print('VALUE')
                    # print(re.findall("\d+\.\d+", row_data))
                    # print('-----')
                    standardspecline_obj = {}
                    # Find the same data
                    dup_key = str(standardspec_obj.id) + header[row_count]
                    try:
                        standardspecline_obj = StandardSpecLine.objects.get(
                            standard_name__exact=dup_key
                        )
                        # standardspecline_obj = StandardSpecLine.objects.get(
                            # id__exact=standardspec_obj,
                            # name__exact=header[row_count]
                        # )
                    except:
                        pass

                    if not standardspecline_obj:
                        standardspecline_obj = StandardSpecLine.objects.create(
                            standard_spec_id = standardspec_obj,
                            standard_name=dup_key,
                            name=header[row_count],
                            value_text=row_data,
                        )
                    else:
                        standardspecline_obj.value_text = row_data
                        standardspecline_obj.save()

            # standardspec_obj = 

        # Get row 5 (Analysis Line)
        # analysis_line_name = []
        # for row in csvreader:
            # if row_count == 5:
                # for line_value in row[1:]:
                    # analysis_line_name.append(line_value)
            # row_count += 1

            # # Get Mean value by evaluate
            # if row[0] == 'Mean':
                # loop_count = 0
                # for line_value in row[1:]:
                    # lower_than_flag = False
                    # greater_than_flag = False
                    # if re.findall("\<", line_value):
                        # # Flag lower_than = True
                        # lower_than_flag = True
                    # elif re.findall("\>", line_value):
                        # # Flag greater_than = True
                        # greater_than_flag = True

                    # # Create analysis line object
                    # AnalysisReportLine.objects.create(
                        # analysis_report_id=analysis_report_obj,
                        # analysis_name=analysis_line_name[loop_count],
                        # value_text=line_value,
                        # value=re.findall("\d+\.\d+", line_value)[0],
                        # lower_than=lower_than_flag,
                        # greater_than=greater_than_flag,
                    # )

                    # loop_count += 1

        dictData['report_data'] = reportData

        # return render(request, self.template_name, dictData)
        return redirect('/')


    def get(self, request) :
        ctx = {}
        return render(request, self.template_name, ctx)
