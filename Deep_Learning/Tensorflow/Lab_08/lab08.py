# Lab 8 Tensor Manipulation
# https://www.tensorflow.org/api_guides/python/array_ops
import tensorflow as tf
import numpy as np
import pprint
tf.set_random_seed(777)  #  for reproducibility

pp = pprint.PrettyPrinter(indent=4)
sess = tf.InteractiveSession()

# 1. Simple Array
# t = np.array([0., 1., 2., 3., 4., 5., 6.])
# pp.pprint(t)
# t.ndim # rank
# t.shape # shape
# t[0], t[1], t[-1]
# t[2:5], t[4:-1]
# t[:2], t[3:]

# 2. 2D Array
# t = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.], [10., 11., 12.]])
# pp.pprint(t)
# t.ndim # rank
# t.shape # shape

# 3. Shape, Rank, Axis
# t = tf.constant([1,2,3,4])
# tf.shape(t).eval()

# t = tf.constant([[1,2],
#                  [3,4]])
# tf.shape(t).eval()

# t = tf.constant([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],[[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]])
# tf.shape(t).eval()

# [
#     [
#         [
#             [1,2,3,4], 
#             [5,6,7,8],
#             [9,10,11,12]
#         ],
#         [
#             [13,14,15,16],
#             [17,18,19,20], 
#             [21,22,23,24]
#         ]
#     ]
# ]

# 4. Matmul vs Multiply
# matrix1 = tf.constant([[3., 3.]])
# matrix2 = tf.constant([[2.],[2.]])
# tf.matmul(matrix1, matrix2).eval()

# (matrix1*matrix2).eval()

# 5. Watch out broadcasting
# matrix1 = tf.constant([[3., 3.]])
# matrix2 = tf.constant([[2.],[2.]])
# matrix1+matrix2).eval()

# matrix1 = tf.constant([[3., 3.]])
# matrix2 = tf.constant([[2., 2.]])
# matrix1+matrix2).eval()

# 6. Random values for variable initializations
# tf.random_normal([3]).eval()
# tf.random_uniform([2]).eval()
# tf.random_uniform([2, 3]).eval()

# 7. Reduce Mean/Sum
# tf.reduce_mean([1, 2], axis=0).eval()

# x = [[1., 2.],
#      [3., 4.]]

# tf.reduce_mean(x).eval()
# tf.reduce_mean(x, axis=0).eval()
# tf.reduce_mean(x, axis=1).eval()
# tf.reduce_mean(x, axis=-1).eval()
# tf.reduce_sum(x).eval()
# tf.reduce_sum(x, axis=0).eval()
# tf.reduce_sum(x, axis=-1).eval()
# tf.reduce_mean(tf.reduce_sum(x, axis=-1)).eval()

# 8. Argmax with axis
# x = [[0, 1, 2],
#      [2, 1, 0]]
# tf.argmax(x, axis=0).eval()
# tf.argmax(x, axis=1).eval()
# tf.argmax(x, axis=-1).eval()

# 9. Reshape, Squeeze, Expand_dims
# t = np.array([[[0, 1, 2], 
#                [3, 4, 5]],
              
#               [[6, 7, 8], 
#                [9, 10, 11]]])
# t.shape

# tf.reshape(t, shape=[-1, 3]).eval()
# tf.reshape(t, shape=[-1, 1, 3]).eval()
# tf.squeeze([[0], [1], [2]]).eval()
# tf.expand_dims([0, 1, 2], 1).eval()

# 10. One hot
# tf.one_hot([[0], [1], [2], [0]], depth=3).eval()
# t = tf.one_hot([[0], [1], [2], [0]], depth=3)
# tf.reshape(t, shape=[-1, 3]).eval()

# 11. Casting
# tf.cast([1.8, 2.2, 3.3, 4.9], tf.int32).eval()
# tf.cast([True, False, 1 == 1, 0 == 1], tf.int32).eval()

# 12. Stack
# x = [1, 4]
# y = [2, 5]
# z = [3, 6]

# Pack along first dim.
# tf.stack([x, y, z]).eval()
# tf.stack([x, y, z], axis=1).eval()

# 13. Ones like and Zeros like
# x = [[0, 1, 2],
#      [2, 1, 0]]

# tf.ones_like(x).eval()
# tf.zeros_like(x).eval()

# 14. Zip
# for x, y in zip([1, 2, 3], [4, 5, 6]):
#     x, y
# for x, y, z in zip([1, 2, 3], [4, 5, 6], [7, 8, 9]):
#     x, y, z

# 15. Transpose
# t = np.array([[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]])
# pp.pprint(t.shape)
# pp.pprint(t)

# t1 = tf.transpose(t, [1, 0, 2])
# pp.pprint(sess.run(t1).shape)
# pp.pprint(sess.run(t1))

# t = tf.transpose(t1, [1, 0, 2])
# pp.pprint(sess.run(t).shape)
# pp.pprint(sess.run(t))

# t2 = tf.transpose(t, [1, 2, 0])
# pp.pprint(sess.run(t2).shape)
# pp.pprint(sess.run(t2))

# t = tf.transpose(t2, [2, 0, 1])
# pp.pprint(sess.run(t).shape)
# pp.pprint(sess.run(t))
