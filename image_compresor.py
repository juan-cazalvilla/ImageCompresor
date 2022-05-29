from PIL import Image, ImageFile
import glob
import os
import datetime
import zlib
import zipfile

image_quality = 50

# Extension allowed
extensions = ['.jpeg', '.png', '.jpg', '.JPG']

images = glob.glob('*.*')
compressed_folder = 'compressed'


if not os.path.exists(compressed_folder):
    os.mkdir(compressed_folder)


for image in images:
    filename, file_extension = os.path.splitext(image)
    
    # Avoid undesired files
    if file_extension not in extensions:
        print ('Ignoring file ' +  filename + file_extension + ' unsupported file')
        continue
    
    # Open pics and compress in a compress folder 
    img = Image.open(image)
    ImageFile.MAXBLOCK = img.size[0] * img.size[1]
    img.save( os.path.join(compressed_folder, image) , quality = image_quality, optimize = True)


    # Make a zip file with the original pictures
    compression = zipfile.ZIP_DEFLATED
    zip_name = (datetime.date.today()).strftime('%m-%d-%Y')
    zf = zipfile.ZipFile(zip_name + '.zip', mode = "w")
    
    try:
        for image in images:
        
        # Avoid undesired files
         filename, file_extension = os.path.splitext(image)
         if file_extension not in extensions:
            continue
         zf.write(image, compress_type= compression)

    except FileNotFoundError:
        print("Error compressing")

    finally:
        zf.close() 