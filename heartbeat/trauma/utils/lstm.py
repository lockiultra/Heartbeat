import torch
from trauma.trauma_models.lstm import LSTM
from trauma.preprocessing.lstm_preprocess import LSTMPreprocess

def get_predict(prompt):
    model = LSTM(100, 100, 2)
    model.load_state_dict(torch.load('trauma/trauma_models/lstm.model'))
    preprocessor = LSTMPreprocess()
    x = torch.FloatTensor(preprocessor.transform(prompt)).view(1, 100)
    return model(x).argmax(dim=1)




