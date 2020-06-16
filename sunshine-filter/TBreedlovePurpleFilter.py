def ssFilter():
 file = pickAFile()
 picture = makePicture(file)
 explore(picture)
 for p in getPixels(picture):
  value = getBlue(p)
  setBlue(p, value*0.7)
  value = getGreen(p)
  setGreen(p,value*0.7)
 explore(picture)

 
