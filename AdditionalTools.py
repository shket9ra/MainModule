#вспомогательный модуль для выноса общих вещей для Meth и остальных методо(блоков)-содержащих 
#
#
#

import random

import sys
import time
from vec2d import *
import math
from Tkinter import * 
import ttk
import mlpy
import numpy as np
import matplotlib.pyplot as plt
import DotsL
import copy

def NTAoL(NumpyArray):
    NewArray=[]
    for i in NumpyArray:
        NewArray.append(list(i))

    return NewArray
