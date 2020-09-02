from datetime import datetime
import csv

##################################
########  ACTOR CLASS  ###########
##################################

class Actor:

    def __init__(self, actor_name_full: str):
        self.colleague_list = []

        if actor_name_full == "" or type(actor_name_full) is not str:
            self.__actor_name = None
        else:
            self.__actor_name = actor_name_full.strip()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_name

    def __repr__(self):
        return f"<Actor {self.__actor_name}>"

    def __eq__(self, other):
        if self.__actor_name == other.__actor_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_name < other.__actor_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_name)

    def add_actor_colleague(self, colleague):
        self.colleague_list.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.colleague_list:
            return True
        else:
            return False


##################################
########  GENRE CLASS  ###########
##################################

class Genre:
    def __init__(self, genre_name_full: str):
        if genre_name_full == "" or type(genre_name_full) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name_full.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other.__genre_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__genre_name < other.__genre_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__genre_name)


#####################################
########  DIRECTOR CLASS  ###########
#####################################

class Director:
    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__director_full_name < other.__director_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__director_full_name)


    

##################################################
########  MOVIE FILE CSV READER CLASS  ###########
##################################################

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.genre_dataset = []
        self.actor_dataset = []
        self.director_dataset = []
        self.movie_dataset = []
        self.__file_name = file_name

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                self.dataset_of_movies_setter(row)
                self.dataset_of_actors_setter(row)
                self.dataset_of_directors_setter(row)
                self.dataset_of_genres_setter(row)
                index += 1

    @property
    def dataset_of_movies(self):
        return self.movie_dataset

    def dataset_of_movies_setter(self, row):
        self.movie_dataset.append(Movie(row['Title'], int(row['Year'])))

    @property
    def dataset_of_actors(self):
        return self.actor_dataset

    def dataset_of_actors_setter(self, row):
        act_lst = row['Actors'].split(",")
        for actor in act_lst:
            act = Actor(actor)
            if act not in self.actor_dataset:
                self.actor_dataset.append(Actor(actor))

    @property
    def dataset_of_directors(self):
        return self.director_dataset

    def dataset_of_directors_setter(self, row):
        dir = Director(row["Director"])
        if dir not in self.director_dataset:
            self.director_dataset.append(Director(row['Director']))

    @property
    def dataset_of_genres(self):
        return self.genre_dataset

    def dataset_of_genres_setter(self, row):
        gen_lst = row['Genre'].split(",")
        for genre in gen_lst:
            gen = Genre(genre)
            if gen not in self.genre_dataset:
                self.genre_dataset.append(Genre(genre))



##################################
########  MOVIE CLASS  ###########
##################################

class Movie:
    def __init__(self, movie_name_full: str, movie_year_full: int):
        self._runtime_in_minutes = 0
        self._genres_list = []
        self._actors_list = []
        self._title = None
        self._description = None
        self._director = None
        if movie_name_full == "" or type(movie_name_full) is not str:
            self.__movie_name = None
            self.__movie_year = None
        else:
            if movie_year_full < 1900 or type(movie_year_full) is not int:
                self.__movie_name = None
                self.__movie_year = None
            else:
                self.__movie_name = movie_name_full.strip()
                self.__movie_year = movie_year_full

    # Title
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value):
        if type(value) is str:
            self._title = value.strip()

    # Director
    @property
    def director(self) -> str:
        return self._director

    @director.setter
    def director(self, value):
        if type(value) is Director:
            if self._director is None:
                self._director = value

    # Description
    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value):
        if type(value) is str:
            self._description = value.strip()

    # Actors
    @property
    def actors(self):
        return self._actors_list

    @actors.setter
    def actors(self, actor):
        if type(actor) is list:
            self._actors_list = actor

    # Genres
    @property
    def genres(self):
        return self._genres_list

    @genres.setter
    def genres(self, genre):
        if type(genre) is list:
            self._genres_list = genre

    @property
    def runtime_minutes(self):
        return self._runtime_in_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if type(runtime) is int:
            if runtime > 0:
                self._runtime_in_minutes = runtime
            else:
                raise ValueError()
        else:
            raise ValueError()

    def __repr__(self):
        return f"<Movie {self.__movie_name}, {self.__movie_year}>"

    def __eq__(self, other):
        if self.__movie_name == other.__movie_name and self.__movie_year == other.__movie_year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__movie_name < other.__movie_name:
            return True
        elif self.__movie_name == other.__movie_name and self.__movie_year < other.__movie_year:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__movie_name + str(self.__movie_year))

    def add_actor(self, actor):
        self._actors_list.append(actor)

    def remove_actor(self, actor):
        if actor in self._actors_list:
            self._actors_list.remove(actor)

    def add_genre(self, genre):
        self._genres_list.append(genre)

    def remove_genre(self, genre):
        if genre in self._genres_list:
            self._genres_list.remove(genre)


###################################
########  REVIEW CLASS  ###########
###################################

class Review:
    def __init__(self, movie_name_full: str, review_text_full: str, movie_rating_full: int):
        self.__review_time = datetime.now()
        if type(movie_name_full) is not Movie:
            self.__movie_name = Movie("Null", 0000)
        else:
            self.__movie_name = movie_name_full

        if review_text_full == "" or type(review_text_full) is not str:
            self.__review_text = None

        else:
            self.__review_text = review_text_full.strip()
        if movie_rating_full == "" or type(
                movie_rating_full) is not int or movie_rating_full < 1 or movie_rating_full > 10:
            self.__movie_rating = None

        else:
            self.__movie_rating = movie_rating_full

    @property
    def movie(self) -> str:
        return self.__movie_name

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__movie_rating

    @property
    def timestamp(self) -> datetime:
        return self.__review_time

    def __repr__(self):
        return f"<Review {self.__movie_name}, {self.__review_text}, {self.__movie_rating}>"

    def __eq__(self, other):
        if self.__movie_name == other.__movie_name and self.__review_text == other.__review_text and self.__movie_rating == other.__movie_rating:
            return True
        else:
            return False




###############      ####          ####      ####################       ###############      #####       ####          #######          ##################          #########         #####       ####
###############       ####        ####       ####################       ###############      ######      ####        ###########        ##################        #############       ######      ####
####                   ####      ####                ####               ####                 #######     ####      #####     #####             ####              #####     #####      #######     ####
####                    ####    ####                 ####               ####                 ########    ####      ####                        ####              ####       ####      ########    ####
####                     ####  ####                  ####               ####                 #### ####   ####       ####                       ####              ####       ####      #### ####   ####
#########                 ########                   ####               #########            ####  ####  ####         #####                    ####              ####       ####      ####  ####  ####
#########                 ########                   ####               #########            ####   #### ####             #####                ####              ####       ####      ####   #### ####
####                     ####  ####                  ####               ####                 ####    ########                ####              ####              ####       ####      ####    ########
####                    ####    ####                 ####               ####                 ####     #######                 ####             ####              ####       ####      ####     #######
####                   ####      ####                ####               ####                 ####      ######      #####     #####             ####              #####     #####      ####      ######
################      ####        ####               ####               ###############      ####       #####        ###########        ###################       #############       ####       #####
################     ####          ####              ####               ###############      ####        ####          #######          ###################         #########         ####        ####

#(Wow that took way too long to make)#


###############################################
########  IMPROVED WATCHLIST CLASS  ###########
###############################################

class WatchList:
    def __init__(self, user):
        self.__watch_list = []
        self.__watch_list_owner = user


    def add_movie(self, movie):
        if type(movie) is Movie and movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if type(index) is int and 0 <= index < len(self.__watch_list):
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) > 0:
            return self.__watch_list[0]
        else:
            return None

    def __iter__(self):
        return iter(self.__watch_list)

    def __next__(self, itr_lst):
        return itr_lst.__next__()


##########################################
########  IMPROVED USER CLASS  ###########
##########################################

class User:
    def __init__(self, username_full: str, password_full: str):
        self.__total_time_watched = 0
        self.__movie_review_list = []
        self.__watched_movies_list = []
        if username_full == "" or type(username_full) is not str or password_full == "" or type(
                password_full) is not str:
            self.__username = None
            self.__password = None
        else:
            username_full.strip()
            self.__username = username_full.lower()
            self.__password = password_full
        self.to_watch_list = WatchList(self.__username)

    @property
    def user_name(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies_list

    @property
    def reviews(self):
        return self.__movie_review_list

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__total_time_watched

    @property
    def watchlist(self):
        return self.to_watch_list

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if self.__username == other.__username:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__username < other.__username:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__username)

    def watch_movie(self, movie):
            self.__watched_movies_list.append(movie)
            self.__total_time_watched += movie.runtime_minutes
            if movie in self.to_watch_list:
                self.to_watch_list.remove_movie(movie)

    def watch_first_movie(self):
        self.watch_movie(self.to_watch_list.first_movie_in_watchlist())


    def add_to_watch_later(self, movie):
        if type(movie) is Movie:
            self.to_watch_list.add_movie(movie)

    def add_review(self, review):
        self.__movie_review_list.append(review)

    def total_watchlist_movie_length(self):
        total = 0
        for movie in self.to_watch_list:
            total += movie.runtime_minutes
        return total


#Testing
########################################################################################################

print("Creating a user specific watch later list")
user1 = User("ABCD", "pw223")
print("""Expected Output:
0

Actual Output:""")
print(user1.to_watch_list.size())


##############################################################
print()
print("---------------------------------------------")
print("Adding Movies to user specific watch later list and testing index/first value retrieving")
user1 = User("ABCD", "pw223")
user1.to_watch_list.add_movie(Movie("Titanic",1900))
user1.to_watch_list.add_movie(Movie("LOTR", 2020))
print("""Expected Output:
2
<Movie Titanic, 1900>
<Movie LOTR, 2020>

Actual Output:""")
print(user1.to_watch_list.size())
print(user1.to_watch_list.first_movie_in_watchlist())
print(user1.to_watch_list.select_movie_to_watch(1))


##############################################################
print()
print("---------------------------------------------")
print("Adding movies to watch later list, and testing the outcome of the user watching the movie added")
user1 = User("ABCD", "pw223")
user1.to_watch_list.add_movie(Movie("Titanic1",1900))
user1.to_watch_list.add_movie(Movie("LOTR1", 2020))
print("""Expected Output:
1
<Movie LOTR1, 2020>
watched:
[<Movie Titanic1, 1900>]

Actual Output:""")
user1.watch_movie(Movie("Titanic1",1900))
print(user1.to_watch_list.size())
print(user1.to_watch_list.first_movie_in_watchlist())
print("watched:")
print(user1.watched_movies)


##############################################################
print()
print("---------------------------------------------")
print("Adding movies, and watching specifically the first movie in the watch later list")
user1 = User("ABCD", "pw223")
user1.to_watch_list.add_movie(Movie("Titanic2",1900))
user1.to_watch_list.add_movie(Movie("LOTR2", 2020))
print("""Expected Output:
1
<Movie LOTR2, 2020>
watched:
[<Movie Titanic2, 1900>]

Actual Output:""")
user1.watch_first_movie()
print(user1.to_watch_list.size())
print(user1.to_watch_list.first_movie_in_watchlist())
print("watched:")
print(user1.watched_movies)

##############################################################
print()
print("---------------------------------------------")
print("Testing total watch later list length")

user1 = User("ABCD", "pw223")
user1.to_watch_list.add_movie(Movie("Titanic2",1900))
user1.to_watch_list.add_movie(Movie("LOTR2", 2020))
for movie in user1.to_watch_list:
    movie.runtime_minutes = 100
print("""Expected Output:
2
200

Actual Output:""")
print(user1.to_watch_list.size())
print(user1.total_watchlist_movie_length())










