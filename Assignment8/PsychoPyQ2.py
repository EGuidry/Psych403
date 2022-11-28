from psychopy import event, visual, monitors, core

mon = monitors.Monitor('myMonitor', width=14.2, distance=8) 
mon.setSizePix([1366,768])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=10
my_text=visual.TextStim(win)
fix_text=visual.TextStim(win, text='+')
fix_text.color = 'red'

sub_resp = []

#-draw start trial text
startr_msg = "Start of Trials"
startr_text = visual.TextStim(win, text = startr_msg)
startr_text.color = 'green'
startr_text.draw()
#-flip window
win.flip() 
#-wait time (stimulus duration)
core.wait(1)

for trial in range(nTrials):
    event.clearEvents() #clear events HERE  
    my_text.text = "Trial %i" %trial #insert integer into the string with %i
    my_text.color = 'chartreuse'
    fix_text.draw()
    win.flip()
    core.wait(2)
    
    my_text.draw()
    win.flip()
    core.wait(1)

    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    print("keys that were pressed", keys) #which keys were pressed?
  
    if keys:
        sub_resp = keys[0] #only take first response - Code for question 1
        
    print("response that was counted", sub_resp)    
    
win.close()