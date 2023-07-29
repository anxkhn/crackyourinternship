class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        if num // 1000 > 0:
            roman = roman + ("M"*(num // 1000))
            num = num % 1000
        if num>= 900:
            roman = roman + "CM"
            num = num-900
        if num>= 500:
            roman = roman + "D"
            num = num-500
        if num>= 400:
            roman = roman + "CD"
            num = num-400
        if num // 100 > 0:
            roman = roman + ("C"*(num // 100))
            num = num % 100
        if num>= 90:
            roman = roman + "XC"
            num = num-90
        print(num)
        if num>= 50:
            roman = roman + "L"
            num = num-50
        if num>= 40:
            roman = roman + "XL"
            num = num-40
        if num // 10 > 0:
            roman = roman + ("X"*(num // 10))
            num = num % 10
        if num>= 9:
            roman = roman + "IX"
            num = num-9
        if num>= 5:
            roman = roman + "V"
            num = num-5
        if num>= 4:
            roman = roman + "IV"
            num = num-4
        if num // 1 > 0:
            roman = roman + ("I"*(num // 1))
            print(roman,num)

        return roman