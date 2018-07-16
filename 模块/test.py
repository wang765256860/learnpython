from PIL import Image

im = Image.open('5656.jpeg')

w,h = im.size
print('Original image size:%s %s'%(w,h))
im.thumbnail(w//2,h//2)
im.save('thumbnail.jpeg','jpeg')