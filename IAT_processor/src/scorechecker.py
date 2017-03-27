'''
Created on 27 Mar 2017

@author: id121943
'''

import os, glob, pandas, csv
import numpy as np

# results header index's
participant_condition = 0
participant_correct = 1
participant_response_time = 2
participant_stim_type = 3
participant_target = 4

print("IAT Results processor")

path = os.curdir

score_array = []
mean_score = 0
sd_score = 0

for current_file in glob.glob(os.path.join(path, '*.csv')):
    print("Now processing" + current_file)
    
    summed_score = 0
    # open CSV and read in line by line
    with open(current_file, 'rb') as f:
        # discard first line
        next(f)
        
        read_in = csv.reader(f)
        for curr_row in read_in:
        #  this is at the `row` level        
            # add the score
            summed_score += int(curr_row[participant_correct])
            
            # if ((curr_row[0] =='5') or (curr_row[0] == '3')):
                #discard first two rows 
                #print(curr_row[0])
        # print('participant\'s score = ' + str(summed_score))       
    score_array.append(summed_score)
#print('total score = ' + str(sum(score_array)))
print('mean score = ' + str(np.mean(score_array)))
print('SD = ' + str(np.std(score_array)))    