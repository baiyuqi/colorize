import  tensorflow as tf

W = tf.Variable([.3],tf.float32,name="W")
b = tf.Variable([-.3],tf.float32,name="bias")
x = tf.placeholder( tf.float32,name="input")
lm = x * W + b
ini = tf.global_variables_initializer()
with tf.Session() as sess:
    writer = tf.summary.FileWriter("/temp/logs", sess.graph)
    sess.run(ini)
    rst = sess.run(lm, {x:[1,2,3,4]})
    print(rst)