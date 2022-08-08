from base64 import decodebytes,encodebytes
exec(decodebytes(encodebytes(b"""from random import randint
from PIL import Image
colors={(81,126,231),(255,229,229),(123,108,108),(206,78,78)}
for i in range(randint(1,10)):rand={(randint(0,255),randint(0,255),randint(0,255))for i in range(len(colors))}
cl=list(colors)
cr=list(rand)
new=[]
img=Image.open('blob.jpg').convert('RGB')
for i in img.getdata():new.append(i if i not in colors else cr[cl.index(i)])
img.putdata(new)
img.save('new.jpg')
# img.show()""")))