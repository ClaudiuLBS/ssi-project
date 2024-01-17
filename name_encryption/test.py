import os
import matplotlib.pyplot as plt
from PIL import Image
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

  


# def encrypt_file_ecb(input_content: bytes, output_file_path: str):
#   key = get_random_bytes(16)
#   cipher = AES.new(key, AES.MODE_ECB)

#   padded_content = pad(input_content, AES.block_size)
#   ciphertext = cipher.encrypt(padded_content)

#   header = 'P6\n902 865\n255\n'.encode()
#   ciphertext = header + ciphertext

#   with open(output_file_path, 'wb') as file:
#     file.write(ciphertext)

# with open('l.ppm', 'rb') as f:
#   content: bytes = f.read()
#   encrypt_file_ecb(content, 'l2.ppm')

  
encrypted_image = Image.open('./encrypted_files_with_header/U.ppm')
plt.imshow(encrypted_image)
plt.show()