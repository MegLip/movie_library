import random
from datetime import date


class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # Variables
        self.views = 0

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self):
        self.views += 1
        return (self)


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title}  {self.season}{self.episode}"


class Library:
    def __init__(self):
        self.database = [
            Movie(title="Jack Strong", year="2014", genre="Thriller"),
            Movie(title="Intouchables", year="2011", genre="Dramat"),
            Movie(title="Matrix", year="1999", genre="Sci-Fi"),
            Movie(title="Green Mile", year="1999", genre="Dramat"),
            Movie(title="Forrest Gump", year="1994", genre="Dramat"),
            Movie(title="Saving Private Ryan", year="1998", genre="Dramat"),
            Movie(title="Gone Girl", year="2014", genre="Thriller"),
            Movie(title="The Help", year="2011", genre="Dramat"),
            Movie(title="Seven Pounds", year="2008", genre="Dramat"),
            Movie(title="Catch Me If You Can", year="2002", genre="Comedy"),
            Series(
                title="Dr House", year="2004", genre="Comedy",
                season="S01", episode="E01"),
            Series(
                title="Dr House", year="2004", genre="Comedy",
                season="S01", episode="E02"),
            Series(
                title="Dr House", year="2004", genre="Comedy",
                season="S01", episode="E03"),
            Series(
                title="The Wonder Years", year="1988", genre="Comedy",
                season="S02", episode="E01"),
            Series(
                title="The Wonder Years", year="1988", genre="Comedy",
                season="S02", episode="E02"),
            Series(
                title="The Wonder Years", year="1988", genre="Comedy",
                season="S02", episode="E03"),
            Series(
                title="Friends", year="1994", genre="Comedy",
                season="S01", episode="E01"),
            Series(
                title="Friends", year="1994", genre="Comedy",
                season="S01", episode="E02"),
            Series(
                title="Friends", year="1994", genre="Comedy",
                season="S02", episode="E01"),
            Series(
                title="Friends", year="1994", genre="Comedy",
                season="S02", episode="E02"),
        ]

    def get_movies(self):
        self.movies_only = [
            item for item in self.database
            if (isinstance(item, Movie) and not isinstance(item, Series))
            ]
        return sorted(self.movies_only, key=lambda movie: movie.title)

    def get_series(self):
        self.series_only = [
            item for item in self.database
            if isinstance(item, Series)
            ]
        return sorted(self.series_only, key=lambda series: series.title)

    def search(self, keyword):
        for item in self.database:
            if item.title == keyword:
                return item
            else:
                pass
        else:
            return "Brak filmu w bibliotece!"

    def generate_views(self):
        self.database[
            random.randint(0, len(self.database)-1)
            ].views += random.randint(1, 100)
        return True

    def top_titles(self, content_type=None, top_counter=3):
        if content_type is None:
            return sorted(
                self.database, key=lambda movie: movie.views, reverse=True
                )[0:top_counter]
        elif content_type == "Movie":
            self.movies_only = [
                item for item in self.database if (
                    isinstance(item, Movie) and not isinstance(item, Series))
                ]
            return sorted(
                self.movies_only, key=lambda movie: movie.views, reverse=True
                )[0:top_counter]
        elif content_type == "Series":
            self.series_only = [
                item for item in self.database if isinstance(item, Series)
                ]
            return sorted(
                self.series_only, key=lambda movie: movie.views, reverse=True
            )[0:top_counter]
        else:
            return 0


if __name__ == "__main__":
    library = Library()

    print("\n***** Biblioteka filmów:")
    for movie in library.get_movies():
        print(f"{movie.title} {movie.year}")
    print('\n')

    print("***** Biblioteka seriali:")
    for series in library.get_series():
        print(f"{series.title} {series.season}{series.episode}")
    print('\n')

    for i in range(10):
        library.generate_views()

    print(f"***** Najpopularniejsze filmy i seriale dnia {date.today()}:")
    for item in library.top_titles(content_type="Movie", top_counter=3):
        print(f"{item.title}: {item.views}")
