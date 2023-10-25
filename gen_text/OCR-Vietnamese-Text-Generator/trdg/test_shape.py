import cv2

path = "/home/ai22/Documents/VUTT/kalapa/handwriten-ocr-kalapa2023/gen_text/OCR-Vietnamese-Text-Generator/trdg/out/images_hw_test/72.jpg"
im = cv2.imread(path)
print(im.shape)