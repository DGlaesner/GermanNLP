# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 00:23:55 2021

@author: d.glaesner
"""

import tensorflow as tf

print(tf.__version__)

print(tf.test.is_built_with_cuda())

print(tf.config.list_physical_devices('GPU'))
