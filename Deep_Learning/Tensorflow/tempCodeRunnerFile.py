aceholder(tf.float32, shape=[None, 3])
# Y = tf.placeholder(tf.float32, shape=[None, 1])

# W = tf.Variable(tf.random_normal([3, 1]), name='weight')
# b = tf.Variable(tf.random_normal([1]), name='bias')

# # Hypothesis
# hypothesis = tf.matmul(X, W) + b

# # Simplified cost/loss function
# cost = tf.reduce_mean(tf.square(hypothesis - Y))

# # Minimize
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
# train = optimizer.minimize(cost)

# # Launch the graph in a session.
# sess = tf.Session()
# # Initializes global variables in the graph.
# sess.run(tf.global_variables_initializer())

# for step in range(2001):
#     cost_val, hy_val, _ = sess.run([cost, hypothesis, train], 
#                                    feed_dict={X: x_data, Y: y_data})
#     if step % 10 == 0:
#         print(step, "Cost:", cost_val, "\nP