from urllib.parse import urlparse

def detect_platform(url):

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    if "github.com" in domain:
        return "GitHub"

    elif "stackoverflow.com" in domain:
        return "Stack Overflow"

    elif "linkedin.com" in domain:
        return "LinkedIn"
    
    elif "leetcode.com" in domain:
        return "LeetCode"

    else:
        return "Unknown"