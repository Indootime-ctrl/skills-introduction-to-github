import tkinter as tk
from tkinter import messagebox

def verifier_texte():
    texte_original = zone_texte_original.get("1.0", "end-1c")
    texte_copied = zone_texte_copied.get("1.0", "end-1c")
    if texte_original == texte_copied:
        messagebox.showinfo("Succès", "Le texte a été copié correctement !")
    else:
        messagebox.showerror("Erreur", "Le texte copié contient des erreurs.")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Copie de texte sans faute")

# Définition de la police
police = ("Arial", 16)

# Zone de texte originale
label_original = tk.Label(fenetre, text="Texte original :", font=police)
label_original.pack()
zone_texte_original = tk.Text(fenetre, height=10, width=60, font=police)
zone_texte_original.pack()

# Zone de texte copiée
label_copied = tk.Label(fenetre, text="Texte copié :", font=police)
label_copied.pack()
zone_texte_copied = tk.Text(fenetre, height=10, width=60, font=police)
zone_texte_copied.pack()

# Bouton pour vérifier
bouton_verifier = tk.Button(fenetre, text="Vérifier", font=police, command=verifier_texte)
bouton_verifier.pack()

# Boucle principale
fenetre.mainloop()
