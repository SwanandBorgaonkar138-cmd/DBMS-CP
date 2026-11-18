def merge_profiles(github=None, stackoverflow=None, leetcode=None):

    """
    Combines all platform profiles
    into one unified profile.
    """

    unified = {

        "display_name": None,

        "username": None,

        "confidence": 0,

        "platforms": {

            "github": github,

            "stackoverflow": stackoverflow,

            "leetcode": leetcode

        }

    }

    # Username priority

    if github and github.get("username"):

        unified["username"] = github["username"]

    elif leetcode and leetcode.get("username"):

        unified["username"] = leetcode["username"]

    # Display name priority

    if github and github.get("name"):

        unified["display_name"] = github["name"]

    elif stackoverflow and stackoverflow.get("display_name"):

        unified["display_name"] = stackoverflow["display_name"]

    elif leetcode and leetcode.get("real_name"):

        unified["display_name"] = leetcode["real_name"]

    return unified