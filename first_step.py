#!/usr/bin/env python
# encoding: utf-8
import random
"""
	 C|D
	-----
	 A|B
"""

initial_state = {'A': 0.5 , 'B' : 0 , 'C' : 0.5 , 'D' : 0 }
sampling_dict = {}




i = 0 #enumarator gia na exw se mia seira tis pi8anes diadromes
while len(sampling_dict)<=1000: # 8elw 1000 samples opote gia oso to dictionary
								# 8a einai mikrotero tou 1000 trexw to loop
	ransam = random.sample( initial_state.items(), 1 )  # pernw tuxaia ena stoixeio
	for key,value in ransam:
		if key != 'A' and key != 'C': #an den einai to 'A' h to 'C'
			pass # den kanw tipota
		else:
			i+=1 # an einai 'A' h 'C' tote o enumarator einai +1
			sampling_dict[i] = key # kai bazw thn timh sto cictionary
print sampling_dict
