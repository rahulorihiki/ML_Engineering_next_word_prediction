import numpy as np
import tensorflow as tf
import pickle

class NextWordPredictor:
    def __init__(self, model_path: str, tokenizer_path: str):
        self.model = tf.keras.models.load_model(model_path)
        with open(tokenizer_path, 'rb') as file:
            self.tokenizer = pickle.load(file)

    def predict(self, text: str, max_len: int = 10):
        token_list = self.tokenizer.texts_to_sequences([text])[0]
        token_list = np.array(token_list).reshape(1, -1)
        token_list = tf.keras.preprocessing.sequence.pad_sequences(token_list, maxlen=max_len, padding='pre')
        predicted = np.argmax(self.model.predict(token_list), axis=-1)
        return self.tokenizer.index_word.get(predicted[0], "")

if __name__ == "__main__":
    predictor = NextWordPredictor("model/next_word_model.h5", "model/tokenizer.pkl")
    print(predictor.predict("The quick brown"))
