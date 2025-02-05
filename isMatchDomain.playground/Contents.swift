import UIKit

func areDomainsMatching(baseURL: String, domainString: String) -> Bool {
    // Parse the host from the base URL
    guard let url = URL(string: baseURL),
          let host = url.host?.lowercased() else {
        return false
    }
    
    let pattern = "^\\.+"
    // Normalize the domain string (remove leading dots and whitespace)
    let normalizedDomain = domainString
        .trimmingCharacters(in: .whitespaces)
        .lowercased()
        .replacingOccurrences(of: pattern, with: "", options: .regularExpression) // Remove leading dots
    
    // Check for direct match or subdomain match
    return host == normalizedDomain || host.hasSuffix(".\(normalizedDomain)")
}

let base_url = "https://mwacc.ips.co.kr//webank//CardAPI.do"
let domain_string = ".mwacc.ips.co.kr"

print(areDomainsMatching(baseURL: base_url, domainString: domain_string)) // ✅ Returns `true`

