#!/usr/bin/env python
# encoding: utf-8
import random
from itertools import izip
from collections import Counter
"""
     C|D
    -----
     A|B
"""

initial_state = {'A': 0.5 , 'B' : 0.5 , 'C' : 0 , 'D' : 0 }
sampling_dict = {}

probability_lookup = {
    'AA' : 0.2,
    'AB' : 0.4,
    'AC' : 0,
    'AD' : 0.4,
    'BA' : 0.4,
    'BB' : 0.2,
    'BC' : 0.4,
    'BD' : 0,
    'CA' : 0,
    'CB' : 0.4,
    'CC' : 0.2,
    'CD' : 0.4,
    'DA' : 0.4,
    'DB' : 0,
    'DC' : 0.4,
    'DD' : 0.2
}

camera_lookup = {
    1 : { 'A' : 0.5 , 'D' : 0.2 , 'B' : 0.2 , 'C' : 0.1},
    2 : { 'B' : 0.5 , 'A' : 0.2 , 'C' : 0.2 , 'D' : 0.1},
    3 : { 'D' : 0.5 , 'C' : 0.2 , 'A' : 0.2 , 'B' : 0.1},
    4 : { 'D' : 0.5 , 'C' : 0.2 , 'A' : 0.2 , 'B' : 0.1}
}

#nasos values
# camera_lookup = {
#   1 : { 'D' : 0.5 , 'C' : 0.2 , 'A' : 0.2 , 'B' : 0.1},
#   2 : { 'D' : 0.5 , 'C' : 0.2 , 'A' : 0.2 , 'B' : 0.1},
#   3 : { 'B' : 0.5 , 'A' : 0.2 , 'C' : 0.2 , 'D' : 0.1},
#   4 : { 'C' : 0.5 , 'B' : 0.2 , 'D' : 0.2 , 'A' : 0.1}
# }


i = 0 #enumarator gia na exw se mia seira tis pi8anes diadromes
while len(sampling_dict)<10000: # 8elw 1000 samples opote gia oso to dictionary
                                # 8a einai mikrotero tou 1000 trexw to loop
    ransam = random.sample( initial_state.items(), 1 )  # pernw tuxaia ena stoixeio
    for key,value in ransam:
        if key != 'A' and key != 'B': #an den einai to 'A' h to 'C'
            pass # den kanw tipota
        else:
            i+=1 # an einai 'A' h 'C' tote o enumarator einai +1
            sampling_dict[i] = [key] # kai bazw thn timh sto cictionary


for k,v in sampling_dict.iteritems():
    while len(v)<5:
        camera_lookup_pick = len(v)
        ransam = random.sample( initial_state.items(), 1 )
        first_param = v[-1]
        second_param = ransam[0][0]
        random_sample = random.random()
        seq_to_check = str(first_param) + str(second_param)
        if seq_to_check not in  ['AD' , 'DA', 'BC', 'CB']: 
            probability1 = probability_lookup[seq_to_check]
            camera_lookup_pick_dict = camera_lookup[camera_lookup_pick]
            probability2 = camera_lookup_pick_dict[second_param]
            if random_sample<probability1*probability2:
                v.append(second_param)
        else:
            pass

for k,v in sampling_dict.items():
    v = ''.join(v)
    sampling_dict[k] = v

cnt = Counter()

for sequen in sampling_dict.itervalues():
    cnt[sequen] += 1

print cnt
