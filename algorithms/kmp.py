# # of substrings of size k in string of length n

# n - k + 1


# find string prefixes
# track the indexes

def longestProperPrefix(s):
    lps = [0] * len(s)
    i, j = 0, 1

    while j < len(s):

        # prefix and suffix is matching
        if s[i] == s[j]:
            lps[j] = lps[j-1] + 1
            i += 1
            j += 1
        # doesn't match (already zero)
        else:
            i = lps[i-1]
            j += 1

    return lps


def kmp(s, pattern):
    # prefix table

    lps = longestProperPrefix(pattern)

    if len(s) < len(pattern):
        return False

    i, j = 0, 0
    while j < len(pattern) and i < len(s):
        # print(i, j, s[i], pattern[j], pattern[0:j])
        if pattern[j] == s[i]:
            i += 1
            j += 1
        # match
        # no match
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1

    return j == len(pattern)


def brute(s, pattern):
    if len(pattern) > len(s):
        return False

    # reason. last valid index is skipped beacuse len(pattern) is > 1, need to put back in range
    for i in range(len(s) - len(pattern)+1):
        if s[i:i+len(pattern)] == pattern:
            return True

    return False
