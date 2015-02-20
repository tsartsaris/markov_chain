#!/usr/bin/env python
# encoding: utf-8
import random
from itertools import izip
from collections import Counter
"""
     Αυτή είναι η γραφική αναπαράσταση των πιθανών θέσεων που μπορεί να πάει το 
     αντικείμενο. Απαγορευμένες κινήσεις όπως δείχνει οι διαγώνιες 'AD''DA''CB''BC'
     C|D
    -----
     A|B
"""

"""
     Αυτές είναι οι πιθανότητες να είναι σε μία από τις θέσεις αρχικά το 
     αντικείμενο. Από εδώ θα κάνουμε την αρχικοποίηση του sampling
"""
initial_state = {'A': 0.5 , 'B' : 0.5 , 'C' : 0 , 'D' : 0 }
sampling_dict = {} 
"""
     Στο sampling_dict θα αποθηκεύσουμε τις πιθανές διαδρομές που θα δώσει 
     ο αλγόριθμος. Η μορφή του θα είναι στην αρχικοποίηση
     {1: ['B'], 2: ['A'], 3: ['A'], 4: ['B'], 5: ['A'], 6: ['A'],
     7: ['B'], 8: ['B'], 9: ['B'], 10: ['A'], 11: ['B'], 12: ['B'],
     13: ['A'], 14: ['A'], 15: ['B'], 16: ['A'], 17: ['A'], 18: ['A'],
     19: ['A'], 20: ['A'], 21: ['B'], 22: ['B'], 23: ['A'], 24: ['B'], 
     25: ['A'], 26: ['B'], 27: ['B'], 28: ['A'], 29: ['B'], 30: ['A'], 
     31: ['B'], 32: ['B'], 33: ['A'], 34: ['A'], 35: ['B'], 36: ['A'], 
     37: ['B'], 38: ['B'], 39: ['A'], 40: ['A'], 41: ['A'], 42: ['A'].......................
     Από την αρχικοποίηση αποκλείω την περίπτωση να ξεκινήσει το αντικείμενο 
     από σημείο με μηδενική πιθανότητα.
     """



"""
     Το probability_lookup είναι ένα dictionary από το οποίο κάθε φορά θα πέρνουμε 
     την πιθανότητα μετακίνησης σε μία θέση από την προηγούμενη
"""
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



"""
     Το camera_lookup δίνει την πιθανότητα με βάση την οποία η παρατήρηση 
     της κάμερας που μας έχει δωθεί είναι σωστή και κατά πόσο
     Στην περίπτωσή μου δόθηκε 
     15 ΤΣΑΡΤΣΑΡΗΣ ΣΩΤΗΡΗΣ (1, 1) (2, 1) (2, 2) (2, 2)
     το οποίο μεταφράζω με το παρακάτω. 
"""
camera_lookup = {
    1 : { 'A' : 0.5 , 'D' : 0.2 , 'B' : 0.2 , 'C' : 0.1}, # στην t1 η camera λέει (1,1)
    2 : { 'B' : 0.5 , 'A' : 0.2 , 'C' : 0.2 , 'D' : 0.1}, # στην t1 η camera λέει (1,1)
    3 : { 'D' : 0.5 , 'C' : 0.2 , 'A' : 0.2 , 'B' : 0.1}, # στην t1 η camera λέει (1,1)
    4 : { 'D' : 0.5 , 'C' : 0.2 , 'A' : 0.2 , 'B' : 0.1}  # στην t1 η camera λέει (1,1)
}


i = 0 # enumarator ο οποίος θα βοηθήσει στην σωστή δομή του sampling_dict
      # κάθε φορά που θα αποθηκεύουμε μία θέση στο επόμενο loop θα έχουμε 
      # και το i του loop
while len(sampling_dict)<10000: # θέλω 10000 samples οπότε για όσο dictionary
                                # θα είναι μικρότερο του 10000 τρέχω το loop
    ransam = random.sample( initial_state.items(), 1 )  # επιλέγω ένα τυχαίο σημείο από το initial_state
                                                        # αφού οι θέσεις Α και Β είναι ισοπίθανες μου αρκεί 
                                                        # μία τυχαία επιλογή
    for key,value in ransam: # κάνω iterate στην επιλογή του random
        if key != 'A' and key != 'B': # αν δεν είναι το 'A' ή το 'B'
            pass # δεν κάνω τίποτα
        else:
            i+=1 # αν είναι 'A' ή 'Β' τότε ο enumarator είναι +1
            sampling_dict[i] = [key] # και βάζω την θέση στο dictionary

"""
     Από εδώ και πέρα έχω την αρχικοποίηση των θέσεων και αυτό που θέλω να κάνω
     είναι να συμπληρώσω τη διαδρομή μέχρι t5. Θα κάνω ένα iteration σε όλες τις 
     αρχικοποιημένες τιμές του sampling_dict και για όσο η κάθε διαδρομή είναι
     μικρότερη των 5 θέσεων στο σύνολό της θα επιλέγω random ένα σημείο και θα το βάζω μέσα
     Σε αυτό το σημείο να πω ότι δεν θα είναι ακριβώς random μιας και υπολογίζω την πιθανότητα 
     να κάνει αυτή την κίνηση το αντικείμενο και τη συγκρίνω με έναν random από 0 μέχρι 1
     μόνο όταν είναι μεγαλύτερη η πιθανότητα από τον random την επιλέγω και την προσθέτω στη διαδρομή.
"""
for k,v in sampling_dict.iteritems(): # iterate σε όλα τα στοιχεία του sampling_dict
    while len(v)<5: # για όσο η διαδρομή είναι μικρότερη του 5
        camera_lookup_pick = len(v) #πέρνω την παρατήρηση της κάμερας για εκίνεη τη θέση
        ransam = random.sample( initial_state.items(), 1 ) #επιλέγω μία random νέα θέση για την επόμενη 
                                                           #χρονική στιγμή
        first_param = v[-1] # πέρνω κάθε φορά την τελευταία θέση της διαδρομής
        second_param = ransam[0][0] # και την επόμενη που μου έδωσε η random επιλογή
        random_sample = random.random() # και έναν τυχαίο αριθμό από 0 μέχρι 1
        seq_to_check = str(first_param) + str(second_param) #κατασκευάζω το μονοπάτι των δύο επιλογών
                                                            # για να πάρω την πιθανότητα μετακίνησης
                                                            # από το probability_lookup
        if seq_to_check not in  ['AD' , 'DA', 'BC', 'CB']:  # αν το μονοπάτι δεν είναι στις απαγορευμένες κινήσεις
                                                            # που είναι οι διαγώνιες τότε 
            probability1 = probability_lookup[seq_to_check] # τότε έχουμε την πιθανότητα μετακίνησης από τη μία θέση στην άλλη
            camera_lookup_pick_dict = camera_lookup[camera_lookup_pick] # και την πιθανότητα με βάση την παρατήρηση της κάμερας
            probability2 = camera_lookup_pick_dict[second_param]
            if probability1*probability2>random_sample: # αν το γινόμενο των 2 πιθανοτήτων είναι μεγαλύτερο από τον random
                v.append(second_param) # αποδέχομαι τη θέση και την προσθέτω στο μονοπάτι μου
        else:
            pass #διαφορετικά μην κάνεις τίποτα και ξαναδοκίμασε


"""
     Από εδώ και πέρα κάνω καταμέτρηση των λύσεων για να δω πια υπερισχύει
"""
or k,v in sampling_dict.items():
    v = ''.join(v)
    sampling_dict[k] = v

D = Counter()

for sequen in sampling_dict.itervalues():
    D[sequen] += 1

deep_copy_D = {}

import matplotlib.pyplot as plt



plt.plot(range(len(D)), D.values())
plt.xticks(range(len(D)), D.keys())

plt.show()
for k,v in D.iteritems():
    if v < 50: # σκοτώνω πολύ μικρές τιμές για να δείχνει το ιστόγραμμα τα labels στον άξονα Y
        pass
    else:
        deep_copy_D[k]=v
D = {}
D = deep_copy_D
import pylab as pl
import numpy as np
X = np.arange(len(D))
pl.bar(X, D.values(), align='center', width=1)
pl.xticks(X, D.keys())
pl.xticks(rotation=45)

ymax = max(D.values()) + 1
pl.ylim(0, ymax)
pl.show()


print D
