import datetime


class DateFormat():
    @classmethod
    def convert_date(self,date):
        return datetime.datetime.strftime(date, '%D%m%Y')