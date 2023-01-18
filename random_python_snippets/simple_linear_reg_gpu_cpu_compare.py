import time
import tensorflow as tf
start = time.process_time()

'''
This code sets up a simple linear regression model using the TensorFlow library. The model is created 
using the Sequential API, and it has a single dense layer with one unit and an input shape of one. 
The Adam optimizer with a learning rate of 1 is used to update the model's parameters during training, 
and the mean squared error is used as the loss function.

The script then provides some example data (xs=[1, 2, 3, 4], ys=[2, 4, 6, 8]) 
and trains the model for 10 epochs using the fit() method. Finally, the model is used to 
make a prediction for a new input (x=10.0), and the predicted output is printed.
'''

# Set up a linear regression model
# model object to stack layers in a linear fashion.
model = tf.keras.Sequential()
# Create dense(fully connectec) layer, which is a layer that is connected to all
# the neurons in the previous layer.(on top of existing layers)
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

# Compile the model with an optimizer and a loss function
# optimizer: how the model is updated based on the data it sees and its loss function.
# loss function: measures how accurate the model is during training. Used as guidance/fct "mean squred error"
# Lower MSE is better
model.compile(optimizer=tf.keras.optimizers.Adam(1), loss='mean_squared_error')

# Provide some example data
xs = [1, 2, 3, 4]  # Independent variable
ys = [2, 4, 6, 8]  # Dependent variable
start = time.process_time()

# Train the model on the data, adjust the parameters to minimize the loss and produce best linear fit for data
# An epoch is a single pass through the entire training dataset. During each epoch,
# the model's parameters are updated to minimize the loss function, which should
# lead to a better fit to the training data.
model.fit(xs, ys, epochs=10)

# Make a prediction using the trained model
# takes a list of input values and returns a list of corresponding output
# values predicted by the trained model. the method uses the learned parameters of the model
# and the input povided to estimate the output. since the model is trained to fit the relationship of y = 2x.

print(model.predict([10.0]))

end = time.process_time()
print(f'Time: {end - start:.4f} seconds')


with tf.device('CPU:0'):

    # Set up a linear regression model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))

    # Compile the model with an optimizer and a loss function
    model.compile(optimizer=tf.keras.optimizers.Adam(1),
                  loss='mean_squared_error')

    # Provide some example data
    xs = [1, 2, 3, 4]
    ys = [2, 4, 6, 8]
    start = time.process_time()

    # Train the model on the data
    model.fit(xs, ys, epochs=10)

    # Make a prediction using the trained model
    print(model.predict([10.0]))

end = time.process_time()
print(f'Time: {end - start:.4f} seconds')
