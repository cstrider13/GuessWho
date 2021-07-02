#Empty Tile (0,0)
#Ear (0,12)
#Empty Tile (0, 24)
#Edge of shoulder (0, 36)

#Hair top (12, 0)
#Eyes (12, 12)
#Mouth (12, 24)
#Shirt (12, 36)

#TODO: color swap by manually setting colors

import PIL
from PIL import Image
import random
import numpy as np
from os import listdir
from os.path import isfile, join
from zipfile import ZipFile

#def mergeImages():
#Color codes for common colors
redCol = (237, 28, 36)
blueCol = (63, 72, 204)
greenCol = (34, 177, 76)
lightBlue = (153, 217, 234)
purpleCol = (163, 76, 164)
pinkCol = (255, 174, 201)
brownCol = (185, 122, 87)
blackCol = (0, 0, 0)
whiteCol = (255, 255, 255)
blondeCol = (255, 242, 0)

def makeEyeLashes(color):#Called to generate a picture of eyes with eyelashes
    eye = Image.open('Eyes/LightBlue_Eyelash_Eye.png') #Open the base file used as a reference
    eye = eye.convert('RGBA') #Convert the image so that the RGB data can be extracted
    data = np.array(eye)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 153) & (green == 217)  & (blue == 234)
    #print(red_spots)
    
    #This converts the image pixels to the appropriate color (color picked by user)
    if color == "Blue":
        data[..., :-1][red_spots.T] = blueCol
    elif color == "Green":
        data[..., :-1][red_spots.T] = greenCol
    elif color == "Red":
        data[..., :-1][red_spots.T] = redCol
    elif color == "Purple":
        data[..., :-1][red_spots.T] = purpleCol
    elif color == "Pink":
        data[..., :-1][red_spots.T] = pinkCol
    elif color == "Brown":
        data[..., :-1][red_spots.T] = brownCol
    elif color == "Black":
        data[..., :-1][red_spots.T] = blackCol
    elif color == "White":
        data[..., :-1][red_spots.T] = whiteCol

    newEye = Image.fromarray(data)
    string = "Eyes/" + str(color) + "_Eyelash_Eye.png"
    newEye.save(string, "PNG") #Saves the recolored eyelash to a file

def makeEyes(color):#Called to generate a file for an eye without eyelashes
    eye = Image.open('Eyes/LightBlue_Eye.png')#Open base reference image
    eye = eye.convert('RGBA') #Convert the image so that the RGB data can be extracted
    data = np.array(eye)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 153) & (green == 217)  & (blue == 234)
    #print(red_spots)
    
    #convert the pixels in image to the desired color
    if color == "Blue":
        data[..., :-1][red_spots.T] = blueCol
    elif color == "Green":
        data[..., :-1][red_spots.T] = greenCol
    elif color == "Red":
        data[..., :-1][red_spots.T] = redCol
    elif color == "Purple":
        data[..., :-1][red_spots.T] = purpleCol
    elif color == "Pink":
        data[..., :-1][red_spots.T] = pinkCol
    elif color == "Brown":
        data[..., :-1][red_spots.T] = brownCol
    elif color == "Black":
        data[..., :-1][red_spots.T] = blackCol
    elif color == "White":
        data[..., :-1][red_spots.T] = whiteCol

    newEye = Image.fromarray(data)
    string = "Eyes/" + str(color) + "_Eye.png"
    newEye.save(string, "PNG") #Saves the recolored eye to a file

def makeMouths(color):#Called to create a mouth of a desired color
    mouth = Image.open('Mouths/Red_Mouth.png')#Opens the base reference file
    mouth = mouth.convert('RGBA') #Convert the image so that the RGB data can be extracted
    data = np.array(mouth)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 237) & (green == 28)  & (blue == 36)
    #print(red_spots)
    
    #convert the pixels in the base image to the desired color
    if color == "Blue":
        data[..., :-1][red_spots.T] = blueCol
    elif color == "Green":
        data[..., :-1][red_spots.T] = greenCol
    elif color == "LightBlue":
        data[..., :-1][red_spots.T] = lightBlue
    elif color == "Purple":
        data[..., :-1][red_spots.T] = purpleCol
    elif color == "Pink":
        data[..., :-1][red_spots.T] = pinkCol
    elif color == "Brown":
        data[..., :-1][red_spots.T] = brownCol
    elif color == "Black":
        data[..., :-1][red_spots.T] = blackCol
    elif color == "White":
        data[..., :-1][red_spots.T] = whiteCol

    newMouth = Image.fromarray(data)
    string = "Mouths/" + str(color) + "_Mouth.png"
    newMouth.save(string, "PNG") #Saves the recolored mouth to a file

def makeShoulders(color):#Called to make an image file for shoulders of a certain color
    shoulder= Image.open('Shoulders/Red_Shoulder.png')#Opens the base reference image for shoulders
    shoulder = shoulder.convert('RGBA')#Convert the image so that the RGB data can be extracted
    data = np.array(shoulder)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 237) & (green == 28)  & (blue == 36)
    #print(red_spots)
    
    #convert the pixels in the base image to the desired color
    if color == "Blue":
        data[..., :-1][red_spots.T] = blueCol
    elif color == "Green":
        data[..., :-1][red_spots.T] = greenCol
    elif color == "LightBlue":
        data[..., :-1][red_spots.T] = lightBlue
    elif color == "Purple":
        data[..., :-1][red_spots.T] = purpleCol
    elif color == "Pink":
        data[..., :-1][red_spots.T] = pinkCol
    elif color == "Brown":
        data[..., :-1][red_spots.T] = brownCol
    elif color == "Black":
        data[..., :-1][red_spots.T] = blackCol
    elif color == "White":
        data[..., :-1][red_spots.T] = whiteCol

    newShoulder = Image.fromarray(data)
    string = "Shoulders/" + str(color) + "_Shoulder.png"
    newShoulder.save(string, "PNG") #Saves the recolored shoulders to a file

def makeShirts(color):#Called to create an image of a shirt of a desired color
    shirt= Image.open('Shirts/Red_Shirt.png')#Open the base reference image
    shirt = shirt.convert('RGBA')#Convert the image so that the RGB data can be extracted
    data = np.array(shirt)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 237) & (green == 28)  & (blue == 36)
    #print(red_spots)
    
    #convert the pixels in the base image to the desired color
    if color == "Blue":
        data[..., :-1][red_spots.T] = blueCol
    elif color == "Green":
        data[..., :-1][red_spots.T] = greenCol
    elif color == "LightBlue":
        data[..., :-1][red_spots.T] = lightBlue
    elif color == "Purple":
        data[..., :-1][red_spots.T] =  purpleCol
    elif color == "Pink":
        data[..., :-1][red_spots.T] = pinkCol
    elif color == "Brown":
        data[..., :-1][red_spots.T] = brownCol
    elif color == "Black":
        data[..., :-1][red_spots.T] = blackCol
    elif color == "White":
        data[..., :-1][red_spots.T] = whiteCol

    newShirt = Image.fromarray(data)
    string = "Shirts/" + str(color) + "_Shirt.png"
    newShirt.save(string, "PNG") #Saves the recolored shoulders to a file

def makeHairs(color):#Called to create an image file of hair of a certain color
    #hair = Image.new('RGB', (12,12), (255,255,255))
    hair = Image.open('Hair/Red_Spike_Hair.png')#Open the base reference image. This is changed to generate differently colored hairs of different styles
    hair = hair.convert('RGBA')#Convert the image so that the RGB data can be extracted
    data = np.array(hair)
    red, green, blue, alpha = data.T
    #print()
    
    #print(hair.getpixel((3,11)))
    
    red_spots = (red == 237) & (green == 28) & (blue == 36)
    #print(red_spots.T)
    
    #convert the pixels in the base image to the desired color
    if color == "Blue":
        data[..., :-1][red_spots.T] = blueCol
    elif color == "Green":
        data[..., :-1][red_spots.T] = greenCol
    elif color == "LightBlue":
        data[..., :-1][red_spots.T] = lightBlue
    elif color == "Purple":
        data[..., :-1][red_spots.T] =  purpleCol
    elif color == "Pink":
        data[..., :-1][red_spots.T] = pinkCol
    elif color == "Brown":
        data[..., :-1][red_spots.T] = brownCol
    elif color == "Black":
        data[..., :-1][red_spots.T] = blackCol
    elif color == "White":
        data[..., :-1][red_spots.T] = whiteCol
    elif color == "Blonde":
        data[..., :-1][red_spots.T] = blondeCol
    
    #TODO:N DO THE HINGS
    
    newHair = Image.fromarray(data)
    string = "Hair/" + str(color) + "_Spike_Hair.png"
    newHair.save(string, "PNG") #Saves the recolored hair to a file

def randomMouths():#Called to pick the name of a random mouth file to use for person generation
    mouthI = random.randint(0,20)
    if mouthI == 0:
        return 'Mouths/Normal_Mouth.png'
    elif mouthI == 1:
        return 'Mouths/Blue_Mouth.png'
    #elif mouthI == 2:
    #    return 'Mouths/Brown_Mouth.png'
    elif mouthI == 2:
        return 'Mouths/Green_Mouth.png'
    elif mouthI == 3:
        return 'Mouths/Pink_Mouth.png'
    #elif mouthI == 4:
    #    return 'Mouths/Purple_Mouth.png'
    #elif mouthI == 6:
    #    return 'Mouths/Red_Lips_Pink_Blush_Mouth.png'
    elif (mouthI >= 4) & (mouthI < 12):
        return 'Mouths/Red_Mouth.png'
    else:
        return 'Mouths/Normal_Mouth.png'
    
def randomShirts():#Called to pick the name of a random shirt file to use for person generation
    shirtI = random.randint(0,4)#6)#Generate a random number
    if shirtI == 0:
        return 'Shirts/Black_Shirt.png', 'Shoulders/Black_Shoulder.png'
    elif shirtI == 1:
        return 'Shirts/Blue_Shirt.png', 'Shoulders/Blue_Shoulder.png'
    #elif shirtI == 2:
    #    return 'Shirts/Brown_Shirt.png', 'Shoulders/Brown_Shoulder.png'
    elif shirtI == 2:
        return 'Shirts/Green_Shirt.png', 'Shoulders/Green_Shoulder.png'
    #elif shirtI == 4:
    #    return 'Shirts/Pink_Shirt.png', 'Shoulders/Pink_Shoulder.png'
    elif shirtI == 3:
        return 'Shirts/Purple_Shirt.png', 'Shoulders/Purple_Shoulder.png'
    elif shirtI == 4:
        return 'Shirts/Red_Shirt.png', 'Shoulders/Red_Shoulder.png'
#    elif shirtI == 5:
#        return 'Shirts/Blue_Shirt.png', 'Shoulders/Blue_Shoulder.png'
    else:
        return 'Shirts/Red_Shirt.png', 'Shoulders/Red_Shoulder.png'

def randomHair():#Called to pick the name of a random hair file to use for person generation
    files = [f for f in listdir("Hair") if ".png" in f]
    hairI = random.randint(0,len(files)+5)#Generate a random number within the number of hair files available
    #print(len(files))
    for i in range(len(files)):
        #print(files[i])
        #print("i=" + str(i))
        if hairI == i:
            string = "Hair/" + str(files[i])
            return string
    return 'Hair/Bald_Hair.png'
#    if hairI == 0:
#        return 'Hair/Bald_Hair.png'
#    elif hairI == 1:
#        return 'Hair/Black_Spike_Hair.png'
#    elif hairI == 2:
#        return 'Hair/Blue_Spike_Hair.png'
#    elif hairI == 3:
#        return 'Hair/Brown_Spike_Hair.png'
    #elif hairI == 3:
    #    return 'Hair/Green_Spike_Hair.png'
#    elif hairI == 4:
#        return 'Hair/Pink_Spike_Hair.png'
#    elif hairI == 5:
#        return 'Hair/Blonde_Spike_Hair.png'
    #elif hairI == 6:
    #    return 'Hair/Purple_Spike_Hair.png'
#    elif hairI == 6:
#        return 'Hair/Red_Spike_Hair.png'
#    else:
#        return 'Hair/Bald_Hair.png'
    
def randomNaturalHair(): #Called to pick the name of a random naturally colored hair file to use for person generation
    hairI = random.randint(0,6)#Generate a random number
    if hairI == 0:
        return 'Hair/Bald_Hair.png'
    elif hairI == 1:
        return 'Hair/Black_Spike_Hair.png'
    elif hairI == 2:
        return 'Hair/Brown_Spike_Hair.png'
    elif hairI == 3:
        return 'Hair/Red_Spike_Hair.png'
    elif hairI == 4:
        return 'Hair/Blonde_Spike_Hair.png'
    else:
        return 'Hair/Brown_Spike_Hair.png'    
        
def randomEyes():#Called to pick the name of a random mouth file to use for person generation
    #files = [f for f in listdir("Eyes") if ".png" in f]
    eyeI = random.randint(0,100)#len(files)) #Generate a random number
    #if eyeI == 0:
    #    return files[0]
    #for i in range(len(files)):
    #    if eyeI == i:
    #        return files[i]
    if eyeI < 50:#The probabilities are meant to roughly mirror naturally occurring odds of different eye colors.
        eyeI2 = random.randint(0,1)#This rolls probability for gender (with or without eyelashes)
        if eyeI2 == 0:
            return 'Eyes/Brown_Eye.png'
        else: 
            return 'Eyes/Brown_Eyelash_Eye.png'
    elif eyeI >= 50 & eyeI < 80:
        eyeI2 = random.randint(0,1)#This rolls probability for gender (with or without eyelashes)
        if eyeI2 == 0:
            return 'Eyes/Blue_Eye.png'
        else: 
            return 'Eyes/Blue_Eyelash_Eye.png'
    elif eyeI >= 80:
        eyeI2 = random.randint(0,1)#This rolls probability for gender (with or without eyelashes)
        if eyeI2 == 0:
            return 'Eyes/Green_Eye.png'
        else: 
            return 'Eyes/Green_Eyelash_Eye.png'
    else:
        return 'Eyes/Blue_Eye.png'#This is the default eye image. 
    
def randomEars():#TODO: Could do one ear and not the other #Called to pick the name of a random ear file to use for person generation
    earI = random.randint(0,2)
    if earI == 0:
        return 'Ears/No_Ear.png'
    elif earI == 1:
        return 'Ears/Normal_Ear.png'
    else:
        return 'Ears/No_Ear.png'
    
def makeFace():#Called to generate a person
    hairPick = randomHair()#Returns the name of a random hair file
    hairImg = Image.open(hairPick)#Returns the opened file of filename=hairPick
    
    earPick = randomEars()#Returns the name of a random ear file
    earImg = Image.open(earPick)#Returns the opened file of filename=earPick
    
    eyePick = randomEyes()#Returns the name of a random eye file
    eyeImg = Image.open(eyePick)#Returns the opened file of filename=eyePick
    
    mouthPick = randomMouths()#Returns the name of a random mouth file
    mouthImg = Image.open(mouthPick)#Returns the opened file of filename=mouthPick
    
    shirtPick, shoulderPick = randomShirts()#Returns the name of a shirt and a shoulder image (they are held seperately)
    shirtImg = Image.open(shirtPick)#Returns the opened file of filename=shirtPick
    shoulderImg = Image.open(shoulderPick)#Returns the opened file of filename=shoulderPick
    blankImg = Image.open('Blank.png')#Opens up a blank slate to work with
    
    faceImg = Image.new('RGB', (24, 48), (255,255,255))#Creates a workable size of the blank picture. It is half the size of the final image
    faceImg.paste(earImg, (0,12))#Applies the ears to the face
    faceImg.paste(shoulderImg, (0, 36))#Applies the shoulders to the body
    faceImg.paste(hairImg, (12, 0))#Applies the hair to the head
    faceImg.paste(eyeImg, (12, 12))#Applies the eyes to the face
    faceImg.paste(mouthImg, (12, 24))#Applies the mouth to the face
    faceImg.paste(shirtImg, (12, 36))#Applies a shirt to the body
    
    #faceImg.save("FinishedFaces/testFace.png", "PNG")
    #faceImg.show()
    
    finalImg = Image.new('RGB', (48, 48), (255,255,255))#Creates the blank template for the final image (double the size of the intermediate picture)
    rightImg = faceImg.transpose(PIL.Image.FLIP_LEFT_RIGHT)#Pictures are drawn for half of the face. This flips the image so that the final picture is symmetrical and complete
    finalImg.paste(faceImg, (0, 0))#Copies over the previous picture to the left half off the canvas
    finalImg.paste(rightImg, (24, 0))#Copies over the mirrored left half of the person to the right half of the canvas
    
    #Empty, Ear, Empty, Shoulder
    #Hair, Eyes, Mouth, Shirt
    
    #All of these will work together to create a unique name for the generated face based on the randomly sampled elements.
    hairStr0 = hairPick.partition("/")[2]
    hairHold = hairStr0.partition("_")[0]
    hairStr1 = hairStr0.partition("_")[2]
    hairStr2 = hairStr1.partition("_")[0]
    hairStr = hairHold + hairStr2
    
    earStr = earPick.partition("/")[2]
    earStr = earStr.partition("_")[0]
    
    eyeLashVal = eyePick.count("_")
    if (eyeLashVal > 1):
        eyeStr0 = eyePick.partition("/")[2]
        eyeHold = eyeStr0.partition("_")[0]
        eyeStr1 = eyeStr0.partition("_")[2]
        eyeStr2 = eyeStr1.partition("_")[0]
        eyeStr = eyeHold + eyeStr2
    else:
        eyeStr = eyePick.partition("/")[2]
        eyeStr = eyeStr.partition("_")[0]
    
    mouthStr = mouthPick.partition("/")[2]
    mouthStr = mouthStr.partition("_")[0]
    
    shirtStr = shirtPick.partition("/")[2]
    shirtStr = shirtStr.partition("_")[0]
    
    helpStr = hairStr + "Hr_" + earStr + "Er_" + eyeStr + "Ey_" + mouthStr + "Mth_" + shirtStr + "Shrt"
    
    #print(helpStr)
    finalStr = "FinishedFaces/" + str(helpStr) + ".png"#Final file name for the finished image.
    
    finalImg.save(finalStr, "PNG")#Saves the completed image.

def resizePixels():#Called to resize final images so that they are usable in a game of Guess Who (Pixel art is small and hard to see before being resized)
    files = [f for f in listdir("FinishedFaces") if ".png" in f]#List of files in the FinishedFaces folder
    zipPics = ZipFile("picZip.zip", "w")#Makes zipfile for final resized faces to be put into
    for file in files:#Iterates through the files
        #print(file)
        helpStr = "FinishedFaces/" + str(file)
        image = Image.open(helpStr)
        image = image.resize((image.size[0] * 10, image.size[1] * 10), Image.NEAREST)
        finalStr = "BiggerFaces/" + str(file)#Generate the new file name.
        image.save(finalStr, "PNG")
        zipPics.write(finalStr)#Put enlarged file into the zip
    zipPics.close()#close it up

#for i in range(0,25):#This for loop will generate that number of faces
#    makeFace()#Call this to generate faces
resizePixels()#Called to resize the generated files in the "FinishedFaces" folder

