

class Decimal:
    # constructor
    def __init__(self, whole = 0, fraction = 0):
        if fraction == 0:
            if isinstance(whole, str):
                self.__setbystring(whole)
            elif isinstance(whole, Decimal):
                self.wholePart = whole.wholePart
                self.fractionPart = whole.fractionPart
            elif isinstance(whole, int):
                self.wholePart = whole
                self.fractionPart = 0
            else:
                raise TypeError
        else:
            if not isinstance(whole, int) or not isinstance(fraction, int):
                raise TypeError
            self.wholePart = whole
            self.fractionPart = fraction

    def __setbystring(self, string: str):
        if not isinstance(string, str):
            raise TypeError
        string = self.__ignorenondigit(string)
        string = string.split('.')
        self.wholePart = self.__stringtonum(string[0])
        self.fractionPart = self.__stringtonum(string[1])

    # removes first characters that are not digits
    def __ignorenondigit(self, string: str) -> str:
        if not isinstance(string, str):
            raise TypeError
        for i in range(len(string)):
            if string[i].isdigit():
                return string[i:]
        return ""

    # reads unsigned int from string until encounters non digit
    def __stringtonum(self, string: str) -> int:
        if not isinstance(string, str):
            raise TypeError
        res = 0
        for i in range(len(string)):
            if not string[i].isdigit():
                return res
            res = res * 10 + (ord(string[i]) - ord('0'))
        return res

    # ToString
    def __str__(self) -> str:
        frac = str(self.fractionPart)
        if self.fractionPart < 10:
            frac = '0' + frac
        return '\'' + str(self.wholePart) + '.' + frac + '\''

    # normalise (fraction in [0, 99])
    def __norm(self):
        self.wholePart += self.fractionPart / 100
        self.wholePart = int(self.wholePart)
        self.fractionPart = int(self.fractionPart % 100)

    # normalise when either field became float
    def __normfloat(self):
        self.fractionPart += (self.wholePart % 1) * 100
        self.wholePart = int(self.wholePart)
        self.__norm()

    # multiplication
    def __mul__(self, o: int):
        res = Decimal(self)
        if isinstance(o, int):
            res.wholePart *= o
            res.fractionPart *= o
            res.__norm()
        elif isinstance(o, float):
            res.wholePart *= o
            res.fractionPart *= o
            res.__normfloat()
        else:
            raise TypeError
        return res

    # addition
    def __add__(self, o):
        res = Decimal(self)
        if isinstance(o, int):
            res.wholePart += o
        elif isinstance(o, Decimal):
            res.wholePart = self.wholePart + o.wholePart
            res.fractionPart = self.fractionPart + o.fractionPart
            res.__norm()
        else:
            raise TypeError
        return res