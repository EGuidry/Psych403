from psychopy import visual, monitors, event, core
import os
#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=14.2, distance=8) 
mon.setSizePix([1366,768])
win = visual.Window(monitor=mon) #define a window
main_dir = os.getcwd()
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text = '+')
fix_text.color = 'red'
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
my_image = visual.ImageStim(win)
nTrials = 4 #create a number of trials for your images

for trial in range(nTrials): #loop through trials
    
    my_image.image = os.path.join(image_dir,stims[trial])
  
#=====================
    #START TRIAL
    #===================== 
    #-draw fixation
    fix_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(.5)
        
    #-draw image
    my_image.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(.5)
        
    #-draw end trial text
    endtr_msg = "End of trial"
    endtr_text = visual.TextStim(win, text = endtr_msg)
    endtr_text.color = 'blueviolet'
    endtr_text.draw()
    #-flip window
    win.flip() 
    #-wait time (stimulus duration)
    core.wait(.5)

#======================
# END OF EXPERIMENT
#======================
win.close() #close the window after trials have looped 