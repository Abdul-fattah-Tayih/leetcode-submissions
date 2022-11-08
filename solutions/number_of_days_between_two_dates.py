"""
Question 1360
Number of Days Between Two Dates
O(n)
"""
class NumberOfDaysBetweenTwoDates:
    MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    """
        The methodology here is to a timestamp that is similar to a unix timestamp, 
        which is the number of days since 1970 (since the question specifically includes dats from 1970 to 2100)
        and just subtract the total days from each other, we need to account for leap years in that as well
    """
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 == date2:
            return 0

        date1_year, date1_month, date1_day = map(int, date1.split('-'))
        date2_year, date2_month, date2_day = map(int, date2.split('-'))

        date1_timestamp = self.getUnixTimeStamp(date1_year, date1_month, date1_day)
        date2_timestamp = self.getUnixTimeStamp(date2_year, date2_month, date2_day)

        return max(date1_timestamp, date2_timestamp) - min(date1_timestamp, date2_timestamp)

    def getUnixTimeStamp(self, year, month, day) -> int:
        timestamp = 0

        for current_year in range(1970, year):
            if self.isLeapYear(current_year):
                timestamp += 366
            else:
                timestamp += 365

        for current_month in range(month - 1):
            timestamp += self.MONTH_DAYS[current_month]

        if self.isLeapYear(year) and (month > 2 or (month == 2 and day == 29)):
            timestamp += 1

        return timestamp + day

    def isLeapYear(self, year) -> bool:
        return (year % 100 and not year % 4) or not year % 400

if __name__ == '__main__':
    object = NumberOfDaysBetweenTwoDates()

    print(object.daysBetweenDates("2019-06-29", "2019-06-30"))
    print(object.daysBetweenDates("2020-01-15", "2019-12-31"))
    print(object.daysBetweenDates("1971-06-29", "2010-09-23"))