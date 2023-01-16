import numpy
import tensorflow as tf
from sklearn.model_selection import train_test_split

soil_humidity = numpy.random.randint(0, 100, 1000)
air_humiditiy = numpy.random.randint(0, 100, 1000)
temperature = numpy.random.randint(-250, 400, 1000) / 10
rain = numpy.random.randint(0, 100, 1000)
watered = numpy.random.choice([False, True], 1000)

data = numpy.dstack((soil_humidity, air_humiditiy, temperature, rain))[0]

X_train, X_test, y_train, y_test = train_test_split(data, watered, test_size=0.2, random_state=42)

model = tf.keras.Sequential()

# Input layer
model.add(tf.keras.layers.Dense(units=64, activation='relu', input_shape=(4,)))

# Hidden layers
model.add(tf.keras.layers.Dense(units=64, activation='relu'))
model.add(tf.keras.layers.Dense(units=64, activation='relu'))

# Output layer
model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=1000, batch_size=32)

test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

model.summary()

# Save the model
model.save('my_model.h5')
