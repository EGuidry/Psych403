#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
from datetime import datetime

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-Create a dialogue box that will collect current participant number, age, gender, 
    #handedness
# Setup the dictionary for the gui
exp_info = {'subject_nr':0, 
            'age':0, 
            'handedness':('right','left','ambi'), 
            'gender':('male','female','other','prefer not to say'),
            'session': 1}

print(exp_info)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg = gui.DlgFromDict(dictionary=exp_info,
                        title='subject info',
                        fixed=['session'],
                        order=['session', 'subject_nr', 'age', 'gender', 'handedness'])
# Make sure subject data is entered correctly
if exp_info['subject_nr'] ==0: #nothing entered
    # Create another dialog box (not from a dictionary because we're just showing an error message)
    err_dlg = gui.Dlg(title='error message') #give the dlg a title
    err_dlg.addText('Enter a valid subject number!') #create an error message
    err_dlg.show() #show the dlg
    core.quit() #quit the experiment
    
# Make sure subject can consent to taking part in the experiment        
if exp_info['age'] < 18:
    err_dlg = gui.Dlg(title='error message')
    err_dlg.addText('%d year olds cannot give consent!' % (exp_info['age']))
    err_dlg.show()
    core.quit()

# What time is it right now?
date = datetime.now()
print(date)
exp_info['date'] = str(date.hour) + '-' + str(date.day) + '-' + str(date.month) + '-' + str(date.year)
print(exp_info['date'])

# Create a unique filename for the data
filename = str( exp_info['subject_nr']) + '_' + exp_info['date'] + '.csv'

main_dir = os.getcwd() 
sub_dir = os.path.join(main_dir,'sub_info',filename)

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width=14.2, distance=8) 
mon.setSizePix([1366,768])
mon.save()

thisSize = mon.getSizePix()
thisWidth = thisSize[0]
thisHeight = thisSize[1]

#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, fullscr = True)

#=====================
#PRESENT STIMULI
#=====================

fix_text = visual.TextStim(win,text='+')
fix_text.color = 'red' #color space allows the creator to change the colours of a stimulus and you can define colours by name.
my_image = visual.ImageStim(win, units='pix', size=(200,200))
# Units allow the creator to specify which units to manipulate measurements such as height to define the window size, or in this case pixes of the image.
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']

#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_msg = 'Welcome to my experiment!'
#-define experiment start text using psychopy functions
start_text = visual.TextStim(win, text = start_msg)
start_text.color = 'cadetblue'
start_text.draw()
win.flip() 
event.waitKeys() 
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
nBlocks = 2
#-present block start message
block_msg = 'Press any key to continue to the next block'

#-define block (start)/end text using psychopy functions
block_text = visual.TextStim(win, text = block_msg)
block_text.color = 'burlywood'

#-for loop for nBlocks *
for block in range(nBlocks):
    block_text.draw()
    win.flip() 
    event.waitKeys() 
    #-randomize order of trials here *
    np.random.shuffle(stims)
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
nTrials = 4
#-for loop for nTrials *
vertMult = [1,1,-1,-1]
horizMult = [-1,1,-1,1]

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.pos = (horizMult[trial]*thisWidth/4, vertMult[trial]*thisHeight/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()
        
        #-set stimuli and stimulus properties for the current trial
        

        #=====================
        #START TRIAL
        #=====================   
        #-draw fixation
        #-flip window
        #-wait time (stimulus duration)
        
        #-draw image
        #-flip window
        #-wait time (stimulus duration)
        
    #-draw end trial text
    endtr_msg = "End of trial"
    #-define stimuli using psychopy functions
    endtr_text = visual.TextStim(win, text = endtr_msg)
    endtr_text.color = 'blueviolet'
    endtr_text.draw()
    #-flip window
    win.flip() 
    #-wait time (stimulus duration)
    event.waitKeys() 
        
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()