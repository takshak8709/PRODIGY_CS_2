# PRODIGY_WD_2
Here's a README file for your image encryption tool project:

---

# Image Encryption Tool

This project is a simple image encryption tool that allows users to encrypt and decrypt images using pixel manipulation techniques. The encryption process involves applying a basic mathematical operation to each pixel in the image. The tool supports both encryption and decryption of images using a user-defined key.

## Features

- *Encrypt Images:* Apply a basic mathematical operation (addition) to each pixel value to encrypt the image.
- *Decrypt Images:* Reverse the encryption by applying the inverse operation (subtraction) using the same key.
- *Support for Various Image Formats:* The tool supports common image formats such as PNG, JPG, BMP, and GIF.

## Prerequisites

- Python 3.x
- Required Python libraries: Pillow, NumPy

You can install the required libraries using pip:

bash
pip install pillow numpy


## Usage

1. *Clone or Download the Repository:*

   bash
   git clone https://github.com/yourusername/image-encryption-tool.git
   cd image-encryption-tool
   

2. *Run the Tool:*

   Execute the script in your terminal:

   bash
   python image_encryption_tool.py
   

3. *Follow the On-Screen Instructions:*

   - Choose whether to encrypt or decrypt an image.
   - Provide the path to the input image file.
   - Specify the path where the output image should be saved.
   - Enter the encryption/decryption key (an integer).

### Example

- *Encryption Example:*

   You have an image input.png and want to encrypt it using a key of 123. The encrypted image will be saved as encrypted_image.png:

   bash
   python image_encryption_tool.py
   # Enter E for encryption
   # Enter "input.png" for input image path
   # Enter "encrypted_image.png" for output image path
   # Enter 123 for the encryption key
   

- *Decryption Example:*

   You want to decrypt the previously encrypted image using the same key:

   bash
   python image_encryption_tool.py
   # Enter D for decryption
   # Enter "encrypted_image.png" for input image path
   # Enter "decrypted_image.png" for output image path
   # Enter 123 for the decryption key
   

## Code Overview

python
from PIL import Image
import numpy as np
import os

def encrypt_image(input_image_path, output_image_path, key):
    # Open the input image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key to each pixel value (mod 256)
    encrypted_array = (image_array + key) % 256
    encrypted_array = np.uint8(encrypted_array)

    encrypted_image = Image.fromarray(encrypted_array, image.mode)
    if not output_image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        output_image_path = os.path.join(output_image_path, 'encrypted_image.png')
    
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    image_array = np.array(image)

    decrypted_array = (image_array - key) % 256
    decrypted_array = np.uint8(decrypted_array)

    decrypted_image = Image.fromarray(decrypted_array, image.mode)
    if not output_image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        output_image_path = os.path.join(output_image_path, 'decrypted_image.png')
    
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

def main():
    print("Image Encryption Tool")
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").upper()
        if choice not in ('E', 'D'):
            print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")
            continue
        
        input_image_path = input("Enter the path to the input image: ").strip('"')
        output_image_path = input("Enter the path to save the output image: ").strip('"')
        key = int(input("Enter the encryption/decryption key (an integer): "))

        if choice == 'E':
            encrypt_image(input_image_path, output_image_path, key)
        elif choice == 'D':
            decrypt_image(input_image_path, output_image_path, key)
        break

if __name__ == "__main__":
    main()


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can customize the README as needed, especially the links and paths to fit your project's structure.
