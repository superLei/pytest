# -*- coding: UTF-8 -*-
import re
import math
import types

class StrUtils:

    """去除数字中无效的0和点"""
    def del_zero_and_point(self,str):
        if str.count('.') == 0:
            return str
        if str.index('.') > 0:
            str = re.sub("0+?$", '', str)
            str = re.sub("[.]$", '', str)
        return str

    """对小数进行取2位，并且不进行四舍五入,第二位若为0也抹去"""
    def keep_two(self,f):
        if len(str(f).split('.')) < 2:
            return f
        else:
            return str(math.floor(f*100) / 100)

    """对小数进行取位，并且不进行四舍五入，不抹去最后位的0"""
    def trunc(self,f, n):
        if str(f).count('.') == 0:
            return str(f)
        else:
            s1, s2 = str(f).split('.')
            if n == 0:
                return s1
            if n <= len(s2):
                print s2[n:n + 1]
                return s1 + '.' + s2[:n]
        return s1 + '.' + s2 + '0' * (n - len(s2))

    """对小数进行取位，并且五舍六入
        f必须是string类型的，不然像2.000会报错
    """
    def trunc2(self, f, n):
        if str(f).count('.') == 0:
            return str(f)
        s1, s2 = str(f).split('.')
        tmp1 = 0
        if n == 0:
            return s1
        if n <= len(s2):
            tmp1 = s2[n-1]
            tmp2 = s2[n-1:n]
            print s2[n:n + 1]
            if int(s2[n:n + 1]) >= 5 and int(s2[n+1:n+2]) > 0:
                if tmp2 ==9:
                    s2[0]
                tmp1 = str(int(tmp2) + 1)
            return s1 + '.' + s2[:n-1] + tmp1
        return s1 + '.' + s2 + tmp1 + '0' * (n - len(s2))


if __name__ == '__main__':
    P = StrUtils()
    print P.trunc2(3017.6952,2)
