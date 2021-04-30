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

def makeEyeLashes(color):
    eye = Image.open('Eyes/LightBlue_Eyelash_Eye.png')
    eye = eye.convert('RGBA')
    data = np.array(eye)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 153) & (green == 217)  & (blue == 234)
    #print(red_spots)
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
    newEye.save(string, "PNG") 

def makeEyes(color):
    eye = Image.open('Eyes/LightBlue_Eye.png')
    eye = eye.convert('RGBA')
    data = np.array(eye)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 153) & (green == 217)  & (blue == 234)
    #print(red_spots)
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
    newEye.save(string, "PNG") 

def makeMouths(color):
    mouth = Image.open('Mouths/Red_Mouth.png')
    mouth = mouth.convert('RGBA')
    data = np.array(mouth)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 237) & (green == 28)  & (blue == 36)
    #print(red_spots)
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
    newMouth.save(string, "PNG") 

def makeShoulders(color):
    shoulder= Image.open('Shoulders/Red_Shoulder.png')
    shoulder = shoulder.convert('RGBA')
    data = np.array(shoulder)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 237) & (green == 28)  & (blue == 36)
    #print(red_spots)
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
    newShoulder.save(string, "PNG") 

def makeShirts(color):
    shirt= Image.open('Shirts/Red_Shirt.png')
    shirt = shirt.convert('RGBA')
    data = np.array(shirt)
    red, green, blue, alpha = data.T
    #print(shirt.getpixel((3,11)))
    #(237, 28, 36, 255)
    
    red_spots = (red == 237) & (green == 28)  & (blue == 36)
    #print(red_spots)
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
    newShirt.save(string, "PNG") 

def makeHairs(color):
    #hair = Image.new('RGB', (12,12), (255,255,255))
    hair = Image.open('Hair/Red_Spike_Hair.png')
    hair = hair.convert('RGBA')
    data = np.array(hair)
    red, green, blue, alpha = data.T
    #print()
    
    #print(hair.getpixel((3,11)))
    
    red_spots = (red == 237) & (green == 28) & (blue == 36)
    #print(red_spots.T)
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
    newHair.save(string, "PNG") 

def randomMouths():
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
    
def randomShirts():
    shirtI = random.randint(0,4)#6)
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

def randomHair():
    files = [f for f in listdir("Hair") if ".png" in f]
    hairI = random.randint(0,len(files)+5)
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
    
def randomNaturalHair():
    hairI = random.randint(0,6)
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
        
def randomEyes():
    #files = [f for f in listdir("Eyes") if ".png" in f]
    eyeI = random.randint(0,100)#len(files))
    #if eyeI == 0:
    #    return files[0]
    #for i in range(len(files)):
    #    if eyeI == i:
    #        return files[i]
    if eyeI < 50:
        eyeI2 = random.randint(0,1)
        if eyeI2 == 0:
            return 'Eyes/Brown_Eye.png'
        else: 
            return 'Eyes/Brown_Eyelash_Eye.png'
    elif eyeI >= 50 & eyeI < 80:
        eyeI2 = random.randint(0,1)
        if eyeI2 == 0:
            return 'Eyes/Blue_Eye.png'
        else: 
            return 'Eyes/Blue_Eyelash_Eye.png'
    elif eyeI >= 80:
        eyeI2 = random.randint(0,1)
        if eyeI2 == 0:
            return 'Eyes/Green_Eye.png'
        else: 
            return 'Eyes/Green_Eyelash_Eye.png'
    else:
        return 'Eyes/Blue_Eye.png'
    
def randomEars():#TODO: Could do one ear and not the other
    earI = random.randint(0,2)
    if earI == 0:
        return 'Ears/No_Ear.png'
    elif earI == 1:
        return 'Ears/Normal_Ear.png'
    else:
        return 'Ears/No_Ear.png'
    
def makeFace():
    hairPick = randomHair()
    hairImg = Image.open(hairPick)
    
    earPick = randomEars()
    earImg = Image.open(earPick)
    
    eyePick = randomEyes()
    eyeImg = Image.open(eyePick)
    
    mouthPick = randomMouths()
    mouthImg = Image.open(mouthPick)
    
    shirtPick, shoulderPick = randomShirts()
    shirtImg = Image.open(shirtPick)
    shoulderImg = Image.open(shoulderPick)
    blankImg = Image.open('Blank.png')
    
    faceImg = Image.new('RGB', (24, 48), (255,255,255))
    faceImg.paste(earImg, (0,12))
    faceImg.paste(shoulderImg, (0, 36))
    faceImg.paste(hairImg, (12, 0))
    faceImg.paste(eyeImg, (12, 12))
    faceImg.paste(mouthImg, (12, 24))
    faceImg.paste(shirtImg, (12, 36))
    
    #faceImg.save("FinishedFaces/testFace.png", "PNG")
    #faceImg.show()
    
    finalImg = Image.new('RGB', (48, 48), (255,255,255))
    rightImg = faceImg.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    finalImg.paste(faceImg, (0, 0))
    finalImg.paste(rightImg, (24, 0))
    
    #Empty, Ear, Empty, Shoulder
    #Hair, Eyes, Mouth, Shirt
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
    finalStr = "FinishedFaces/" + str(helpStr) + ".png"
    
    finalImg.save(finalStr, "PNG")

def resizePixels():
    files = [f for f in listdir("FinishedFaces") if ".png" in f]
    zipPics = ZipFile("picZip.zip", "w")
    for file in files:
        #print(file)
        helpStr = "FinishedFaces/" + str(file)
        image = Image.open(helpStr)
        image = image.resize((image.size[0] * 10, image.size[1] * 10), Image.NEAREST)
        finalStr = "BiggerFaces/" + str(file)
        image.save(finalStr, "PNG")
        zipPics.write(finalStr)
    zipPics.close()

#for i in range(0,25):
#    makeFace()
resizePixels()

