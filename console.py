import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist("Artist 1")
artist_repository.save(artist_1)
artist_2 = Artist("Artist 2")
artist_repository.save(artist_2)

album_1 = Album("1st Album", artist_1, "Country Truck Driving Music")
album_repository.save(album_1)
album_2 = Album("2nd Album", artist_1, "Country Truck Driving Music")
album_repository.save(album_2)

pdb.set_trace()
