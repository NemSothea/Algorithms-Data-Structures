import UIKit

func longestCommonPrefix(_ strs: [String]) -> String {
    if strs.isEmpty {
        return ""
    }
    var prefix = strs[0]
    
    for string in strs[1...] {
        while !string.hasPrefix(prefix) {
            prefix.removeLast()
            if prefix.isEmpty {
                return ""
            }
        }
    }
    return prefix
}
//print(longestCommonPrefix(["protestation","president","protest"]))
print(longestCommonPrefix(["flower","flow","flight"]))
