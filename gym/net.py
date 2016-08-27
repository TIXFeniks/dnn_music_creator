# build the model: a single LSTM
from text_model import *
print('Build model...')
model = Sequential()
model.add(LSTM(512, input_shape=(maxlen, len(chars)), return_sequences=True))
model.add(LSTM(512 ))
model.add(Dense(len(chars)))
print (len(chars))
model.add(Activation('softmax'))


optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

model.save('model_dump.h5py')