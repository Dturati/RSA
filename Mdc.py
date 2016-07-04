import fractions
class Mdc():
    def getMdc(self,n):
        num = 2
        mdc = 0
        while(mdc != 1):
            num = num + 1
            mdc = fractions.gcd(n, num)
        return num