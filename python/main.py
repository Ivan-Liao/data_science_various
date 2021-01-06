# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def roman_to_num(s):
    result = 0
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    s.replace('IV','IIII').replace('IX', 'VIIII')
    s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
    s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
    for char in s:
        result += roman_dict[char]
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    roman_to_num('MMMDCCXLIV')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
