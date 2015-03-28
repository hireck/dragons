#!/usr/bin/python
# -*- coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from operator import itemgetter


#**************** TOOLS ***********************

#giving structure to an input parameter:
class InputParam(object):
  def __init__(self, cat, shortname, longname, unit, minim, maxim):
        self.cat = cat
        self.shortname = shortname
        self.longname = longname
        self.unit = unit
        self.min = float(minim)
        self.max = float(maxim)
        #self.mean = float(ave)
  def generate_values(self, n):
        self.values = np.random.uniform(self.min, self.max, n)
        
#creating structured input parameters (from a list that was read from a file) and putting them into a dictionary:
def prepare_input(input_data, input_cats):
        for l in input_data:
                infos = l.strip().split('\t')
                ip = InputParam(*infos)
                ip.generate_values(n)
                input_cats[ip.cat][ip.shortname] = ip 
                
#giving structure to an output parameter:
class OutputParam(object):
  def __init__(self, shortname, plot_title, y_axis_name, unit):
        self.shortname = shortname
        self.plot_title = plot_title
        self.y_label = y_axis_name
        self.unit = unit
        #self.fuction = function
    #def calculate_impact(self):
        #self.values = self.function(*args)
                
                
#*************** THE MODEL *********************

def cal_num_knights(dragons,knight_population,food_factor):

  knights = knight_population - dragons['number'].values * food_factor * dragons['weigth'].values + knight_population*(1.-1./np.log10(dragons['age'].values))
  
  return knights



def cal_dragon_output(dragons,knight_population,knights_left):

  digestion_efficiency = dragons['age'].values * dragons['weigth'].values

  digested_knights_products = (knight_population - knights_left)/digestion_efficiency
  
  return digested_knights_products


        


#***************** LOAD INPUT ***********************

#set the number of repetitions: 
n = 1000       

#set any fixed values:
initial_knight_population = 15430
food_factor = 10.

#initialize a dictionary to hold all your input data, organized by category:
input_cats = defaultdict(dict)

# read in the data from a file:       
input_data = open('dragon_farm_input.txt', 'r').readlines()[1:]
#structure it and put it into the input_cats dictionary:
prepare_input(input_data, input_cats) 


#***************** RUN THE MODEL *********************

dragons = input_cats['dragons']
#knights = input_cats['knights'] #not used right now, as we have only 'initial knight population' with a fixed value
#but you could add this one and other knight parameters to the input file, just like the dragons, 
#e.g. knight running speed, knight armor budget, ....

#initialize a dictionary to hold the output of the calculations:
impact_factors = {}

#create the output parameter 'knights_left':
impact_factors['knights_left'] = OutputParam('knights_left', 'Knight population', 'Knights left', '')
#calculate the values for this output parameter:
impact_factors['knights_left'].values = cal_num_knights(dragons,initial_knight_population,food_factor) 

knights_left = impact_factors['knights_left'].values

impact_factors['dragon_output'] = OutputParam('dragon_output', 'Dragon waste products', 'Dragon output', 'kg')
impact_factors['dragon_output'].values = cal_dragon_output(dragons,initial_knight_population, knights_left)

#*********** PLOT *************

for ic in input_cats:
    incat = input_cats[ic]
    for factor in impact_factors:
        outpar = impact_factors[factor]
        sorted_inparams = sorted(incat.keys())
        for i, key in enumerate(sorted_inparams):
            inpar = incat[key]
            rows = len(sorted_inparams) / 2
            plt.subplot(2, 2, i) #which of the 2's indicates the number of rows?
            #if i == 0:
                #plt.title(outpar.plot_title)
            plt.plot(inpar.values, outpar.values, 'ro')
            plt.xlabel(inpar.longname)
            plt.ylabel(outpar.y_label)
        plt.show()

