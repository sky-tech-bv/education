from PIL import Image

tab = Image.open('word_matrix.png')
image_size = tab.size
mask = Image.open('mask.png')
mask.resize(image_size)
tab.paste(mask)
tab.show()