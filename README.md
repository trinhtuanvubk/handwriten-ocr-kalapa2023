# handwriten-ocr-kalapa2023

### Environment

- To create `venv`:
```
virualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Augment Data

- For data train (from dataset kalapa)
```
cd ./gen_text/OCR-Vietnamese-Text-Generator/augment
python augment_training.py --root # path image (include ./images and ./labels)
# Default augment X 10 
```
- For data synthetic (from dataset gen)
```
cd ./gen_text/OCR-Vietnamese-Text-Generator/augment
python augment_training.py --root # path image (include ./images and ./labels)
# Default augmant X 1
```