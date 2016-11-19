import fresh_tomatoes
import media

# this is a list of objects, instances from class Movie
mitty = media.Movie("The Secret Life of Walter Mitty",
                        "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=HddkucqSzSM")

horton = media.Movie("Horton Hears a Who!",
                    "http://www.impawards.com/2008/posters/horton_hears_a_who.jpg",
                    "https://www.youtube.com/watch?v=MIQFTBsGccA")

cuento_chino = media.Movie("Un Cuento Chino",
                           "http://www.cinemista.com.br/wp-content/uploads/2012/02/Un_Cuento_Chino.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=cDw_eiwGfY0")

lenin = media.Movie("Good Bye, Lenin!",
                           "https://www.movieposter.com/posters/archive/main/60/MPW-30406",  # NOQA
                           "https://www.youtube.com/watch?v=iJb4efZcFUM")

belleville = media.Movie("Les Triplettes de Belleville",
                           "http://ilarge.lisimg.com/image/756609/740full-the-triplets-of-belleville-poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=Npro9kjyaJk")

full_monty = media.Movie("The Full Monty",
                           "https://www.movieposter.com/posters/archive/main/122/MPW-61470",  # NOQA
                           "https://www.youtube.com/watch?v=CWZBdTCsRCY")
# list of objects
movies = [mitty, horton, cuento_chino, lenin, belleville, full_monty]

# function called from fresh tomatoes to open the movies page
fresh_tomatoes.open_movies_page(movies)
