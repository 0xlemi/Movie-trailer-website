import media
import fresh_tomatoes

movie_title = "Toy Story"
movie_storyline = "A Story of toys that come to life."
movie_image_url = "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg"
movie_youtube_url = "https://youtu.be/0q1rxc96m2w"
toy_story = media.Movie(movie_title, movie_storyline, movie_image_url, movie_youtube_url);

movie_title = "Avatar"
movie_storyline = "Army on alien planet."
movie_image_url = "http://orig15.deviantart.net/a0e7/f/2010/192/b/e/avatar_special_edition_poster_by_j_k_k_s.jpg"
movie_youtube_url = "https://youtu.be/5PSNL1qE6VY"
avatar = media.Movie(movie_title, movie_storyline, movie_image_url, movie_youtube_url);

movie_title = "School of rock"
movie_storyline = "A guy that teaches kids rock."
movie_image_url = "http://static.rogerebert.com/uploads/movie/movie_poster/school-of-rock-2003/large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg"
movie_youtube_url = "https://youtu.be/XCwy6lW5Ixc"
school_of_rock = media.Movie(movie_title, movie_storyline, movie_image_url, movie_youtube_url);

movie_title = "The Dark Knight"
movie_storyline = "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice."
movie_image_url = "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg"
movie_youtube_url = "https://youtu.be/EXeTwQWrcwY"
the_dark_knight = media.Movie(movie_title, movie_storyline, movie_image_url, movie_youtube_url);

movie_title = "Friends with Benefits"
movie_storyline = "While trying to avoid the cliches of Hollywood romantic comedies, Dylan Harper and Jamie Rellis soon discover however that adding the act of sex to their friendship does lead to complications."
movie_image_url = "http://ia.media-imdb.com/images/M/MV5BMTQ2MzQ0NTk4N15BMl5BanBnXkFtZTcwMDc2NDYzNQ@@._V1_SY317_CR0,0,214,317_AL_.jpg"
movie_youtube_url = "https://youtu.be/iJS-wWqVAyk"
friends_with_benefits = media.Movie(movie_title, movie_storyline, movie_image_url, movie_youtube_url);

#print(avatar.storyline)
#avatar.show_trailer()

movies = [toy_story, avatar, school_of_rock, the_dark_knight, friends_with_benefits]
fresh_tomatoes.open_movies_page(movies)