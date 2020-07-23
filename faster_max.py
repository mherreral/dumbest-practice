def max_pair(numbers):
    sort_numb = sorted(numbers)
    return sort_numb[-1] * sort_numb[-2]


if __name__ == '__main__':
    n = int(input())
    numb_array = [int(x) for x in input().split()]
    print(max_pair(numb_array))

