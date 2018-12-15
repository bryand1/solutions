from collections import OrderedDict

vocabulary = OrderedDict([
    (90, 'Ninety'),
    (80, 'Eighty'),
    (70, 'Seventy'),
    (60, 'Sixty'),
    (50, 'Fifty'),
    (40, 'Forty'),
    (30, 'Thirty'),
    (20, 'Twenty'),
    (19, 'Nineteen'),
    (18, 'Eighteen'),
    (17, 'Seventeen'),
    (16, 'Sixteen'),
    (15, 'Fifteen'),
    (14, 'Fourteen'),
    (13, 'Thirteen'),
    (12, 'Twelve'),
    (11, 'Eleven'),
    (10, 'Ten'),
    (9, 'Nine'),
    (8, 'Eight'),
    (7, 'Seven'),
    (6, 'Six'),
    (5, 'Five'),
    (4, 'Four'),
    (3, 'Three'),
    (2, 'Two'),
    (1, 'One')
])

class Solution:

    def under_one_hundred(self, num):
        ret = []
        it = iter(vocabulary.keys())
        while num:
            divisor = next(it)
            if num >= divisor:
                ret.append(vocabulary[divisor])
                num -= divisor
        return ret
    
    def under_one_thousand(self, num):
        ret = []
        hundreds = int(num // 1e2)
        if hundreds:
            ret.extend([vocabulary[hundreds], "Hundred"])
        num = int(num % 1e2)
        ret.extend(self.under_one_hundred(num))
        return ret
    
    def under_one_million(self, num):
        ret = []
        thousands = int(num // 1e3)
        if thousands:
            ret.extend(self.under_one_thousand(thousands))
            ret.append("Thousand")
        num = int(num % 1e3)
        ret.extend(self.under_one_thousand(num))
        return ret
    
    def under_one_billion(self, num):
        ret = []
        millions = int(num // 1e6)
        if millions:
            ret.extend(self.under_one_thousand(millions))
            ret.append("Million")
        num = int(num % 1e6)
        ret.extend(self.under_one_million(num))
        return ret

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
        l = []
        billions = int(num // 1e9)
        if billions:
            l.extend(self.under_one_hundred(billions))
            l.append("Billion")
        num = int(num % 1e9)
        l.extend(self.under_one_billion(num))
        return ' '.join(l)
