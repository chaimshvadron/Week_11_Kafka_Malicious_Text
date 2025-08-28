from datetime import datetime

class DateProcessor:

    def __init__(self):
        self.format = "%d-%m-%Y"

    def get_dates_in_text(self, text):
        list_date = []
        matches = text
        for match in matches.split():
            try:
                datetime.strptime(match, self.format)
                list_date.append(match)
            except ValueError:
                pass
        if list_date:
            return list_date
        return None

    def get_latest_date(self, dates_list):
        return max(dates_list)

    def process(self, text):
        dates = self.get_dates_in_text(text)
        if dates:
            date = self.get_latest_date(dates)
            return date
        return None


#
#
#
