#lab6_JuanCallejas_100143996.py
#By Juan Callejas
#COMP 1110L X1
#Instructor: Greg Lee

def Quarters (img):
    
    #Seriously? Why not let us use a primitive colour like with the other corners instead of having to define a new one smh
    purple = makeColor (152, 0, 255)
    w = img.getWidth()
    h = img.getHeight()
    
    for pix in img.getPixels ():
        
        x = pix.getX()
        y = pix.getY()
        
        top = true
        left = true
        
        if (x > w / 2):
            left = false
        if (y > h / 2):
            top = false
        
        if top:
            if left:
                invert (pix)
            else:
                greyscale (pix)
        else:
            if left:
                RGB_Percent (pix, 0, 1, 1)
            else:
                SwapGreenBlue (pix)
                
        if (x < w / 4):
            if (y < h / 4):
                pix.setColor (yellow)
            elif (y > (h / 4) * 3):
                pix.setColor (orange)
        elif (x > (w / 4) * 3):
            if (y < h / 4):
                pix.setColor (pink)
            elif (y > (h / 4) * 3):
                pix.setColor (purple)
                
    return img
                
        
#So-called "negatize"
def invert (pix):
	pix.setColor (makeColor(255 - pix.getRed(), 255 - pix.getGreen(), 255 - pix.getBlue()))
	return pix
	
#Unlike Assignment 2, this method will actually use the correct
#method of obtaining the greyscale value of a pixel, which is by
#calculating the average of the RGB values, instead of using the
#smallest value for all three.
def greyscale (pix):
	value = (pix.getRed() + pix.getGreen() + pix.getBlue()) / 3
	pix.setColor (makeColor (value, value, value))
	return pix
	
#To eliminate all red, this method will be used with parameters (0, 1, 1)
#Which will use 0% red and 100% green and blue
def RGB_Percent (pix, r, g, b):
	pix.setRed (int (float (pix.getRed()) * r))
	pix.setGreen (int (float (pix.getGreen()) * g))
	pix.setBlue (int (float (pix.getBlue()) * b))
    
def SwapGreenBlue (pix):
    #Store the green value in a variable since it will be overridden before we use it
    green = pix.getGreen()
    pix.setGreen (pix.getBlue())
    pix.setBlue (green)