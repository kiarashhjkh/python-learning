from PIL import Image

img = Image.open("/home/kiarash/Downloads/cat_pic.jpg")

secret_message = "09121940843"

k = 0

for i in range(0, img.size[0], 10):
    for j in range(0, img.size[1], 10):
        if k >= len(secret_message):
            break
        img.putpixel((j, i), (ord(secret_message[k]), ord(secret_message[k]), ord(secret_message[k])))
        k += 1
    if k >= len(secret_message):
        break

img.show()
