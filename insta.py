from PIL import Image
import image_utils


print(".__                 __")                                       
print("|__| ____   _______/  |______     ________________    _____")  
print("|  |/    \ /  ___/\   __\__  \   / ___\_  __ \__  \  /     \ ")
print('|  |   |  \\___ \  |  |  / __ \_/ /_/  >  | \// __ \|  Y Y  \\')
print("|__|___|  /____  > |__| (____  /\___  /|__|  (____  /__|_|  /")
print("        \/     \/            \//_____/            \/      \/") 


while(True):
	msg = input('(f)ilter an image or (q)uit\n')
	if (msg == 'f' or msg == 'F'):
		path = input('What\'s the full path to your image?\n')
		write = input('Write a series of filters to apply: \n(p)ixelate\n(k)aleidoscope\n(g)ray-day\n(r)ighty\nExample: kpkr will run keleidoscope, pixelate, kaleidoscope and gray-day in sequence.\n')
		image = Image.open(path)
		pic = image

		
		for char in write:
			
			if(char == 'g'):
				pic = image_utils.grayscale(pic)
			elif(char == 'r'):
				pic = image_utils.righty(pic)
			elif(char == 'k'):
				pic = image_utils.kaleidoscope(pic)
			elif(char == 'p'):
				pic = image_utils.pixelate(pic)
			else:
				print("pls type p,k,g,r, or any combination of them")
				break;
	
		pic.show()
		
	elif (msg == 'q'):
		break
	else:
		print("pls type f or q")
