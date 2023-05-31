import random
import math 
from array import *
from math import pi
import numpy as np

############################################################
# Bubble Sort Algorithm
############################################################

def bubble_sort(arr, count):
    for i in range(count):    

        #insert keyframe for every cube on every frame
        for cube in arr:
            cube.keyframe_insert(data_path="location", frame=i) 

        already_sorted = True
        for j in range(count - i -1):

            #get materials
            mat1 = arr[j].active_material.diffuse_color
            mat2 = arr[j + 1].active_material.diffuse_color

            rg1, rg2 = get_rg(mat1, mat2)

            #compare first colorarray values
            if rg1 > rg2: 

                #change location & insert keyframes based on bubble sort
                arr[j].location.x = (j+1)*2
                arr[j].keyframe_insert(data_path="location", frame=i+1)

                arr[j+1].location.x = j*2
                arr[j+1].keyframe_insert(data_path="location", frame=i+1)       

                #rearrange arrays
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False

        if already_sorted:
            break

############################################################
# Setup Random Colors + Array to be sorted
############################################################

############################################################
# Get R and G Values from Material
############################################################

def get_rg(mat1, mat2):

    #get R value of both materials
    r1 = mat1[0]
    r2 = mat2[0]

    #get G value of both materials
    g1 = mat1[1]
    g2 = mat2[1]

    # R + G = value for comparison
    rg1 = r1 + g1
    rg2 = r2 + g2

    return rg1, rg2

############################################################
# Call Functions
############################################################

#setup_array(number of planes)
#Matrix, count = setup_array(24)#only even numbers are valid
data = list(range(24))
data = random.sample(data, k=24)
Matrix = data
count = 24
bubble_sort(data, count)
#bubble_sort + visualisation
#for i in range(count):
#    bubble_sort(Matrix[i], count)
