import os
import av
from PIL import Image

def convert_avif_to_jpg(folder_path, output_extension = 'jpg'):
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.avif'):
            avif_path = os.path.join(folder_path, filename)
            jpg_path = f'{os.path.splitext(avif_path)[0]}.{output_extension}'

            container = av.open(avif_path)
            for frame in container.decode(video=0):
                img = Image.fromarray(frame.to_rgb().to_ndarray())
                img.save(jpg_path, 'JPEG')
                print(f"Converted '{avif_path}' to '{jpg_path}'")
            container.close()

folder_path = input(">> Please enter the folder path containing AVIF images: ")
output_extension = ''

print('\nAVAILABLE EXTENSIONS: [jpeg, jpg, png]\n')

while output_extension not in ['jpeg', 'jpg', 'png']:
    output_extension = input('>> What is the image extension you want: ').strip().lower()



convert_avif_to_jpg(folder_path, output_extension)
