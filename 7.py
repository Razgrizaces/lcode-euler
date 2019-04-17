class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        negative = 1
        if y[0] is "-":
            negative = -1
            y = y[1:]
        y = y[::-1]
        try:
            if abs(int(y) > 2**31):
                return 0
            return int(y)*negative
        except ValueError:
            print ("Error")