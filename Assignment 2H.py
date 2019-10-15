# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:27:03 2019

@author: HP
"""

import math
import numpy as np
def fillSudokuRow(sudokuRow):
    element_missing = sum(np.arange(1,10))-sum(sudokuRow) #sum of 1 to 9 is fixed 
                                                        #0 doesn't contribute to sum
    sudokuRow[sudokuRow==0]= element_missing
    return sudokuRow
