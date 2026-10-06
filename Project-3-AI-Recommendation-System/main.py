# ============================================================
# AI Movie Recommendation System
# DecodeLabs Artificial Intelligence Internship - Project 3
# ============================================================

MOVIES = [
    {
        "title": "Interstellar",
        "genres": ["sci-fi", "adventure", "drama"]
    },
    {
        "title": "Inception",
        "genres": ["sci-fi", "action", "thriller"]
    },
    {
        "title": "The Matrix",
        "genres": ["sci-fi", "action", "thriller"]
    },
    {
        "title": "The Dark Knight",
        "genres": ["action", "crime", "drama"]
    },
    {
        "title": "Avengers: Endgame",
        "genres": ["action", "adventure", "sci-fi"]
    },
    {
        "title": "The Hangover",
        "genres": ["comedy"]
    },
    {
        "title": "Toy Story",
        "genres": ["animation", "comedy", "family"]
    },
    {
        "title": "Jurassic Park",
        "genres": ["adventure", "sci-fi", "thriller"]
    }
]

AVAILABLE_GENRES = [
    "action",
    "adventure",
    "comedy",
    "crime",
    "drama",
    "animation",
    "family",
    "sci-fi",
    "thriller"
]


def normalize_genre(genre):
    """Convert user input into the standard genre format."""
    genre = genre.strip().lower()

    # Accept both "sci fi" and "sci-fi"
    if genre == "sci fi":
        return "sci-fi"

    return genre


def calculate_similarity(user_preferences, movie_genres):
    """
    Calculate the similarity score.

    Score = matched preferences / total user preferences * 100
    """

    matched_genres = set(user_preferences) & set(movie_genres)

    if not user_preferences:
        return 0, []

    score = (len(matched_genres) / len(user_preferences)) * 100

    return score, sorted(matched_genres)


def get_recommendations(user_preferences):
    """Generate and rank movie recommendations."""

    recommendations = []

    for movie in MOVIES:
        score, matched_genres = calculate_similarity(
            user_preferences,
            movie["genres"]
        )

        if score > 0:
            recommendations.append({
                "title": movie["title"],
                "score": score,
                "matched": matched_genres,
                "genres": movie["genres"]
            })

    # Highest score first
    recommendations.sort(
        key=lambda movie: movie["score"],
        reverse=True
    )

    return recommendations


def display_header():
    """Display the application header."""

    print("\n" + "=" * 60)
    print("             AI MOVIE RECOMMENDATION SYSTEM")
    print("=" * 60)
    print("  Intelligent preference matching using similarity logic")
    print("=" * 60)


def display_genres():
    """Display available movie genres."""

    print("\nAVAILABLE GENRES")
    print("-" * 60)

    formatted_genres = [
        genre.title().replace("Sci-Fi", "Sci-Fi")
        for genre in AVAILABLE_GENRES
    ]

    print(" | ".join(formatted_genres))


def main():
    display_header()
    display_genres()

    user_input = input(
        "\nEnter your interests (comma-separated): "
    )

    # Process user preferences
    user_preferences = []

    for preference in user_input.split(","):
        genre = normalize_genre(preference)

        if genre and genre not in user_preferences:
            user_preferences.append(genre)

    if not user_preferences:
        print("\nERROR: Please enter at least one interest.")
        return

    # Separate valid and invalid genres
    valid_preferences = [
        genre for genre in user_preferences
        if genre in AVAILABLE_GENRES
    ]

    invalid_preferences = [
        genre for genre in user_preferences
        if genre not in AVAILABLE_GENRES
    ]

    if not valid_preferences:
        print("\nNo recognized genres were entered.")
        print("Please choose from the available genres.")
        return

    # Generate recommendations
    recommendations = get_recommendations(valid_preferences)

    print("\n" + "-" * 60)
    print("USER PROFILE")
    print("-" * 60)

    print(
        "Selected interests : "
        + ", ".join(genre.title() for genre in valid_preferences)
    )

    print(f"Preferences found  : {len(valid_preferences)}")

    if invalid_preferences:
        print(
            "Ignored interests  : "
            + ", ".join(invalid_preferences)
        )

    print("\n" + "-" * 60)
    print("TOP RECOMMENDATIONS")
    print("-" * 60)

    if not recommendations:
        print("\nNo matching movies found.")
        return

    # Display top 5 recommendations
    for number, movie in enumerate(recommendations[:5], start=1):

        print(f"\n#{number}  {movie['title']}")
        print(f"    Match Score : {movie['score']:.0f}%")
        print(
            "    Matched     : "
            + ", ".join(
                genre.title() for genre in movie["matched"]
            )
        )
        print(
            "    Genres      : "
            + ", ".join(
                genre.title() for genre in movie["genres"]
            )
        )

    print("\n" + "-" * 60)
    print("Recommendation process completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()