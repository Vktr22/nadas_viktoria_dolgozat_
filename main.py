import feladatok

print("1. feladat:")
print(feladatok.parosBeker())
print("")

print("2. feladat:")
velLista=feladatok.veletlenListaZartINtervallum(10, 150)
print(velLista)
oszth3=feladatok.oszthatoeDb(velLista, 3)
print(f"A számok között {oszth3} db 3-mal osztható van")
print("")

print("3. feladat:")
feladatok.szovegbenKeres("A kedvenc fagyim a vanília", 6)
print("")


