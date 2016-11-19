import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    # the constructor for the objects
    def __init__(self, movie_title, movie_poster, movie_trailer):
        self.title = movie_title
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        
    # the method to show the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
