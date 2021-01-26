############
# QUESTION 6 - Bonus
############
# a

from PIL import Image  # need to install PIL/PILLOW


def what(img):
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()

    for x in range(w):
        ls_aux = [mat[x, y] for y in range(h)]
        ls_aux.sort()
        for y in range(h):
            new_mat[x, y] = ls_aux[y]
    return new_img


# img = Image.open("./guess.bmp").convert('L')
# what(img).show()

# b
def process_img(img, op):
    w, h = img.size
    mat = img.load()
    new_img = img.copy()
    new_mat = new_img.load()

    for x in range(w):
        for y in range(h):
            new_mat[x, y] = op(mat, x, y)
            #mat[x, y] = op(mat, x, y)

    return new_img
    #return img


img = Image.open("./my_picture.jpg").convert('L')
h = img.size[1]
upside_down = process_img(img, lambda mat, x, y: mat[x, h - y - 1])
upside_down.save("./my_picture1.jpg", 'bmp')
