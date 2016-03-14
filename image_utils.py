from PIL import Image

#this function from slides
def grayscale(img):
    pixels = img.load() 
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            avg = sum(pixels[i,j]) // 3
            pixels[i,j] = (avg,) * 3
    return img

def righty(img):
	pixels = img.load()
	img2 = Image.new('RGB',(img.size[1], img.size[0]), (0,0,0))
	pixels2 = img2.load()

	for i in range(img2.size[0]):
		for j in range(img2.size[1]):
			pixels2[img2.size[0] - i - 1,j] = pixels[j,i]
	return img2

#this function adapted from slides
def pixelate(img):
	pixels = img.load()

	width = img.size[0]
	height = img.size[1]
	#pixelsize is set to 10 just because the problem specs
	#state that the squares should be 10x10 pixels large
	#if you want to make it less blurry, decrement this variable
	#conversely, if you want to make it more blurry, increment this variable
	ps = 10
	img2 = Image.new('RGB', (img.size[0],img.size[1]), (0,0,0))
	pixels2 = img2.load()
	
	for i in range(0,width - ps, ps):
		for j in range(0,height-ps, ps):
			for k in range(i, i + ps):
				for l in range(j, j +ps):
					pixels2[k,l] = pixels[i,j];
	return img2


def kaleidoscope(img):
	w = img.size[0]
	h = img.size[1]
	#lower left, lower right, upper left, and upper right respectively
	ll = shrink(img)
	lr = horizontal(ll)
	ul = vertical(ll)
	ur = vertical(lr)

	llPixels = ll.load()
	lrPixels = lr.load()
	ulPixels = ul.load()
	urPixels = ur.load()

	img2 = Image.new('RGB', (w, h), (0,0,0))
	pixels2 = img2.load()

	for i in range(0, w// 2):
		for j in range(0, h//2):
			pixels2[i,j] = ulPixels[i,j]

	for i in range(0, w// 2):
		for j in range(h// 2, h):
			pixels2[i, j] = llPixels[i, j - h // 2]

	for i in range(w // 2, w - 1):
		for j in range(h // 2, h):
			pixels2[i,j] = lrPixels[i - w//2, j - h //2]

	for i in range(w // 2, w-1):
		for j in range(0, h//2):
			pixels2[i,j] = urPixels[i - w//2, j]
	return img2
#helper functions for kaleidoscope
def shrink(img):
	pixels = img.load()
	img2 = Image.new('RGB', (img.size[0] // 2 , img.size[1] // 2))
	pixels2 = img2.load()
	
	for j in range(img2.size[0]):
		for i in range(img2.size[1]):
			pixels2[j,i] = pixels[j*2, i*2]
	return img2

def vertical(img):
	pixels = img.load()
	w,h = img.size
	img2 = Image.new('RGB', (w,h), (0,0,0))
	pixels2 = img2.load()
	
	for x in range(w):
		for y in range(h): 
			pixels2[x,y] = pixels[x , h - y - 1]
	return img2

	
def horizontal(img):
	pixels = img.load()
	w,h = img.size
	img2 = Image.new('RGB', (w,h), (0,0,0))
	pixels2 = img2.load()
	
	for x in range(w):
		for y in range(h): 
			pixels2[x,y] = pixels[w - x -1, y]
	return img2
