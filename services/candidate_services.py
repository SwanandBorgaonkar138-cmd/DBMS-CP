def generate_candidates(profile):

    """
    Generates possible usernames
    from profile information.
    """

    candidates = set()

    # Username if available
    if "username" in profile:
        candidates.add(profile["username"].lower())

    # Display name
    if "display_name" in profile:
        name = profile["display_name"].lower()

        candidates.add(name.replace(" ", ""))

        candidates.add(name.replace(" ", "_"))

        candidates.add(name.replace(" ", "-"))

    # Real name
    if "real_name" in profile:
        name = profile["real_name"].lower()

        candidates.add(name.replace(" ", ""))

        candidates.add(name.replace(" ", "_"))

        candidates.add(name.replace(" ", "-"))

    return list(candidates)