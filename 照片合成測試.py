
import PIL.Image as Image
import os
 
IMAGES_PATH = 'C://Users/User/Desktop/1081220_Focus_20X_S1_1_RawData/'  
IMAGES_FORMAT = ['.jpg', '.JPG', 'png']  
IMAGE_WIDTH = 800  
IMAGE_HEIGHT = 800 
IMAGE_ROW = 65 
IMAGE_COLUMN = 62 
IMAGE_SAVE_PATH = 'C://Users/User/Desktop/1081220_Focus_20X_S1_1_RawData/final.jpg'  
 
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
               os.path.splitext(name)[1] == item]

print(len(image_names))
 
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    raise ValueError("合成圖片的數量及大小不符合設定！")
 
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_WIDTH, IMAGE_ROW * IMAGE_HEIGHT)) 
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_WIDTH, IMAGE_HEIGHT),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_WIDTH, (y - 1) * IMAGE_HEIGHT))
    return to_image.save(IMAGE_SAVE_PATH) 
image_compose() 
