def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title, }
    if songs:
        album['songs'] = songs
    return album


album_1 = make_album('Von Kaiser', 'Sythwave')
print(album_1)

album_2 = make_album('Gunship', 'New Retro Wave', 39)
print(album_2)

album_3 = make_album('Destructoid', 'Kool Wave', '86')
print(album_3)
