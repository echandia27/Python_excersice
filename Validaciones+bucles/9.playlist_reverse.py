# 9) Música “Playlist Reversa” — Escucha en orden invertido
# Como DJ, quiero una función invertir_playlist(playlist) que valide que no esté vacía y la invierta en sitio.

# Luego, recorre la lista para reproducir las primeras 5 canciones (o menos si no hay suficientes).

playlist=["cancion1", "cancion2", "cancion3", "cancion4","canciones5", "canciones6"]

def invertir_playlist(playlist):
    if len(playlist) == 0:
        print("lista vacia")
        return []
    playlist.reverse()

    print("reproduciones las primeras 5 canciones")
    for i in range(min(5,len(playlist))):
        print(f"- {playlist[i]}")

    return playlist

print(invertir_playlist(playlist))
