
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_CACHE = os.path.join(BASE_DIR, "modelos")

os.environ["HF_HUB_CACHE"] = PATH_CACHE

from transformers import pipeline

NOMBRE_MODELO = "distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline("sentiment-analysis",
                      model=NOMBRE_MODELO)
                      #cache_dir = PATH_MODELO)

phrase = input("Write any phrase (Positive or Negative): ")
print(classifier(phrase))
#print(PATH_MODELO)

