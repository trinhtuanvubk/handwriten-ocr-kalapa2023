import cv2
import math
import os
import random as rnd
import numpy as np

from PIL import Image, ImageDraw, ImageFilter



def image(height: int, width: int, image_dir: str) -> Image:
    """
    Create a background with a image
    """
    images = os.listdir(image_dir)

    # For Kalapa2023
    # if width / height < 15:
    #     width = int(height*15)

    if len(images) > 0:
        pic = Image.open(
            os.path.join(image_dir, images[rnd.randint(0, len(images) - 1)])
        )

        if pic.size[0] < width:
            pic = pic.resize(
                [width, int(pic.size[1] * (width / pic.size[0]))],
                Image.Resampling.LANCZOS,
            )
        if pic.size[1] < height:
            pic = pic.resize(
                [int(pic.size[0] * (height / pic.size[1])), height],
                Image.Resampling.LANCZOS,
            )

        if pic.size[0] == width:
            x = 0
        else:
            x = rnd.randint(0, pic.size[0] - width)
        if pic.size[1] == height:
            y = 0
        else:
            y = rnd.randint(0, pic.size[1] - height)

        return pic.crop((x, y, x + width, y + height))
    else:
        raise Exception("No images where found in the images folder!")


if __name__=="__main__":
    image_dir = "./images"
    h = 48
    w = 720
    
    for i in range(300):
        outpath = os.path.join("./out/images_hw_background_eval", f"{i}.jpg")
        textpath = os.path.join("./out/labels_hw_background_eval", f"{i}.txt")
        
        with open(textpath, 'w') as f:
            f.write("" + "\n")
            f.close()
        a = image(h, w, image_dir)
        rgb_im = a.convert('RGB')
        rgb_im.save(outpath)
    print(a)