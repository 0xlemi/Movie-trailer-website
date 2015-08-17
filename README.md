# Movie Trailer Website Generator :movie_camera:

The only thing you need to create a website with your favorite movies.
Is create a instance of the object Movie or TvShow, and send it to the create_movie_tiles_content() function in fresh_tomatoes.py

#### In file entertaiment_center.py

You can create Movie or TvShow objects
Create the object like this:

```python
instance_movie = media.Movie(movie_title, duration,
 movie_storyline, movie_image_url, movie_youtube_url, date_on_theater)

instance_tvshow = media.TvShow(tvshow_title, duration,
 tvshow_storyline, tvshow_image_url, tvshow_youtube_url, num_seasons)
```

Put them all in a array, and call the function

```python
movies_or_tvshows = [movie1, movie2, tvShow1, tvShow2 ]
fresh_tomatoes.open_movies_page(movies_tvshow)
```

run entertaiment_center.py and the website is going to be generated as fresh_tomatoes.html

