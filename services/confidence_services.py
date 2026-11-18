from services.username_similarity import username_similarity
from services.name_similarity import similarity as name_similarity

from services.scoring_config import (
    USERNAME_EXCELLENT,
    USERNAME_GOOD,
    USERNAME_AVERAGE,
    USERNAME_WEAK,
    USERNAME_POINTS,

    NAME_EXCELLENT,
    NAME_GOOD,
    NAME_AVERAGE,
    NAME_POINTS,

    LOCATION_POINTS,
    WEBSITE_POINTS
)


def calculate_confidence(
        github=None,
        stackoverflow=None,
        leetcode=None
):

    score = 0
    available_points = 0

    explanation = []

    # ==================================================
    # USERNAME
    # ==================================================

    if github and leetcode:

        github_username = (
            github.get("username") or ""
        ).strip()

        leetcode_username = (
            leetcode.get("username") or ""
        ).strip()

        if github_username and leetcode_username:

            username_score = username_similarity(
                github_username,
                leetcode_username
            )

            available_points += 40

            if username_score >= USERNAME_EXCELLENT:

                points = USERNAME_POINTS["excellent"]
                score += points

            elif username_score >= USERNAME_GOOD:

                points = USERNAME_POINTS["good"]
                score += points

            elif username_score >= USERNAME_AVERAGE:

                points = USERNAME_POINTS["average"]
                score += points

            elif username_score >= USERNAME_WEAK:

                points = USERNAME_POINTS["weak"]
                score += points

            else:

                points = 0

            explanation.append(
                f"✓ Username similarity = "
                f"{username_score:.2%} (+{points})"
            )

    # ==================================================
    # NAME
    # ==================================================

    if github and leetcode:

        github_name = (
            github.get("name") or ""
        ).strip()

        leetcode_name = (
            leetcode.get("real_name") or ""
        ).strip()

        if github_name and leetcode_name:

            name_score = name_similarity(
                github_name,
                leetcode_name
            )

            available_points += 30

            if name_score >= NAME_EXCELLENT:

                points = NAME_POINTS["excellent"]
                score += points

            elif name_score >= NAME_GOOD:

                points = NAME_POINTS["good"]
                score += points

            elif name_score >= NAME_AVERAGE:

                points = NAME_POINTS["average"]
                score += points

            else:

                points = 0

            if points > 0:

                explanation.append(
                    f"✓ Name similarity = "
                    f"{name_score:.2%} (+{points})"
                )

            else:

                explanation.append(
                    f"✗ Name similarity = "
                    f"{name_score:.2%}"
                )

        else:

            explanation.append(
                "⚠ Name comparison skipped "
                "(insufficient data)"
            )

    # ==================================================
    # LOCATION
    # ==================================================

    if github and stackoverflow:

        github_location = (
            github.get("location") or ""
        ).strip().lower()

        stack_location = (
            stackoverflow.get("location") or ""
        ).strip().lower()

        if github_location and stack_location:

            available_points += LOCATION_POINTS

            if github_location == stack_location:

                score += LOCATION_POINTS

                explanation.append(
                    f"✓ Location matched "
                    f"(+{LOCATION_POINTS})"
                )

            else:

                explanation.append(
                    "✗ Location different"
                )

        else:

            explanation.append(
                "⚠ Location comparison skipped "
                "(insufficient data)"
            )

    # ==================================================
    # WEBSITE
    # ==================================================

    if github and stackoverflow:

        github_blog = (
            github.get("blog") or ""
        ).strip().lower()

        stack_website = (
            stackoverflow.get("website") or ""
        ).strip().lower()

        if github_blog and stack_website:

            available_points += WEBSITE_POINTS

            if github_blog == stack_website:

                score += WEBSITE_POINTS

                explanation.append(
                    f"✓ Website matched "
                    f"(+{WEBSITE_POINTS})"
                )

            else:

                explanation.append(
                    "✗ Website different"
                )

        else:

            explanation.append(
                "⚠ Website comparison skipped "
                "(insufficient data)"
            )

    # ==================================================
    # NORMALIZE SCORE
    # ==================================================

    if available_points > 0:

        normalized_score = (
            score / available_points
        ) * 100

    else:

        normalized_score = 0

    normalized_score = round(
        normalized_score,
        2
    )

    # ==================================================
    # FINAL DECISION
    # ==================================================

    if normalized_score >= 80:

        status = "Highly Likely Same Person"

    elif normalized_score >= 60:

        status = "Likely Match"

    elif normalized_score >= 40:

        status = "Possible Match"

    else:

        status = "Low Confidence"

    # ==================================================
    # RETURN
    # ==================================================

    return {

        "score": normalized_score,

        "raw_score": score,

        "available_points": available_points,

        "status": status,

        "explanation": explanation

    }