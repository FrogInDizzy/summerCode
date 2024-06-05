def longest_common_prefix(strs):
    if not strs:
        return ""
    min_str = min(strs)
    max_str = max(strs)

    i = 0
    while i < len(min_str) and min_str[i] == max_str[i]:
        i += 1

    return min_str[:i]

print(longest_common_prefix(["flower","flow","flight"]))  # should return "fl"
