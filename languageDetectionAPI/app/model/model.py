import pickle
from pathlib import Path

# Get the base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent
print(BASE_DIR)

__version__ = '0.1'

# Load the Vectorizer
with open(f"{BASE_DIR}/vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)


# Load the Label Encoder
with open(f"{BASE_DIR}/encoder.pkl", "rb") as f:
    le_obj = pickle.load(f)


# Load the model
with open(f"{BASE_DIR}/language_detection.pkl", "rb") as f:
    model = pickle.load(f)


classes = [
    "English",
    "French",
    "Spanish",
    "Portugeese",
    "Italian",
    "Russian",
    "Sweedish",
    "Malayalam"
    "Dutch"
    "Arabic",
    "Turkish",
    "German"   
    "Tamil",
    "Danish",
    "Kannada",
    "Greek",
    "Hindi"
]


def lang_predict(text):
    # text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    # text = re.sub(r"[[]]", " ", text)
    # text = text.lower()

    # converting text to bag of words model (Vector)
    x = cv.transform([text]).toarray()

    # predicting the language
    lang = model.predict(x)

    # finding the language corresponding the predicted value
    lang = le_obj.inverse_transform(lang)

    # printing the language
    print(lang)
    print("The langauge is in", lang[0])

    return lang[0]