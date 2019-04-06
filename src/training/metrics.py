"""
To understand mode on jaquard loss and metrics, follow the link below:
https://www.jeremyjordan.me/semantic-segmentation/

"""

import numpy as np
from keras import backend as K
import tensorflow as tf
from keras.losses import binary_crossentropy
import config

def dice_coeff(y_true, y_pred, eps=K.epsilon()):

    if np.max(y_true) == 0.0:
        return dice_coeff(1-y_true, 1-y_pred) ## empty image; calc IoU of zeros
    
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    
    intersection = K.sum(y_true_f * y_pred_f)
    union = K.sum(y_true_f) + K.sum(y_pred_f) - intersection
    
    dice = (intersection + eps) / (union + eps)
  
    return dice


def dice_loss(y_true, y_pred, eps=1e-6):
    
    dloss = 1 -  dice_coeff(y_true, y_pred)
      
    return dloss


def bce_loss(y_true, y_pred):    
    return binary_crossentropy(y_true, y_pred)
    

def bce_dice_loss(y_true, y_pred):
    
    if not tf.contrib.framework.is_tensor(y_true):
        y_true = tf.convert_to_tensor(y_true, dtype=tf.float32)
        
    if not tf.contrib.framework.is_tensor(y_pred):
        y_pred = tf.convert_to_tensor(y_pred, dtype=tf.float32)  
    
    loss = bce_loss(y_true, y_pred)*config.cross_entropy_weight + \
                            dice_loss(y_true, y_pred)*config.dice_weight
    
    return loss


