def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# print(longestCommonPrefix(["flower","flow","flight"])) #return "fl"

# print(longestCommonPrefix(["happy","unhappy","happiness"])) # return ""

print(longestCommonPrefix(["protestation","protest","president"])) # return "happy"