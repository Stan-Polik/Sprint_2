class Movies:
    def __init__(self, movies = []):
        self.movies = movies
    def add_movie(self,movies):
        self.movies.append(movies)


class Comedy(Movies):
    def __init__(self,movies = []):
        super().__init__(movies)
    def add_movie(self,movies):
        self.movies.append(movies)
        return f"Комедии:  {movies}"
class Drama(Movies):
    def __init__(self,movies = []):
        super().__init__(movies)
    def add_movie(self,movies):
        self.movies.append(movies)
        return f"Драмы:  {movies}"

comedy = Comedy()
drama = Drama()
print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))
... # напиши свой код здесь