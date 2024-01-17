import os
import matplotlib.pyplot as plt
from PIL import Image

  
encrypted_image = Image.open('./encrypted_files/B.ppm')
plt.imshow(encrypted_image)
plt.show()