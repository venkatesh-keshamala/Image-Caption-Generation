import os
import keras
from keras.preprocessing.text import tokenizer_from_json
import numpy as np
import matplotlib.pyplot as plt
from .build import feature_extractions, sample_caption, single_image_extractions
import json
from django.conf import settings
from pickle import load, dump

# Load tokenizer
with open(os.path.join(settings.MEDIA_ROOT, "models",'tokenizer.json'), 'r') as f:
    tokenizer_json = json.load(f)
tokenizer = tokenizer_from_json(tokenizer_json)

model = keras.models.load_model(os.path.join(settings.MEDIA_ROOT, "models","sample_model.h5"))  # Load model
vocab_size = tokenizer.num_words  # The number of vocabulary
max_length = 37  # Maximum length of caption sequence
def start_process(imagepath):
    print("Image Path")
    imagepath= os.path.join(settings.MEDIA_ROOT,imagepath)
    features = single_image_extractions(imagepath)
    caption = sample_caption(model, tokenizer, max_length, vocab_size, features)
    print("Caption is", caption)
    return caption