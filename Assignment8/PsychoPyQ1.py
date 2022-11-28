from psychopy import event, visual, monitors, core

mon = monitors.Monitor('myMonitor', width=14.2, distance=8) 
mon.setSizePix([1366,768])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])
2
nTrials=10
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')

sub_resp = []

for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print("keys that were pressed", keys) #which keys were pressed?
    
    
    if keys:
        sub_resp = keys[0] #only take first response
        
    print("response that was counted", sub_resp)    
    
win.close()