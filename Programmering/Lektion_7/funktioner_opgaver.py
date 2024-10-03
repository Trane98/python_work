#Her vises en funktion, Hvor der bare skal indsættes 3 variabler, også printer koden selv resten. 
def make_shirt(size_shirt, text_on_shirt, placement):
    """T-shirt selecting proces"""
    print(f"You have choosen the size {size_shirt} and the text on the shirt will be {text_on_shirt}")
    print(f"\nYou have choosen to place the logo/text on {placement}")
    print(f"\nYour t-shirt will have the following elements size = {size_shirt}\nlogo/text on shirt = {text_on_shirt}\nplacement for text/logo = {placement}")
#Funktionen bliver her kaldt
make_shirt(55, "Fuck you", "Front and back")

#Selvom der er en defualt value som hedder large, kan dette laves om til medium ved at indsætte variablen lig med en ny som vist under
def make_large_shirt(text_on_t_shirt, placement, size_shirt = "large"):
    """T-shirt selecting proces"""
    print(f"\nYou have choosen the size {size_shirt} and the text on the shirt will be {text_on_t_shirt}")
    print(f"\nYou have choosen to place the logo/text on {placement}")
    print(f"\nYour t-shirt will have the following elements size = {size_shirt}\nlogo/text on shirt = {text_on_t_shirt}\nplacement for text/logo = {placement}")

make_large_shirt(text_on_t_shirt = "Hell Yeah",placement = "Only front", size_shirt = "medium")