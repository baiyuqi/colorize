import tensorflow as tf
from colorize.utils import *
from colorize.net import Net
from skimage.io import imsave
import numpy
import cv2
from PIL import  Image as IM

export_dir = "/tensorflow1/color/full_model"
class Colorizer:
    def __init__(self):

        self.sess = tf.Session()
        tf.saved_model.loader.load(self.sess, ['standard_size'], export_dir)
        self.y = self.sess.graph.get_tensor_by_name('conv23/BiasAdd:0')
        self.inputPlace = self.sess.graph.get_tensor_by_name('Placeholder:0')
    def __init1__(self):
        autocolor = Net(train=False)
        self.inputPlace = tf.placeholder(dtype=np.float32, shape=(1, 200, 300, 1))
        self.conv8_313 = autocolor.inference(self.inputPlace)
    def colorize( self, path, pil_image):
        data_l = self.transform(pil_image)
        saver = tf.train.Saver()
        with tf.Session() as sess:
          saver.restore(sess, '../models/model.ckpt')
          conv8_313 = sess.run(self.conv8_313, feed_dict={self.inputPlace: data_l})

          img_rgb = decode(data_l, conv8_313,2.63)
        #  img = PIL.Image.fromarray( img_rgb, 'RGB')
          path, file = os.path.split(path)
          file = "colorized-" + file;
          color = os.path.join(path,file)

          imsave(color, img_rgb)
          return color;

    def transform(self, pil_image):
        pil_image = pil_image.convert("RGB")
        img = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
        # img = cv2.imread(path)
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img[None, :, :, None]
        data_l = (img.astype(dtype=np.float32)) / 255.0 * 100 - 50
        return data_l

    def exportModel(self):

        builder = tf.saved_model.builder.SavedModelBuilder(export_dir)
        saver = tf.train.Saver()
        with tf.Session() as sess:
            saver.restore(sess, '../models/model.ckpt')
            builder.add_meta_graph_and_variables(sess,['standard_size'])
        builder.save()
    def load(self):
         with tf.Session() as sess:
             meta_graph_def = tf.saved_model.loader.load(sess, ['standard_size'], export_dir)
             y = sess.graph.get_tensor_by_name('conv23/BiasAdd:0')
    # 'conv23/BiasAdd:0'
    def colorize1( self, path, pil_image):
        data_l = self.transform(pil_image)
        conv8_313 = self.sess.run(self.y, feed_dict={self.inputPlace: data_l})
        img_rgb = decode(data_l, conv8_313,2.63)
        path, file = os.path.split(path)
        file = "colorized-" + file;
        color = os.path.join(path,file)
        imsave(color, img_rgb)
        return color;