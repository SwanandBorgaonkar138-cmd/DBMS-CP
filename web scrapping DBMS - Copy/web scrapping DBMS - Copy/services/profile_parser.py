from urllib.parse import urlparse

def extract_identifier(profile_url):

    parsed = urlparse(profile_url)

    domain = parsed.netloc.lower()

    path = parsed.path.strip("/")

    parts = path.split("/")

    if "github.com" in domain:

        if len(parts) < 1 or parts[0] == "":

            return {
                "platform": "GitHub",
                "error": "GitHub username not found"
            }

        return {
            "platform": "GitHub",
            "username": parts[0]
        }

    elif "stackoverflow.com" in domain:

        if len(parts) < 3:

            return {
                "platform": "Stack Overflow",
                "error": "Invalid Stack Overflow profile URL."
            }

        return {
            "platform": "Stack Overflow",
            "user_id": parts[1],
            "display_name": parts[2]
        }

    elif "linkedin.com" in domain:

        if len(parts) < 2:

            return {
                "platform": "LinkedIn",
                "error": "LinkedIn username not found"
            }

        return {
            "platform": "LinkedIn",
            "username": parts[1]
        }
    
    elif "leetcode.com" in domain:

        # Expected URL:
        # https://leetcode.com/u/username/

        if len(parts) < 2 or parts[0] != "u" or parts[1] == "":

            return {
                "platform": "LeetCode",
                "error": "LeetCode username not found"
            }

        return {
            "platform": "LeetCode",
            "username": parts[1]
        }
    else:

        return {
            "platform": "Unknown"
        }