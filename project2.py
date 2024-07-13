from PIL import Image
import numpy as np
import os

def encrypt_image(input_image_path, output_image_path, key):
    # Open the input image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key to each pixel value (mod 256)
    encrypted_array = (image_array + key) % 256

    # Create a new image from the encrypted array
    encrypted_image = Image.fromarray(np.uint8(encrypted_array))
    
    # Ensure the output path includes a file name and extension
    if not output_image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        output_image_path = os.path.join(output_image_path, 'encrypted_image.png')
    
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    image = Image.open(input_image_path)
    image_array = np.array(image)

    # Decrypt the image by subtracting the key from each pixel value (mod 256)
    decrypted_array = (image_array - key) % 256

    # Create a new image from the decrypted array
    decrypted_image = Image.fromarray(np.uint8(decrypted_array))
    
    # Ensure the output path includes a file name and extension
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
