def write_liked_songs_to_file(file_name, liked_songs):
    with open(file_name, 'w') as f:
        for song, artist in liked_songs.items():
            f.write(f"{song} - {artist}\n")

liked_songs = {
    '7 rings': 'Ariana Grande',
    'bad guy': 'Billie Eilish',
    'Summertime Sadness': 'Lana Del Rey',
    'hello kitty': 'Jazmin Bean',
    'drivers license': 'Olivia Rodrigo'
}

write_liked_songs_to_file('liked_songs.txt', liked_songs)