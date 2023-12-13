## cryptopunk generator GUI version

The provided Python code is a simple graphical user interface (GUI) application using the Tkinter library for generating and displaying CryptoPunk images. CryptoPunks are unique 24x24 pixel art characters (selected as an example of this demonstration). The application uses a pre-trained TensorFlow model to generate these images based on random input noise.
Here's a breakdown of the code:

Import Libraries:
- `tensorflow` for machine learning functionalities.
- `matplotlib.pyplot` for plotting generated images.
- `random` for generating random numbers.
- `tkinter` for creating the GUI.
- `PIL` (Python Imaging Library) for working with images.

GUI Setup:
- It creates a `Tkinter` window titled "CryptoPunk Generator" with a specific column configuration.
- It loads an initial image ("output.png") and displays it in the `Tkinter` window using the Label widget.

Image Update Function:
- `update_img` function reloads the image from the file ("output.png") and updates the displayed image in the `Tkinter` window.

Image Generation Function:
- `generate` function takes a parameter number representing the number of CryptoPunk images to generate.
- It loads a pre-trained `TensorFlow` model from the "./models/" directory.
- Generates random noise based on the specified number and a seed.
- Uses the generator model to generate a batch of images.
- Plots the generated images in a grid using Matplotlib and saves the composite image as "output.png."
- Calls `update_img` to update the displayed image in the `Tkinter` window.

Four buttons are created for different generation options:
- "Generate 1 cryptopunk" button calls `generate(1)`
- "Generate 3x3 cryptopunks" button calls `generate(3)`
- "Generate 5x5 cryptopunks" button calls `generate(5)`
- "Terminate" button quits the `Tkinter` application.
- Buttons are arranged in a grid layout within the `Tkinter` window.

Overall, this code provides a simple interface for generating CryptoPunk images with different options for the number of images to generate. The generated images are displayed in the Tkinter window using Matplotlib.

[<img src="https://raw.githubusercontent.com/calcuis/ai-picture-generator-gui/master/output.png" width="400" height="400">](https://github.com/calcuis/ai-picture-generator-gui/blob/main/output.png)

Run it with
```
python generator.py
```

**References**

huggingface.co/huggan/crypto-gan

github.com/dimitreOliveira/cryptogans

github.com/teddykoker/cryptopunks-gan

tensorflow.org/tutorials/generative/dcgan
