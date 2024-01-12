def make_album(singer, album):
    
    album_info = {
        'singer': singer.title(),
        'album': album.title(),
    }


    return album_info

def print_album_info(album_info):
    for key, value in album_info.items():
        print(f"{key}: {value}")



while True:
    print("Please input singer name and album name: ")
    print("(enter 'q' at any time to quit)")

    singer = input("singer name: ")
    if singer=='q':
        break

    album = input("album name: ")
    if album=='q':
        break

    album_info = make_album(singer, album)
    print("The added album information is as follows:")
    print_album_info(album_info)


