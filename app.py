from algorithms.kmp import kmp, longestProperPrefix, brute


def k_in_n(s, k):
    count = 0
    n = len(s)

    for i in range(n-k+1):
        count += 1

    return n - k + 1 == count


# print(k_in_n("abcdefg", 2))


# s = "ababcabcabababd"

# pattern = "ababd"

# pattern = "abcdabeabf"
# pattern = "abcdeabfabc"
# pattern = "aabcadaabe"
# pattern = "aaaabaacd"


# prefix_table = [0] * len(pattern)

# seen = {}
# for i, ch in enumerate(pattern):
#     if ch not in seen:
#         seen[ch] = i + 1
#     else:
#         prefix_table[i] = seen[ch]

# generate prefix table


def main():
    # res = kmp()
    # print(res)

    #  i
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
    # a d s g w a d s x d  s  g  w  a  d  s  g  z
    # j
    # dsgwadsgz

    # abac

    # i               j
    # a a a a b c a b c
    # 0 1 2 3 0 0 1 0 0

    #         i
    # adsgwadsxdsgwadsgz
    #                j
    #  d s g w a d s g z
    # [0,0,0,0,0,1,2,3,0]

    # print(longestProperPrefix("dsgwadsgz"))
    print(kmp("a" * 10000001 + "c",
          "a" * 10000000 + "c"))

    print(brute("a" * 1000001 + "c",
          "a" * 1000000 + "c"))

    # print(kmp("adsgwadsxdsgwadsgz", "dsgwadsgz"))


if __name__ == "__main__":
    main()
