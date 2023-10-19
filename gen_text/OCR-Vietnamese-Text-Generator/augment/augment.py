import cv2
import albumentations as A
import numpy as np
import math
import os
import random
from tqdm import tqdm
import concurrent.futures

def save_dict2txt(results_dict, out_path):
    with open(out_path, "a", encoding="utf-8") as outfile:  # Use "a" mode for appending
        for key, value in results_dict.items():
            line = f"{key}\t{value}"
            outfile.write(line)
    print("=======================================append dict done=====================================================")
    return "append dict done"

def pad_image(image, padding_width_percent, padding_height_percent, padding_color=(0, 0, 0)):
    """
    Pad an image with a specified percentage of padding width and height.

    Parameters:
    - image: The input image as a NumPy array.
    - padding_width_percent: The percentage of padding width (0 to 100).
    - padding_height_percent: The percentage of padding height (0 to 100).
    - padding_color: The color of the padding in BGR format (default is black).

    Returns:
    - padded_image: The image with padding and the original image randomly positioned.
    """
    if padding_width_percent < 0 or padding_height_percent < 0:
        raise ValueError("Padding percentages should be non-negative.")

    height, width, channels = image.shape

    # Calculate the amount of padding in pixels based on the percentages
    pad_width = int(padding_width_percent / 100 * width)
    pad_height = int(padding_height_percent / 100 * height)

    # Create an image with the desired padding color
    padded_image = np.full((height + 2 * pad_height, width + 2 * pad_width, channels), padding_color, dtype=np.uint8)

    # Generate random positions for the top-left corner of the original image within the padded canvas
    rand_x = random.randint(0, 2 * pad_width)
    rand_y = random.randint(0, 2 * pad_height)

    # Calculate the coordinates for pasting the original image
    paste_x1 = max(0, rand_x)
    paste_x2 = min(rand_x + width, padded_image.shape[1])
    paste_y1 = max(0, rand_y)
    paste_y2 = min(rand_y + height, padded_image.shape[0])

    # Calculate the coordinates for copying a portion of the original image
    copy_x1 = max(0, -rand_x)
    copy_x2 = min(width, padded_image.shape[1] - rand_x)
    copy_y1 = max(0, -rand_y)
    copy_y2 = min(height, padded_image.shape[0] - rand_y)

    # Paste the original image into the padded canvas at the random position
    padded_image[paste_y1:paste_y2, paste_x1:paste_x2] = image[copy_y1:copy_y2, copy_x1:copy_x2]

    return padded_image


def augmentation(image):
    pixel_color = image[3, 3]
    try:
        if (int(pixel_color[0]) + int(pixel_color[1]) + int(pixel_color[2]))/3 < 100:
            pixel_color = (128,128,128)
    except:
        pixel_color = (128,128,128)

    # image = pad_image(image, 5, 10, padding_color=pixel_color)

        # cv2.imwrite("check.jpg", image)
    image = cv2.resize(image, (int(image.shape[1] * 64 / image.shape[0]), 64 ))    # 48



    transform = A.Compose([
    A.Blur(p = 0.1),
    A.MotionBlur(p = 0.1),
    # A.ElasticTransform(alpha=1, alpha_affine = 3, p =0.2),
    A.GaussNoise(p = 0.1),
    A.GridDistortion( num_steps=5, distort_limit=0.1, p = 0.2),
    A.CLAHE(p = 0.2),
    A.RandomBrightnessContrast(p=0.7),
    A.ISONoise(p = 0.3),
    A.RGBShift(p = 0.5),
    # A.ShiftScaleRotate(shift_limit=0.02, scale_limit=0.05, rotate_limit=7, p=0.2),
    # A.ElasticTransform(alpha_affine=0.5, alpha=0.5, sigma=0, p = 0.1),
    # A.Perspective(p = 0.2),
    A.ToGray(p = 0.25),
    ])
        
    image_aug_list = []
    for _ in range(1):
        transformed = transform(image=image)
        transformed_image = transformed['image']

        # aug_1 = random.uniform(0,1)
        # if aug_1 > 0.5:
        # # preprocess image line text
        #     transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2GRAY)

        image_aug_list.append(transformed_image)
    return image_aug_list


def process_line(line):
    label_text = line.split('\t')[1]
    name_file_img = line.split('\t')[0]
    img_path_input = os.path.join(root, name_file_img)
    img = cv2.imread(img_path_input)
    

    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)


    # kernel = np.ones((2,2), np.uint8)  # Define kernel for erosion and dilation, adjust size as needed
    # img = cv2.dilate(img, kernel, iterations=1)  # Erosion
    # img = cv2.erode(img, kernel, iterations=random.randint(3, 5))  # Erosion

    # image = np.expand_dims(img , axis = 2)
    # image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    image_aug_list = augmentation(img)
    result_image_dict = {}

    for image_aug in image_aug_list:
        name_save = name_file_img.split('/')[-1]
        result_image_dict[os.path.join("data_ocr_v1_0210_aug", name_save)] = label_text
        cv2.imwrite(os.path.join(folder_output, name_save), image_aug)

    return result_image_dict

# Your input and output paths and other variables
root = "/home/sonlt373/Desktop/SoNg/OCR_handwriting_shop_sticker/data/data_sticker_handwriting/KALAPA_ByteBattles_2023_OCR_Set1/OCR/training_HWT_v1_171023/"
input_path = "/home/sonlt373/Desktop/SoNg/OCR_handwriting_shop_sticker/data/data_sticker_handwriting/KALAPA_ByteBattles_2023_OCR_Set1/OCR/training_HWT_v1_171023/data_hwt_500k_syn.txt"
folder_output = "/home/sonlt373/Desktop/SoNg/OCR_handwriting_shop_sticker/data/data_sticker_handwriting/KALAPA_ByteBattles_2023_OCR_Set1/OCR/training_HWT_v1_171023/data_500k_hwt_synthetic_augment"

result_image_list = {}

# Use a ThreadPoolExecutor to parallelize the processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        results = list(tqdm(executor.map(process_line, lines[:-1]), total=len(lines[:-1])))

    # Combine results from all threads into a single dictionary
    # for result in results:
    #     result_image_list.update(result)

# Save the combined dictionary to a file
# save_dict2txt(result_image_list, "label_0210_aug.txt")