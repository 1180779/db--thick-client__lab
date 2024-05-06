

class Datetime(object):
    def __init__(self, string: str = ""):
        if not isinstance(string, str):
            raise TypeError
        string = string.replace(' ', '')
        string = string[:-1]
        string = self.__ignorenondigit(string)
        values = string.split(',')
        self.year = int(values[0])
        self.month = int(values[1])
        self.day = int(values[2])
        self.hour = int(values[3])
        self.minute = int(values[4])

    def __str__(self): 
        hourstr = str(self.hour)
        if self.hour < 10:
            hourstr = '0' + hourstr
        minutestr = str(self.minute)
        if self.minute < 10:
            minutestr = '0' + minutestr
        return '\'' + str(self.year) + '-' + str(self.month) + '-' + str(self.day) + ' ' + hourstr + ':' + minutestr + '\''

# removes first characters that are not digits
    def __ignorenondigit(self, string: str) -> str:
        if not isinstance(string, str):
            raise TypeError
        for i in range(len(string)):
            if string[i].isdigit():
                return string[i:]
        return ""
