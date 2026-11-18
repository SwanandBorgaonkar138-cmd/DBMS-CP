from difflib import SequenceMatcher

from services.normalization_service import normalize_username


def username_similarity(username1, username2):
    """
    Compare two usernames after normalization.

    Returns:
        float between 0 and 1
    """

    username1 = normalize_username(username1)
    username2 = normalize_username(username2)

    return SequenceMatcher(
        None,
        username1,
        username2
    ).ratio()