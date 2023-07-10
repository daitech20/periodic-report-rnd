import xlsxwriter
from datetime import date
from report.models import (
    Personnel,
    Bug,
    ProjectReport,
    Nsns,
    KpiOkr,
    EmergingIssues,
    TimeOff,
    NextWeekPlan
)


def export_to_xlsx(time: date, io):
    bugs = Bug.objects.filter(time=time)
    project_report = ProjectReport.objects.filter(time=time)
    nsns = Nsns.objects.filter(time=time)
    kpi_okr = KpiOkr.objects.get(time=time)
    emerging_issues = EmergingIssues.objects.get(time=time)
    timeoff = TimeOff.objects.filter(time=time)
    nextweek_plan = NextWeekPlan.objects.get(time=time)

    
    # Nhân sự sheet
    report = xlsxwriter.Workbook(io)
    personnel_sheet = report.add_worksheet('Nhân sự')
    bold = report.add_format({'bold': True})
    date = report.add_format({'num_format': 'yy/mm/dd'})
    personnel_sheet.write('A1', 'Thời gian', bold)
    personnel_sheet.write('B1', 'Tổng CBNV/ quota', bold)
    personnel_sheet.write('C1', 'Số nhân sự in', bold)
    personnel_sheet.write('D1', 'Số nhân sự out', bold)
    personnel_sheet.write('E1', 'Tỉ lệ nghỉ việc <20% (2NS/1NĂM)', bold)
    personnel_sheet.write('F1', 'WFO-WFH', bold)
    personnel_sheet.write('G1', 'Tình hình sức khỏe', bold)

    personnel_fields = Personnel.objects.values_list(
        'time__time',
        'personnel_of_quota',
        'personnel_in',
        'personnel_out',
        'resignation_rate',
        'wfo_wfh',
        'health_status'
    ).get(time=time)
    col = 0
    for personnel in personnel_fields:
        if col == 0:
            personnel_sheet.write(1, col, personnel, date)
        else:
            personnel_sheet.write(1, col, personnel)
        col+=1


    report.close()