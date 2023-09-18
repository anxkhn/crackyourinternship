class Solution:
    def dayOfYear(self, date: str) -> int:
        def check_leap(year):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        tot = 0
        for i in range(int(date[5:7])-1):

            tot += days[i]
        if int(date[5:7]) > 2 and check_leap(int(date[0:4])):
            tot += 1
        print(check_leap(int(date[0:4])))
        return tot + int(date[8:10])

