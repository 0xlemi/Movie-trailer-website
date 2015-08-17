import webbrowser

# Parent class that contains tvShow and movie info
class Video():
	#constructor
	def __init__(self, title, duration_minutes, storyline, poster_url , trailer_url):
		self.title = title
		self.duration = duration_minutes
		self.storyline = storyline
		self.poster_image_url = poster_url
		self.trailer_youtube_url = trailer_url
	#open the browser to the trailer_url
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)


class Movie(Video):
	'''This class provides a way to store movie related information'''
	def __init__(self, title, duration_minutes, storyline, poster_url , trailer_url, date_on_theater):
		Video.__init__(self, title, duration_minutes, storyline, poster_url , trailer_url)
		self.date_on_theater = date_on_theater

class TvShow(Video):
	'''This class provides a way to store tv_show related information'''
	def __init__(self, title, duration_minutes, storyline, poster_url , trailer_url, num_seasons):
		Video.__init__(self, title, duration_minutes, storyline, poster_url , trailer_url)
		self.num_seasons = num_seasons

