# -*- coding: utf-8 -*-


from PIL import Image
im = Image.open('wei.jpg')

w, h = im.size
print('Original image size: %s*%s' % (w, h))

im.thumbnail((w//2, h//2))
print('Resize image to: %s*%s' % (w//2, h//2))

im.save('thumbnail.jpg', 'jpeg')
