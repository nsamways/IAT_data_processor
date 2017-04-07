'''
Created on 27 Mar 2017

@author: neale samways
'''

import os, glob, csv
import numpy as np

# results header index's
participant_response = 0    # a for rape/positive, l for no rape/ negative
participant_response_time = 1
participant_truth_condition = 2
participant_vignette_number = 3


print("Results processor")

path = os.curdir

# variables
positive = []
negative = []
pos_total = 0
neg_total = 0
# untransformed score arrays

# do a glob to get the files in the directory *BEFORE* creating the output file
existing_files = glob.glob(os.path.join(path, '*.csv'))

if len(existing_files) > 0:
    # open outfile
    out_name = open(os.path.join(path, 'processedResults.csv'),'wb') 
    out_handle = csv.writer(out_name)

    # write the headers
    out_handle.writerow(['Participant' , 'mean positive', 'mean negative', 'difference', ])
    
for current_file in existing_files:
  
    print("Now processing" + current_file)
    
    # clear variables and arrays    
    pos_total = 0
    neg_total = 0
    processed_trials = 0
    
 
    del positive[:]
    del negative[:]
 
    # open CSV and read in line by line
    with open(current_file, 'rb') as f:
        # discard first line, which contains the headers
        next(f)
        # read in the remainder of the file
        read_in = csv.reader(f)
        for curr_row in read_in:
        #  this is at the `row` level        
            summed_score += int(curr_row[participant_correct])
            processed_trials += 1
        
            if (curr_row[participant_condition] == '3'):
                # discard first two rows 
                if cond3_status < 2:
                    cond3_status += 1
                else:
                # process the data 
                    if (int(curr_row[participant_response_time]) < lower_bound):    # push as lower bound
                        # print("Less than " + str(lower_bound))
                        lb_count += 1 # increase count
                        cond3_untransformed.append(lower_bound)
                    elif (int(curr_row[participant_response_time]) > higher_bound): # push as upper bound
                        # print("greater than " + str(higher_bound))
                        hb_count += 1
                        cond3_untransformed.append(higher_bound)
                    else:
                        cond3_untransformed.append(float(curr_row[participant_response_time]))
                        # print("continuing 3")
                        
            elif (curr_row[participant_condition] =='5'):
                # discard first two rows
                if cond5_status < 2:
                    cond5_status += 1
                    # print("Skipping" + str(cond5_status) + ' of 5')    # condition status
                else:
                    # check bounds
                    if (int(curr_row[participant_response_time]) < lower_bound):    # push as lower bound
                        # print("Less than " + str(lower_bound) + " : " + curr_row[participant_response_time])
                        lb_count += 1 # increase count
                        cond5_untransformed.append(lower_bound)
                    elif (int(curr_row[participant_response_time]) > higher_bound): # push as upper bound
                        # print("greater than " + str(higher_bound))
                        hb_count += 1   
                        cond5_untransformed.append(higher_bound)
                    else:
                        cond5_untransformed.append(float(curr_row[participant_response_time]))

        # write the outfile if the number of errors is acceptable
        
        # do the log transformaions
        c3_trans = np.log(cond3_untransformed)
        c5_trans = np.log(cond5_untransformed)
        # get the means 
        c3_mean = np.mean(c3_trans)
        c5_mean = np.mean(c5_trans)
        # compute the difference
        diff_score = c3_mean - c5_mean
        # calculate percent score    
        per_corr = 100.0*( float(summed_score)/float(processed_trials))
        #write name (clean current file first)
        infilename = current_file[2:]
        linedata = [infilename, diff_score, summed_score, per_corr, processed_trials, lb_count, hb_count] 
        out_handle.writerow(linedata)
print('Processed ' + str(len(existing_files)) + ' results files')
#close the outfile
out_name.close()