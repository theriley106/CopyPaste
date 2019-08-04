from pytesseract import pytesseract
from PIL import Image
import os

def scan_image():
	os.system("./scanline -flatbed -jpg -dir . -name temp_result")

def deskew_image(src="temp_result.jpg", dst="temp_image2.jpg", percent=40):
	os.system("convert {} -deskew {}% {}".format(src, percent, dst))
	#os.system("mv ")

def deskew_flatten_image(src="temp_final8.png", dst="temp_image2.jpg", percent=50):
	os.system("convert {} -flatten -deskew {}% {}".format(src, percent, dst))


def make_transparent(src="temp_image2.jpg", dst="temp_result.png"):
	os.system('magick {} -fuzz 10% -bordercolor "#eeeced" -border 1 -fill none -draw "alpha 0,0 floodfill" -shave 1x1 {}'.format(src, "temp_result.png"))
	os.system('magick temp_result.png -fuzz 10% -bordercolor "#a89ca0" -border 1 -fill none -draw "alpha 0,0 floodfill" -shave 1x1 {}'.format(dst))

def remove_noise(src="temp_result.png", dst="temp_final3.png"):
	os.system("convert {} -channel a -morphology open octagon:5 +channel temp.png".format(src))
	os.system("convert temp.png -fuzz 10% -trim +repage {}".format(dst))
	os.system("rm temp.png")

def remove_rotation(src="temp_final3.png", dst="temp_final8.png"):
	os.system("./unrotate {} {}".format(src, dst))

def finalize(src="temp_final3.png", dst="final.png"):
	os.system("mv {} {} && rm temp_*".format(src, dst))

def calc_consistant(string):
	score = 0
	prevInt = True
	prevCapital = False
	#prevLower = False
	for char in string:
		if prevInt:
			try:
				int(char)
				score += 1
			except:

				score = score - 1
				prevCapital = char.isupper()
				prevInt = False
		else:
			try:
				if prevCapital == char.isupper():
					score += 1
				else:
					prevCapital = char.isupper()
					prevInt = False
			except:
				#score = score - 1
				try:
					int(char)
					prevInt = True
				except:
					print("ERROR")
	return score

def rotate_image(imageFile, rotate=False):
	imageObject = Image.open(imageFile)
	# This opens the image file you specify
	if rotate:
		imageObject = imageObject.rotate(180)
	return pytesseract.image_to_string(imageObject)

def correct_rotate(imageFile):
	im = Image.open(imageFile)
	width, height = im.size

	if height > width:
		size = height,width
		im.rotate(90,expand=True).save(imageFile)
	flippedImage = rotate_image(imageFile, True)
	flippedScore = calc_consistant(flippedImage)
	regularImage = rotate_image(imageFile, False)
	regularScore = calc_consistant(regularImage)
	if regularScore < flippedScore:
		imageObject = Image.open(imageFile).rotate(180)
		imageObject.save(imageFile)
	else:
		imageObject = Image.open(imageFile)
		imageObject.save(imageFile)

if __name__ == '__main__':
	scan_image()
	deskew_image()
	make_transparent()
	remove_noise()
	remove_rotation()
	deskew_flatten_image()
	make_transparent()
	remove_noise()
	finalize()
	correct_rotate("final.png")
	