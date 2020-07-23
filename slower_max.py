def max_pair(numbers):
    larg = float("-inf")
    sec_larg = float("-inf")

    for number in numbers:
        if number > larg:
            sec_larg = larg
            larg = number
        elif (number < larg) and number > sec_larg:
            sec_larg = number

    return larg * sec_larg


if __name__ == '__main__':
    n = int(input())
    numb_array = [int(x) for x in input().split()]
    print(max_pair(numb_array))
