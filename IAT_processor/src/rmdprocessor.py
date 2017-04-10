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
positive_pre = []
negative_pre = []

positive_post = []
negative_post = []


# do a glob to get the files in the directory *BEFORE* creating the output file
existing_files = glob.glob(os.path.join(path, '*.csv'))

if len(existing_files) > 0:
    # open outfile for myth condition
    out_name_myth = open(os.path.join(path, 'processedResultsMyth.csv'),'wb') 
    out_handle_myth = csv.writer(out_name_myth)

    out_name_fact = open(os.path.join(path, 'processedResultsFact.csv'),'wb') 
    out_handle_fact = csv.writer(out_name_fact)

    # write the headers
    out_handle_myth.writerow(['Participant' , 'mean positive pre', 'mean negative pre', 'difference pre', 'mean positive post', 'mean negative post', 'difference post'])
    out_handle_fact.writerow(['Participant' , 'mean positive pre', 'mean negative pre', 'difference pre', 'mean positive post', 'mean negative post', 'difference post'])
    
for current_file in existing_files:
  
    print("Now processing" + current_file)
    
    # clear variables and arrays    
    
    del positive_pre[:]
    del negative_pre[:]
    del positive_post[:]
    del negative_post[:]    
    

    
    # open CSV and read in line by line
    with open(current_file, 'rb') as f:
        # discard first line, which contains the headers
        next(f)
        # read in the remainder of the file
        read_in = csv.reader(f)
        for curr_row in read_in:
        #  this is at the `row` level        
            
            # check whether this is before or after the intervention
            if (float(curr_row[participant_vignette_number]) < 5):  # PRE
                if(curr_row[participant_response] == 'a'):  # positive
                    positive_pre.append(curr_row[participant_response_time])

                else:   #negative
                    negative_pre.append(curr_row[participant_response_time])      
            else:   # POST
                if(curr_row[participant_response] == 'a'):  # positive
                    positive_post.append(curr_row[participant_response_time])

                else:   #negative
                   negative_post.append(curr_row[participant_response_time])                
 
        # calculate the averages etc.
        
      
        #write name (clean current file first)
        infilename = current_file[2:]
        linedata = [infilename, diff_score, summed_score, per_corr, processed_trials, lb_count, hb_count] 
        out_handle.writerow(linedata)
print('Processed ' + str(len(existing_files)) + ' results files')
#close the outfile
out_name_1.close()


def ( parameters ):
   "function_docstring"
   function_suite
   return [expression]