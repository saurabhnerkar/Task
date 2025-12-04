import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.callbacks import EarlyStopping


(X_train, y_train), (X_val, y_val) = mnist.load_data()

X_train = X_train / 255.0
X_val   = X_val / 255.0


model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


early_stop = EarlyStopping(
    monitor='val_loss',         
    patience=3,                 
    restore_best_weights=True,  
    verbose=1
)

history = model.fit(
    X_train, y_train,
    epochs=30,                      
    batch_size=128,
    validation_data=(X_val, y_val),
    callbacks=[early_stop],
    verbose=2
)

loss, acc = model.evaluate(X_val, y_val, verbose=0)
print("\nFinal Model Accuracy:", acc)