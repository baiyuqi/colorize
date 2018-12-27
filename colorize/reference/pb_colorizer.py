import tensorflow as tf
from colorize.utils import *
from colorize.net import Net
from skimage.io import imsave
import numpy
import cv2
from PIL import  Image as IM

export_dir = "/tensorflow1/color/full_model"


sess = tf.Session()
tf.saved_model.loader.load(sess, ['standard_size'], export_dir)
y = sess.graph.get_tensor_by_name('conv23/BiasAdd:0')
inputPlace = sess.graph.get_tensor_by_name('Placeholder:0')
def transform( pil_image):
    pil_image = pil_image.convert("RGB")
    img = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    # img = cv2.imread(path)
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img[None, :, :, None]
    data_l = (img.astype(dtype=np.float32)) / 255.0 * 100 - 50
    return data_l
def colorize(  path, pil_image):
    data_l = transform(pil_image)
    conv8_313 = sess.run(y, feed_dict={inputPlace: data_l})
    img_rgb = decode(data_l, conv8_313,2.63)
    path, file = os.path.split(path)
    file = "colorized-" + file;
    color = os.path.join(path,file)
    imsave(color, img_rgb)
    return color;
