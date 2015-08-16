import webbrowser


class Video():

	def __init__(self, title, duration_minutes, storyline, poster_url , trailer_url):
		self.title = title
		self.duration = duration_minutes
		self.storyline = storyline
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)



class Movie(Video):
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, duration_minutes, storyline, poster_url , trailer_url, date_on_theater):
		Video.__init__(self, title, duration_minutes, storyline, poster_url , trailer_url)
		self.date_on_theater = date_on_theater

class TvShow(Video):
	def __init__(self, title, duration_minutes, storyline, poster_url , trailer_url, num_seasons):
		Video.__init__(self, title, duration_minutes, storyline, poster_url , trailer_url)
		self.num_seasons = num_seasons

