from psychopy import visual, monitors, event, core, logging
import os

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=14.2, distance=8) 
mon.setSizePix([1366,768])
win = visual.Window(monitor=mon) #define a window
main_dir = os.getcwd() #define a path
image_dir = os.path.join(main_dir,'images')

fix_text = visual.TextStim(win, text = '+') # define fix text
fix_text.color = 'red'
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg', 'face04.jpg', 'face05.jpg', 'face06.jpg', 'face07.jpg', 'face08.jpg', 'face09.jpg', 'face10.jpg']
my_image = visual.ImageStim(win)
nTrials = len(stims) #create a number of trials for your images
waitTimer = core.Clock()  #define a clock/timer for stimulus
waitTimer.getTime() #get time on the clock
stimTimer = core.CountdownTimer() #time the stimulus

#set durations
fix_dur = 0.2 #200 ms
image_dur = 0.1 #100 ms
text_dur = 0.2 #200 ms

refresh = 1.0/60.0
#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

fix = visual.TextStim(win, text = '+')
fix_text.color = 'red'

win.recordFrameIntervals = True #record frames
#give the monitor refresh rate plus a few ms tolerance (usually 4ms)
win.refreshThreshold = 1.0/60.0 + 0.004

# Set the log module to report warnings to the standard output window 
#(default is errors only).
logging.console.setLevel(logging.WARNING)

#=====================
#BLOCK SEQUENCE
#=====================
nBlocks=1
nTrials=4

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): #for the whole trial...
            #-draw stimulus
            if 0 <= frameN <= fix_frames: #number of frames for fixation      
                fix.draw() #draw
                win.flip() #show
                
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+image_frames):      
                fix.draw() #draw
                win.flip() #show 
                
                if frameN == (fix_frames+image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number  
                    
            #number of frames for the final text stimulus    
            if (fix_frames+image_frames) < frameN < total_frames:  
                fix.draw() #draw
                win.flip() #show  
                
                if frameN == (total_frames-1): #last frame for the text
                    print("End text frame =", frameN) #print frame number
            
    print('Overall, %i frames were dropped.' % win.nDroppedFrames)
                
win.close()                