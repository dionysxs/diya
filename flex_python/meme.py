import PIL
from PIL import Image, ImageFont, ImageDraw
afbeelding = Image.open("baldman.jpg")
breedte = afbeelding.width
hoogte = afbeelding.height
print("De afbeelding is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")
helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2
nieuwe_afmeting = (helft_breedte, helft_hoogte)
#kleinere_afbeelding = afbeelding.resize(nieuwe_afmeting)
#kleinere_afbeelding.save('th.jpg')
lettertype = ImageFont.truetype("impact.ttf", 20)
tekengebied = ImageDraw.Draw(afbeelding)
tekst = "HOLY SHIT I'M\n  \n  \n  \n  \n  \n  \n  I'M FUCKING BALD"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(0,0,0))
afbeelding.show()