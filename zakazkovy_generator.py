import random
import os
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

city_list = ['Birmingham','Swansea','Cambridge','Cardiff','Plymouth','Southampton','Londýn','Dover','Calais','Lille','Le Havre','Roscoff','Brest','Rennes','Nantes','Le Mans','Paříž','Remeš','La Rochelle','Bordeaux','Limoges','Bourges','Clermont-Ferrand','Lyon','Dijon','Mety','Brusel','Lutych','Rotterdam','Amsterdam','Groningen','Brémy','Hamburk','Kolín','Dortmund','Osnabruck','Rostock','Kassel','Frankfurt n. M.','Norimberk','Magdeburg','Lipsko','Berlín','Štětín','Drážďany','Stuttgart','Štrasburk','Mnichov','Innsbruck','Salzburg','Vídeň','Curych','Praha','Turín','Janov','Miláno','Verona','Benátky','Terst','Rijeka','Lublaň','Maribor','Záhřeb','Št. Hradec','Bratislava','Vídeň','Budapešť','Szeged','Debrecín','Košice','Krakov','Lublin','Lodž','B. Bystrica','Ostrava','Katovice','Krakov','Linec','Klagenfurt','Gdaňsk','Olštýn','Bělostok','Varšava','Poznaň']
zakazky_list_normal = ['brambory','cihly','hračky','jablka','kancelářský papír','bagry','cukr','elektronika','hovězí maso','klády','mouka','oblečení','pneumatiky','rýže','sýry','prázdná nádrž','velké trubky','zmrzlina','železné trubky']
zakazky_list_adr = ['acetylen','arzen','benzín','draslík','bílý fosfor','dynamit','fluor','hydroxid draselný','chemikálie','chlór','chlornan sodný','kyselina','kyselina sírová','pesticidy','ropa','petrolej','výbušniny','vodík','zábavní pyrotechnika','vodík','sodík']
zakazky_list_special = ['auta','balené sklo','bagry','nakladač Digger 500','nakladač Digger 1000','nápoje','potřeby ke stolování','tlaková nádrž','vysokozdvižné vozíky','rypadlo']
id = 0
current = 0
wanted = 0
placed_id = 0

def vytvor_zakazku():
    global departure
    global destination
    global zakazka
    global typ
    j = random.randint(0,83)
    departure = city_list[j]
    j = random.randint(0,83)
    destination = city_list[j]

    j = random.randint(0,2)
    if j == 0:
        j = random.randint(0,len(zakazky_list_normal) - 1)
        zakazka = zakazky_list_normal[j]
        typ = "Normální"
    elif j == 1:
        j = random.randint(0,len(zakazky_list_adr) - 1)
        zakazka = zakazky_list_adr[j]
        typ = "ADR"
    elif j == 2:
        j = random.randint(0,len(zakazky_list_special) - 1)
        zakazka = zakazky_list_special[j]
        typ = "Speciální"

wanted = int(input("Enter amount: "))

print("Starting generator...")
while current != wanted:
    vytvor_zakazku()
    if departure == destination:
        vytvor_zakazku()    

    image_width = 700
    image_height = 200
    background_color = (255, 255, 255) 
    image = Image.new('RGB', (image_width, image_height), background_color)

    font = ImageFont.truetype('arial.ttf', 26)  
    font_ = ImageFont.truetype('arial.ttf', 18)  
    text_color = (0, 0, 0)  

    #adding base.png (can be modified in file explorer, size needs to be 700x200px)
    image_to_add = Image.open('base.png')
    image_to_add_width, image_to_add_height = image_to_add.size
    image.paste(image_to_add, (0, 0))  

    image_to_add = Image.open('Brno.png')
    image_to_add_width, image_to_add_height = image_to_add.size

    image_to_add = image_to_add.resize((360, 180)) 

    image.paste(image_to_add, (12, 12))  

    draw = ImageDraw.Draw(image)
    draw.text((400, 25),departure + " - " + destination,font=font,fill=text_color)
    draw.text((400, 88),typ + " - " + zakazka.capitalize(),font=font_,fill=text_color)

    image.save("zakazka_" + str(id) + ".png")
    print("Created image "+str(id + 1) +"/"+str(wanted),end="\r")
    current = current + 1
    id = id + 1

print("Everything is generated, ready to place these images onto A4 paper...")
print("Starting placing...")

due = wanted
id = 0
while due > 0:
    image_width = 2500
    image_height = 3500
    background_color = (255, 255, 255)  # White
    image = Image.new('RGB', (image_width, image_height), background_color)
    current = 0
    x = 35
    y = 50
    while current != 16:
        while current < 8:
            image_to_add = Image.open('zakazka_'+ str(id) +'.png')
            image_to_add_width, image_to_add_height = image_to_add.size
            image_to_add = image_to_add.resize((1200, 342))
            image.paste(image_to_add, (x, y)) 
            os.remove("C:/Users/kubik/Documents/Python/zakazka_"+str(id)+".png") 
            y = y + 400
            print("Placed image zakazka_" + str(id) + ".png",end="\r")
            current = current + 1
            id = id + 1   
        y = 50
        while current > 7 and current < 16:
            image_to_add = Image.open('zakazka_'+ str(id) +'.png')
            image_to_add_width, image_to_add_height = image_to_add.size
            image_to_add = image_to_add.resize((1200, 342))
            image.paste(image_to_add, (x + 1250, y))  
            os.remove("C:/Users/kubik/Documents/Python/zakazka_"+str(id)+".png") 
            y = y + 400
            print("Placed image zakazka_" + str(id) + ".png",end="\r")
            current = current + 1
            id = id + 1
    due = due - 16
    current = 0
    placed_id = placed_id + 1
    image.save("zakazky_tisk_" + str(placed_id) + ".png")
    print("Page number " + str(placed_id)+"/"+str(int(wanted/16)) + " successfully saved.")
    
messagebox.showinfo("Success!","Everything is packed into " + str(placed_id) + " pages of A4 paper.")

#A je hotovo, copyright Jakub Chvílíček 2024