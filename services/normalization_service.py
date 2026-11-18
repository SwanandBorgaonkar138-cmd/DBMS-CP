import re


def normalize_username(username):
    """
    Normalize usernames before comparison.

    Example:
        Krishna_Bheda
        Krishna-Bheda
        Krishna.Bheda

    →

        krishnabheda
    """

    username = (username or "").lower()

    username = re.sub(r'[^a-z0-9]', '', username)

    return username