import numpy as np
import matplotlib.pyplot as plt


################ THE MODEL ################

def cal_num_knights(dragons,knight_population,food_factor):

  knights = knight_population - dragons[number].values * food_factor * dragons[weigth].values + knight_population*(1.-1./np.log10(dragons[age].values))
  
  return knights



def cal_dragon_output(dragons,knight_population,knights_left):

  digestion_efficiency = dragons[age].values * dragons[weigth].values

  digested_knights_products = (knight_population - knights_left)/digestion_efficiency
  
  return digested_knights_products


############## TOOLS TO FETCH AND PREPARE INPUT ###########


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

def prepare_input(input_data, input_cats):
	for l in input_data:
		infos = l.strip().split('\t')
		ip = InputParam(*infos)
		ip.generate_values(n)
		input_cats[ip.cat][ip.shortname] = ip 

########### LOAD INPUT ###################
 
n = 1000 	
initial_knight_population = 15430
food_factor = 10.
input_cats = defaultdict(dict)

  	
input_data = open('dragon_farm_input.txt', 'r').readlines()[1:]
prepare_input(input_data)


########### RUN THE MODEL ###########

dragons = input_cats['dragons']
#knights = input_cats['knights'] #not used right now, as we have only 'initial knight population' with a fixed value
#but you could add this one and other knight parameters to the input file, just like the dragons, 
#e.g. knight running speed, knight armor budget, ....



knights_left = cal_num_knights(input_params,initial_knight_population,food_factor) 

dragon_leftovers = cal_dragon_output(input_params,initial_knight_population,knights_left)


plt.subplot(2, 2, 1)
plt.title('Knight population')
plt.plot(dragons.number[4],knights_left,'ro')
plt.xlabel(dragons.number[0])
plt.ylabel('Kinghts left')

plt.subplot(2, 2, 2)
plt.plot(dragons.length[4],knights_left,'ro')
plt.xlabel(dragons.length[0])
plt.ylabel('Kinghts left')

plt.subplot(2, 2, 3)
plt.plot(dragons.weigth[4],knights_left,'ro')
plt.xlabel(dragons.weigth[0])
plt.ylabel('Kinghts left')

plt.subplot(2, 2, 4)
plt.plot(dragons.age[4],knights_left,'ro')
plt.xlabel(dragons.age[0])
plt.ylabel('Kinghts left')

plt.show()




plt.subplot(2, 2, 1)
ylabel1 = 'Dragon output [kg]'
plt.title('Dragon leftovers')
plt.plot(dragons.number[4],dragon_leftovers,'ro')
plt.xlabel(dragons.number[0])
plt.ylabel(ylabel1)

plt.subplot(2, 2, 2)
plt.plot(dragons.length[4],dragon_leftovers,'ro')
plt.xlabel(dragons.length[0])
plt.ylabel(ylabel1)


plt.subplot(2, 2, 3)
plt.plot(dragons.weigth[4],dragon_leftovers,'ro')
plt.xlabel(dragons.weigth[0])
plt.ylabel(ylabel1)

plt.subplot(2, 2, 4)
plt.plot(dragons.age[4],dragon_leftovers,'ro')
plt.xlabel(dragons.age[0])
plt.ylabel(ylabel1)

plt.show()

#print knights_left

#print dragon_leftovers

#print dragons.number[4],knights_left



#for attr, value in dragons.__dict__.iteritems():
#       print attr

#a = dir(dragons) if not dragons.startswith('__')

#[i for i in dir(dragons) if not dragons.startswith('__')]

