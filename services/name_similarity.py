from difflib import SequenceMatcher


def similarity(text1, text2):
    """
    Calculates similarity between two names.

    Returns:
        float:
            0.0 = completely different
            1.0 = exactly same
    """

    text1 = (text1 or "").lower().strip()
    text2 = (text2 or "").lower().strip()

    # Remove spaces
    text1 = text1.replace(" ", "")
    text2 = text2.replace(" ", "")

    return SequenceMatcher(
        None,
        text1,
        text2
    ).ratio()