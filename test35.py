#!/usr/bin/python2
# coding: UTF-8

# test for adding number to a picture

import Image
import ImageDraw
import ImageFont
import os

if not os.access("./cat_new.jpeg", os.F_OK):
	im = Image.open("./cat.jpeg")
	imsize = im.size
	im2 = im.resize((imsize[0]/2, imsize[1]/2))
	box = (0, 0, im2.size[0]/2, im2.size[1])
	im3 = im2.crop(box)
	im3.save("./cat_new.jpeg")

num = raw_input("input the number you want to add:")

im = Image.open("./cat_new.jpeg")
im.show()
imsize = im.size
draw = ImageDraw.Draw(im)
#font = ImageFont.truetype("Arial.ttf", 36)
draw.text((imsize[0] - 10, 5), num, fill = (255, 0, 0))
im.show()
im.save("add.jpeg")


