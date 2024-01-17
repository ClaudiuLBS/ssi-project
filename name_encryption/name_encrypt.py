import os
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


def encrypt_file_ecb(input_content: bytes, output_file_path: str):
  key = get_random_bytes(16)
  cipher = AES.new(key, AES.MODE_ECB)

  padded_content = pad(input_content, AES.block_size)
  ciphertext = cipher.encrypt(padded_content)

  with open(output_file_path, 'wb') as file:
    file.write(ciphertext)


letters_folder = 'name_letters'
hashed_headers_file_name = 'hashvalues.txt'
all_hashed_headers = ''

for file_name in os.listdir(letters_folder):
  file_path: str = os.path.join(letters_folder, file_name)
  with open(file_path, 'rb') as file_object:
    file_header_components: list[str] = [file_object.readline().strip().decode() for _ in range(4)]
    file_header: str = ' '.join(file_header_components)
    hashed_header: str = sha256(file_header.encode()).hexdigest()
    all_hashed_headers += hashed_header + '\n'
    file_content: bytes = file_object.read()

    encrypted_file_folder = 'encrypted_files'
    encrypted_file_path = os.path.join(encrypted_file_folder, file_name)
    encrypt_file_ecb(file_content, encrypted_file_path)


with open(hashed_headers_file_name, 'w') as output_headers_object:
  output_headers_object.write(all_hashed_headers)


