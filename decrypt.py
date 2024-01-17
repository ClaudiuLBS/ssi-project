import os
from hashlib import sha256
import matplotlib.pyplot as plt
from PIL import Image


def almost_equal(x: int,  y: int, tolerance: int = 100):
  return abs(x - y) < tolerance


def get_header_specified_size(header: str):
  header_components = header.split(' ')
  width = int(header_components[1])
  height = int(header_components[2])
  return 3 * width * height 


def get_decrypted_headers(input_path: str = 'hashvalues.txt') -> list[str]:
  hashed_headers = open(input_path, 'r').read()

  headers: list[str] = []
  for i in range(1024):
    for j in range(1024):
      header = f'P6 {i} {j} 255'
      hashed_header = sha256(header.encode()).hexdigest()

      if hashed_header in hashed_headers:
        headers.append(header)

  return headers


def get_header_by_size(size: int, headers: list[str]):
  return list(filter(lambda x: almost_equal(get_header_specified_size(x), size), headers))[0]


def associate_images_with_headers(encrypted_files_folder: str = 'encrypted_files', result_files_folder: str = 'result_files'):
  headers: list[str] = get_decrypted_headers()

  for file_name in os.listdir(encrypted_files_folder):
    file_path: str = os.path.join(encrypted_files_folder, file_name)
    file_size: int = os.path.getsize(file_path)
    file_header: str = get_header_by_size(file_size, headers)
    file_content: bytes = open(file_path, 'rb').read()

    result_file_content = file_header.encode() + b' ' + file_content
    result_file_path = os.path.join(result_files_folder, file_name)
    with open(result_file_path, 'wb') as output_file:
      output_file.write(result_file_content)


def show_img(id: int):
  file_path = os.path.join('result_files', f'File{id}_encr.ppm')
  
  encrypted_image = Image.open(file_path)
  plt.imshow(encrypted_image)
  plt.show()


show_img(8)
# <3 i love you