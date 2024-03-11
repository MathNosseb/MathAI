class color:
    g = '\033[92m' # vert
    y = '\033[93m' # jaune
    r = '\033[91m' # rouge
    n = '\033[0m' #gris, couleur normale
    
file = ""
def colorise(text):
    couleurs = [ color.g , color.y , color.r, color.n ]
    if "g " in text:
        text = text.replace("g ","")
        text = couleurs[0]+text
    elif "y " in text:
        text = text.replace("y ","")
        text = couleurs[1]+text
    elif "r " in text:
        text = text.replace("r ","")
        text = couleurs[2]+text
    elif "n " in text:
        text = text.replace("n ","")
        text = couleurs[3]+text
    return(text)

            