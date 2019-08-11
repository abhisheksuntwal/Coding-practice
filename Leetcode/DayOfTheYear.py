class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))
        # print(year, month, day)
        daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not year % 4 == 0:
            days = sum(daysInMonth[:month-1]) + day
            return days
        elif not year % 100 == 0:
            days = sum(daysInMonth[:month - 1]) + day + 1
            if (month == 2 and day == 29) or month < 2:
                days -= 1
            return days
        elif not year % 400 == 0:
            days = sum(daysInMonth[:month - 1]) + day
            return days
        else:
            days = sum(daysInMonth[:month - 1]) + day + 1
            if (month == 2 and day == 29) or month < 2:
                days -= 1
            return days

sol = Solution()
print(sol.dayOfYear("2019-01-09"))
print(sol.dayOfYear("2019-02-10"))
print(sol.dayOfYear("2003-03-01"))
print(sol.dayOfYear("1976-01-24"))