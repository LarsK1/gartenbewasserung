import numpy
from tensorflow.keras.models import load_model

# Load the model from the HDF5 file
loaded_model = load_model('my_model.h5')
loaded_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Use the model to make predictions on new data
predictions = loaded_model.predict(numpy.array([numpy.asarray([96, 20, 15.4, 21])]))
predictions = (predictions > 0.5).astype(bool)
print(predictions)
