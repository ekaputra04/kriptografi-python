#!/usr/bin/env python
# ----------------- Header Files ---------------------#

import sys
import random
import argparse
import logging
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
from PIL import Image
import numpy as np
from Crypto.Cipher import AES
import hashlib
import binascii

global password

def load_image(name):
    return Image.open(name)

# ----------------- Functions for encryption ---------------------#
def prepare_message_image(image, size):
    if size != image.size:
        image = image.resize(size, Image.ANTIALIAS)
    return image

def generate_secret(size, secret_image=None):
    width, height = size
    new_secret_image = Image.new(mode="RGB", size=(width * 2, height * 2))

    for x in range(0, 2 * width, 2):
        for y in range(0, 2 * height, 2):
            color1 = np.random.randint(255)
            color2 = np.random.randint(255)
            color3 = np.random.randint(255)
            new_secret_image.putpixel((x, y), (color1, color2, color3))
            new_secret_image.putpixel((x + 1, y), (255 - color1, 255 - color2, 255 - color3))
            new_secret_image.putpixel((x, y + 1), (255 - color1, 255 - color2, 255 - color3))
            new_secret_image.putpixel((x + 1, y + 1), (color1, color2, color3))

    return new_secret_image

def generate_ciphered_image(secret_image, prepared_image):
    width, height = prepared_image.size
    ciphered_image = Image.new(mode="RGB", size=(width * 2, height * 2))
    for x in range(0, width * 2, 2):
        for y in range(0, height * 2, 2):
            sec = secret_image.getpixel((x, y))
            msssg = prepared_image.getpixel((int(x / 2), int(y / 2)))
            color1 = (msssg[0] + sec[0]) % 256
            color2 = (msssg[1] + sec[1]) % 256
            color3 = (msssg[2] + sec[2]) % 256
            ciphered_image.putpixel((x, y), (color1, color2, color3))
            ciphered_image.putpixel((x + 1, y), (255 - color1, 255 - color2, 255 - color3))
            ciphered_image.putpixel((x, y + 1), (255 - color1, 255 - color2, 255 - color3))
            ciphered_image.putpixel((x + 1, y + 1), (color1, color2, color3))

    return ciphered_image

def generate_image_back(secret_image, ciphered_image):
    width, height = secret_image.size
    new_image = Image.new(mode="RGB", size=(int(width / 2), int(height / 2)))
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            sec = secret_image.getpixel((x, y))
            cip = ciphered_image.getpixel((x, y))
            color1 = (cip[0] - sec[0]) % 256
            color2 = (cip[1] - sec[1]) % 256
            color3 = (cip[2] - sec[2]) % 256
            new_image.putpixel((int(x / 2), int(y / 2)), (color1, color2, color3))

    return new_image

#------------------------Encryption -------------------#
def level_one_encrypt(Imagename):
    message_image = load_image(Imagename)
    size = message_image.size
    width, height = size

    secret_image = generate_secret(size)
    secret_image.save("./images/secret.jpeg")

    prepared_image = prepare_message_image(message_image, size)
    ciphered_image = generate_ciphered_image(secret_image, prepared_image)
    ciphered_image.save("./result/share_encrypt.jpeg")

# -------------------- Construct Encrypted Image  ----------------#
def construct_enc_image(ciphertext, relength, width, height):
    asciicipher = binascii.hexlify(ciphertext).decode('utf-8')
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    # use replace function to replace ascii cipher characters with numbers
    reps = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6'}
    asciiciphertxt = replace_all(asciicipher, reps)

    # construct encrypted image
    step = 3
    encimageone = [asciiciphertxt[i:i + step] for i in range(0, len(asciiciphertxt), step)]
    # if the last pixel RGB value is less than 3-digits, add a digit a 1
    if int(encimageone[len(encimageone) - 1]) < 100:
        encimageone[len(encimageone) - 1] += "1"
    # check to see if we can divide the string into partitions of 3 digits.  if not, fill in with some garbage RGB values
    if len(encimageone) % 3 != 0:
        while (len(encimageone) % 3 != 0):
            encimageone.append("101")

    encimagetwo = [(int(encimageone[int(i)]), int(encimageone[int(i + 1)]), int(encimageone[int(i + 2)])) for i in range(0, len(encimageone), step)]
    print(len(encimagetwo))
    while (int(relength) != len(encimagetwo)):
        encimagetwo.pop()

    encim = Image.new("RGB", (int(width), int(height)))
    encim.putdata(encimagetwo)
    encim.save("./result/visual_encrypt.jpeg")

#------------------------- Visual-encryption -------------------------#
def encrypt(imagename, password):
    plaintext = list()
    plaintextstr = ""

    im = Image.open(imagename)
    pix = im.load()

    width = im.size[0]
    height = im.size[1]

    # Break up the image into a list, each with pixel values and then append to a string
    for y in range(height):
        for x in range(width):
            plaintext.append(pix[x, y])

    # Add 100 to each tuple value to make sure each are 3 digits long.
    for pixel in plaintext:
        for value in pixel:
            aa = int(value) + 100
            plaintextstr += str(aa)

    # Length save for encrypted image reconstruction
    relength = len(plaintext)

    # Append dimensions of image for reconstruction after decryption
    plaintextstr += f"h{height}h" + f"w{width}w"

    # Make sure that plaintextstr length is a multiple of 16 for AES. If not, append "n".
    while len(plaintextstr) % 16 != 0:
        plaintextstr += "n"

    # Encrypt plaintext
    obj = AES.new(password, AES.MODE_CBC, b'This is an IV456')
    ciphertext = obj.encrypt(plaintextstr.encode('utf-8'))

    # Create the ./crypt/ directory if it doesn't exist
    if not os.path.exists('./crypt/'):
        os.makedirs('./crypt/')

    # Write ciphertext to file in ./crypt/ directory
    cipher_name = os.path.join('./crypt/', os.path.basename(imagename) + ".crypt")
    with open(cipher_name, 'wb') as g:
        g.write(ciphertext)

    construct_enc_image(ciphertext, relength, width, height)
    print("Visual Encryption done.......")
    level_one_encrypt("./result/visual_encrypt.jpeg")
    print("2-Share Encryption done.......")

# ---------------------- decryption ---------------------- #
def decrypt(ciphername, password):
    secret_image = Image.open("./images/secret.jpeg")
    ima = Image.open("./result/share_encrypt.jpeg")
    new_image = generate_image_back(secret_image, ima)
    new_image.save("./result/share_decrypt.jpeg")
    print("2-share Decryption done....")
    with open(ciphername, 'rb') as cipher:
        ciphertext = cipher.read()

    # decrypt ciphertext with password
    obj2 = AES.new(password, AES.MODE_CBC, b'This is an IV456')
    decrypted = obj2.decrypt(ciphertext).decode('utf-8')

    # parse the decrypted text back into integer string
    decrypted = decrypted.replace("n", "")

    # extract dimensions of images
    newwidth = decrypted.split("w")[1]
    newheight = decrypted.split("h")[1]

    # replace height and width with emptyspace in decrypted plaintext
    heightr = "h" + str(newheight) + "h"
    widthr = "w" + str(newwidth) + "w"
    decrypted = decrypted.replace(heightr, "")
    decrypted = decrypted.replace(widthr, "")

    # reconstruct the list of RGB tuples from the decrypted plaintext
    step = 3
    finaltextone = [decrypted[i:i + step] for i in range(0, len(decrypted), step)]
    finaltexttwo = [(int(finaltextone[int(i)]) - 100, int(finaltextone[int(i + 1)]) - 100, int(finaltextone[int(i + 2)]) - 100) for i in range(0, len(finaltextone), step)]

    # reconstruct image from list of pixel RGB tuples
    newim = Image.new("RGB", (int(newwidth), int(newheight)))
    newim.putdata(finaltexttwo)
    newim.save("./result/visual_decrypt.jpeg")
    print("Visual Decryption done......")

# ---------------------
# GUI stuff starts here
# ---------------------

def pass_alert():
    messagebox.showinfo("Password Alert", "Please enter a password.")

def enc_success(imagename):
    messagebox.showinfo("Success", "Encrypted Image: " + imagename)

# image encrypt button event
def image_open():
    global password

    enc_pass = passg.get()
    if enc_pass == "":
        pass_alert()
    else:
        password = hashlib.sha256(enc_pass.encode()).digest()
        filename = filedialog.askopenfilename()
        if filename:
            encrypt(filename, password)

# image decrypt button event
def cipher_open():
    global password

    dec_pass = passg.get()
    if dec_pass == "":
        pass_alert()
    else:
        password = hashlib.sha256(dec_pass.encode()).digest()
        filename = filedialog.askopenfilename()
        if filename:
            decrypt(filename, password)

class App:
    def __init__(self, master):
        global passg
        title = "Image Cryptography with AES Algorithm"
        author = "Made by Group 1"
        
        # Configure title message
        msgtitle = Message(master, text=title, width=300)
        msgtitle.config(font=('helvetica', 12, 'bold'))
        msgtitle.pack(anchor=CENTER)

        # Configure author message
        msgauthor = Message(master, text=author, width=200)
        msgauthor.config(font=('helvetica', 10))
        msgauthor.pack(anchor=CENTER)

        # Configure canvas
        canvas_width = 300
        canvas_height = 100
        w = Canvas(master, width=canvas_width, height=canvas_height)
        w.pack()

        # Configure password label and entry
        passlabel = Label(master, text="Enter Encrypt/Decrypt Password:")
        passlabel.pack()
        passg = Entry(master, show="*", width=50)
        passg.pack()

        # Configure buttons
        self.encrypt = Button(master, text="Encrypt", fg="black", command=image_open, width=25, height=5)
        self.encrypt.pack(side=LEFT, padx=5, pady=5)
        
        self.decrypt = Button(master, text="Decrypt", fg="black", command=cipher_open, width=25, height=5)
        self.decrypt.pack(side=RIGHT, padx=5, pady=5)

# Main application
root = Tk()
root.wm_title("Image Encryption")
app = App(root)
root.mainloop()
