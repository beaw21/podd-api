import json
from django.core.management import BaseCommand
from django.template import Template, Context
import sys
from reports.models import Report
from reports.search_indexes import ReportIndex


class Command(BaseCommand):
    help = 'Update index for negative reports only'

    def handle(self, *args, **options):
        reports = Report.objects.filter(negative=True)
        total_reports = reports.count()
        report_index = ReportIndex()

        done_reports_count = 0

        for report in reports:
            # update elasticsearch
            report_index.update_object(report)

            done_reports_count += 1

            percent_progress = min((float(done_reports_count) / float(total_reports)) * 100, 100)
            sys.stdout.write('\r[%s] %s%% (%s/%d)' %
                             (('#' * int(percent_progress / 2)).ljust(50, ' '), int(percent_progress),
                              str(done_reports_count).rjust(10, ' '), total_reports))
            sys.stdout.flush()
