def ajout_separateur(nombre):
        nombre = str(nombre)[::-1]
        resultat = ""
     
        for i, chiffre in enumerate(nombre, 1):
            chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombre) else chiffre
            resultat += chiffre_formatte
     
        return resultat[::-1]
     
nombre = 52039480394023
print(ajout_separateur(nombre))