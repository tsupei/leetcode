class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1 if dividend > 0 else 0
        divisor_sign = 1 if divisor > 0 else 0

        value = abs(dividend)
        divisor = abs(divisor)

        OVERFLOWVAL = 1 << 31
        if sign == 0 and value == OVERFLOWVAL and divisor == 1 and divisor_sign == 0:
        	return OVERFLOWVAL-1

        if sign == 0:
        	divisor_sign = 1 if divisor_sign == 0 else 0

        cnt = 0
        while value >= divisor:
        	m = divisor
        	t = 1
        	while value > (m << 1):
        		m = m << 1
        		t = t << 1
        	cnt += t
        	value -= m
        if divisor_sign == 1:
        	return cnt
        else:
        	return -cnt