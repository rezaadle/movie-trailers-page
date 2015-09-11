#!/usr/bin/env python

import media
import media_maker

toy_story = media.Movie("Toy Story",
						"Story of a boy and his toys that come to life.",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
					 "A marine on an alien planet.",
					 "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")
hunger_games = media.Movie("Hunger Games",
					 "A game of killing to stay alive.",
					 "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
					 "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, hunger_games]
# print toy_story.title
# print avatar.storyline
# hunger_games.show_trailer()
print media.Movie.__doc__

media_maker.open_movies_page(movies)
# print media.Movie.VALID_RATINGS

