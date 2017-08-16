# -*- coding: utf-8 -*-
# 回数是指从左向右读和从右向左读都是一样的数，用filter过滤掉非回数

def main():
    output = filter(is_palindrome, range(1, 1000))
    print(list(output))

def is_palindrome(n):
    # return int(str(n)[::-1]) == n
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    main()
