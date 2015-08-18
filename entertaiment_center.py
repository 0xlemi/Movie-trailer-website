import media
import fresh_tomatoes

# ***********
# MOVIES
# ***********

# here goes all the instancing for the movies
movie_title = "Toy Story"
movie_storyline = "A Story of toys that come to life."
movie_image_url = "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg"  # noqa
movie_youtube_url = "https://youtu.be/0q1rxc96m2w"
date_on_theater = "19-nov-1995"
duration = "81"
toy_story = media.Movie(
            movie_title, duration, movie_storyline,
            movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "Avatar"
movie_storyline = "Army on alien planet."
movie_image_url = "http://orig15.deviantart.net/a0e7/f/2010/192/b/e/avatar_special_edition_poster_by_j_k_k_s.jpg"  # noqa
movie_youtube_url = "https://youtu.be/5PSNL1qE6VY"
date_on_theater = "18-dic-2009"
duration = "162"
avatar = media.Movie(
         movie_title, duration, movie_storyline,
         movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "School of rock"
movie_storyline = "A guy that teaches kids rock."
movie_image_url = "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg"  # noqa
movie_youtube_url = "https://youtu.be/XCwy6lW5Ixc"
date_on_theater = "3-oct-2003"
duration = "108"
school_of_rock = media.Movie(
                 movie_title, duration, movie_storyline,
                 movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "The Dark Knight"
movie_storyline = "When the menace known as the Joker wreaks \
                   havoc and chaos on the people of Gotham, the \
                   caped crusader must come to terms with one of \
                   the greatest psychological tests of his ability \
                   to fight injustice."
movie_image_url = "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg"  # noqa
movie_youtube_url = "https://youtu.be/EXeTwQWrcwY"
date_on_theater = "18-jul-2008"
duration = "152"
the_dark_knight = media.Movie(
                  movie_title, duration, movie_storyline,
                  movie_image_url, movie_youtube_url, date_on_theater)

movie_title = "Friends with Benefits"
movie_storyline = "While trying to avoid the cliches of Hollywood \
                  romantic comedies, Dylan Harper and Jamie Rellis \
                  soon discover however that adding the act of sex \
                  to their friendship does lead to complications."
movie_image_url = "http://ia.media-imdb.com/images/M/MV5BMTQ2MzQ0NTk4N15BMl5BanBnXkFtZTcwMDc2NDYzNQ@@._V1_SY317_CR0,0,214,317_AL_.jpg"  # noqa
movie_youtube_url = "https://youtu.be/iJS-wWqVAyk"
date_on_theater = "22-jul-2011"
duration = "109"
friends_with_benefits = media.Movie(
                        movie_title, duration, movie_storyline,
                        movie_image_url, movie_youtube_url, date_on_theater)

# ***********
# TVSHOWS
# ***********
# here goes the instanceing for the tv_shows
title = "Breaking Bad"
storyline = "A chemistry teacher diagnosed with a terminal \
            lung cancer teams up with his former student to \
            cook and sell crystal meth."
image_url = "http://ia.media-imdb.com/images/M/MV5BMTQ0ODYzODc0OV5BMl5BanBnXkFtZTgwMDk3OTcyMDE@._V1_SY317_CR0,0,214,317_AL_.jpg"  # noqa
youtube_url = "https://youtu.be/HhesaQXLuRY"
duration = "41"
num_seasons = "5"
breaking_bad = media.TvShow(
               title, duration, storyline,
               image_url, youtube_url, num_seasons)

title = "Game of Thrones"
storyline = "Several noble families fight for control \
             of the mythical land of Westeros."
image_url = "http://ia.media-imdb.com/images/M/MV5BNTgxOTI4NzY2M15BMl5BanBnXkFtZTgwMjY3MTM2NDE@._V1_SX214_AL_.jpg"  # noqa
youtube_url = "https://youtu.be/8ixEWrTLiZg"
duration = "55"
num_seasons = "6"
game_of_thrones = media.TvShow(
                  title, duration, storyline,
                  image_url, youtube_url, num_seasons)

title = "Cosmos"
storyline = "Astronomer Carl Sagan leads us on an engaging \
             guided tour of the various elements and \
             cosmological theories of the universe."
image_url = "http://ia.media-imdb.com/images/M/MV5BMTI0NTg5MjA5OF5BMl5BanBnXkFtZTcwNDMxMTEyMQ@@._V1_SY317_CR13,0,214,317_AL_.jpg"  # noqa
youtube_url = "https://youtu.be/bSxHZPoQ4JQ"
duration = "60"
num_seasons = "1"
cosmos = media.TvShow(
         title, duration, storyline,
         image_url, youtube_url, num_seasons)

# put all the objects into an array,
# so they can be parameter to the function open_movies_page
movies_tvshow = [toy_story, avatar, school_of_rock,
                 the_dark_knight, friends_with_benefits,
                 breaking_bad, game_of_thrones, cosmos]
# run the function that will generate the html file
fresh_tomatoes.open_movies_page(movies_tvshow)
