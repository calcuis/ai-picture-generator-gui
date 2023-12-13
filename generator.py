import tensorflow as tf
import matplotlib.pyplot as plt
import random
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("CryptoPunk Generator")
root.columnconfigure([0, 1, 2, 3], minsize=200)

img = ImageTk.PhotoImage(Image.open("output.png"))
panel = Label(root, image=img)
panel.grid(row=1, columnspan=4, sticky="nsew")

def update_img():
    img = ImageTk.PhotoImage(Image.open("output.png"))
    panel.configure(image=img)
    panel.image = img

def generate(number):
    generator = tf.keras.models.load_model("./models/")
    n_images = number*number
    seed = random.getrandbits(32)
    code_size = 100

    noise = tf.random.normal(shape=[n_images, code_size], seed=seed)
    generated_images = generator(noise, training=False)

    fig = plt.figure(figsize=(8, 8))
    for i in range(generated_images.shape[0]):
        plt.subplot(number, number, i+1)
        plt.imshow(generated_images[i, :, :, :])
        plt.axis('off')
    plt.savefig("output.png")

    update_img()

btn_1 = Button(text = "Generate 1 cryptopunk", command=lambda:generate(1))
btn_3 = Button(text = "Generate 3x3 cryptopunks", command=lambda:generate(3))
btn_5 = Button(text = "Generate 5x5 cryptopunks", command=lambda:generate(5))
btn_q = Button(text = "Terminate", command=root.quit)

btn_1.grid(row=0, column=0, sticky="nsew")
btn_3.grid(row=0, column=1, sticky="nsew")
btn_5.grid(row=0, column=2, sticky="nsew")
btn_q.grid(row=0, column=3, sticky="nsew")

root.mainloop()
