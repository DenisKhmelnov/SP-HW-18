from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, uid):
        return self.session.query(Movie).filter(Movie.id == uid).one()

    def get_movies_by_params(self, **kwargs):
        return self.session.query(Movie).filter_by(**kwargs).all()

    def create_movie(self, movie):
        try:
            new_movie = Movie(**movie)
            self.session.add(new_movie)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False
    def update_movie(self, movie, uid):
        try:
            self.session.query(Movie).filter(Movie.id == uid).update(movie)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False

    def delete_movie(self, uid):
        try:
            self.session.query(Movie).filter(Movie.id == uid).delete()
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            return False