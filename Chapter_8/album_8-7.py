def make_album(singer, album, number_songs=None):
    
    album_info = {
        'singer': singer.title(),
        'album': album.title(),
    }

    if number_songs:
        album_info['number of songs'] = number_songs

    return album_info


album_1 = make_album('jay chou', 'jay', 10)
album_2 = make_album('justin bieber', 'My World 2.0')
album_3 = make_album('Taylor Swift', 'Lover', 18)

print(album_1)
print(album_2)
print(album_3)