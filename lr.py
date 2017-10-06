import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE='DATA/fire_theft.xls'

# Step 1: read in data from the .xls file
# Ps: if you are  unfamilar with  xlrd, please read xlrd.py
book = xlrd.open_workbook(DATA_FILE, encoding_override='utf-8') # open a xls file
sheet = book.sheet_by_index(0) # get the sheet by index, alse can implemant this by name
data = np.asarray([sheet.row_values(i) for i in range(1,sheet.nrows)]) # asarray is just convert the data to ndarray ,then can compute it in numpy
n_samples = sheet.nrows - 1
# Step 2: create placeholders for  input x( number of fire) and input y (number of theft)
X = tf.placeholder(tf.float32,name='X')
Y = tf.placeholder(tf.float32,name='Y')

# Step 3: create weight and bias ,initialized to 0
w = tf.Variable(0.0,name='weights')
b = tf.Variable(0.0,name='bias')

# Step 4: construct model to predict Y from X
Y_predicted = X*w + b

# Step 5: use the square error as the loss function
loss = tf.square(Y - Y_predicted,name='loss')

# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

with tf.Session() as sess:
    # Step 7: initialize the necessary variables ,in this case ,w and b
    sess.run(tf.global_variables_initializer())

    # Step 8: train the model
    for i in range(100) :
        for x,y in data:
            # Session run train_op to minimize loss
            sess.run(optimizer,feed_dict={X:x,Y:y})

    # Step 9: output the values of w and b
    w_value,b_value = sess.run([w,b])
    print(w_value)
    print(b_value)
