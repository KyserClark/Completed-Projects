def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title, }
    if songs:
        album['songs'] = songs
    return album

artist = ''
title = ''

while True:
    artist = input("\nInput an artist "
                   "\n\t or type 'quit' to exit program: \n")
    if artist == 'quit'.lower():
        break
    title = input("\nInput an album title "
                   "\n\t or type 'quit' to exit program: \n")
    if title == 'quit'.lower():
        break

    if artist and title:
        album = make_album(artist,title)
        print('\n')
        print(album)
