from psychopy import core, event, visual, monitors
import numpy as np
import os
import csv

#monitor specs
mon = monitors.Monitor('myMonitor', width=14.2, distance=8) 
mon.setSizePix([1366,768])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

#make pathway and filename
filename = 'Sess1Sub1.csv'
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
fullAddress = os.path.join(data_dir, filename)
print(fullAddress)

#blocks, trials, stims, and clocks
nBlocks=2
nTrials=4
#define blocks and trials
blocks = [[0, 0, 0, 0], [1, 1, 1, 1]] 
trials = [[0, 1, 2, 3], [0, 1, 2, 3]] 
my_text=visual.TextStim(win)
rt_clock = core.Clock()  # create a response time clock
cd_timer = core.CountdownTimer() #add countdown timer

#prefill lists for responses
sub_resp = [[-1]*nTrials]*nBlocks
sub_acc = [[-1]*nTrials]*nBlocks
prob = [[-1]*nTrials]*nBlocks
corr_resp = [[-1]*nTrials]*nBlocks
resp_time = [[-1]*nTrials]*nBlocks

#create problems and solutions that will show in trials
math_problems = ['3 + 2 =','5 - 3 =','4 + 4 =','1 + 5 ='] #problems
solutions = [5,2,8,6] #solutions
prob_sol = list(zip(math_problems,solutions))

#empty lists for dict.
sub_resp = dict()
sub_acc = dict()
prob = dict()
corr_resp = dict()
resp_time = dict()

#-draw start trial text
startr_msg = "Start of Trials"
startr_text = visual.TextStim(win, text = startr_msg)
startr_text.color = 'lawngreen'
startr_text.draw()
#-flip window
win.flip() 
#-wait time (stimulus duration)
core.wait(1)

for block in range(nBlocks):
    sub_resp[block]= [-1]*nTrials
    sub_acc[block] = [-1]*nTrials
    prob[block] = [-1]*nTrials
    corr_resp[block] = [-1]*nTrials
    resp_time[block] = [-1]*nTrials
    
    for trial in range(nTrials):
        #what are the problems and responses?
        prob[block][trial] = prob_sol[np.random.choice(4)]
        corr_resp[block][trial] = prob[block][trial][1]
        
        rt_clock.reset()  # reset timing for every trial
        cd_timer.add(3) #add 3 seconds

        event.clearEvents(eventType='keyboard')  # reset keys for every trial
        
        count=-1 #for counting keys
        while cd_timer.getTime() > 0: #for 3 seconds

            my_text.text = prob[block][trial][0] #present the problem for that trial
            my_text.color = 'yellow'
            my_text.draw()
            win.flip()

            #collect keypresses after first flip
            keys = event.getKeys(keyList=['1','2','3','4','escape'])

            if keys:
                count=count+1 #count up the number of times a key is pressed

                if count == 0: #if this is the first time a key is pressed then get RT for first response in that loop
                    resp_time[block][trial] = rt_clock.getTime()
                    #get key for only the first response in that loop
                    sub_resp[block][trial] = keys[0] #remove from list

        #record subject accuracy
        #keys are saved as strings
        if sub_resp[block][trial] == str(corr_resp[block][trial]):
            sub_acc[block][trial] = 1 #arbitrary number for accurate response
        elif sub_resp[block][trial] != str(corr_resp[block][trial]):
            sub_acc[block][trial] = 2 #arbitrary number for inaccurate response 
                                    #(should be something other than 0 to distinguish 
                                    #from non-responses)
                    
        #print results
        print('problem=', prob[block][trial], 'correct response=', 
              corr_resp[block][trial], 'subject response=',sub_resp[block][trial], 
              'subject accuracy=',sub_acc[block][trial])

win.close()

#put all dicts into one list
data_as_list = [prob, corr_resp, sub_resp, sub_acc, resp_time]
print(data_as_list) #to show what it looks like

with open(fullAddress, 'w') as sub_data:
    fieldnames = ['block', 'trial', 'problem','corr_resp','sub_resp','sub_acc', 'resp_time'] #excel headers
    data_writer = csv.DictWriter(sub_data, fieldnames=fieldnames)
    data_writer.writeheader()

    for block in range(nBlocks):  #to make excel look pretty
        data_as_dict = []
        for a,b,c,d,e,f,g in zip(blocks[block], trials[block], prob[block], corr_resp[block], sub_resp[block], sub_acc[block], resp_time[block]):
            data_as_dict.append({'block':a, 'trial':b, 'problem':c,'corr_resp':d,'sub_resp':e,'sub_acc':f, 'resp_time':g})
        print(data_as_dict)
        for iTrial in range(nTrials):
            data_writer.writerow(data_as_dict[iTrial]) 