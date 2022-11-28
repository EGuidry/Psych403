## PsychoPy Keypress Exercises
- What happens if you put event.ClearEvents within the trial loop instead of outside the trial loop? See [PsychoPyQ1](https://github.com/EGuidry/Psych403/blob/main/Assignment8/PsychoPyQ1.py)
    - Answer: When event.clear is inside the trail loop, it clears what is collected within the loop. It needs to be way before the getKeys 
      and.draw(), because it wouldn't make any sense to clear eveything after you just collected it.
- What happens if you unindent the "if keys:" line? See [PsyshoPyQ2](https://github.com/EGuidry/Psych403/blob/main/Assignment8/PsychoPyQ2.py)
    - If you unident keys, then that section of the code would only happen after all the responses, but what is needed is for that section       to happen after each response, therefore it must remain in the loop. Especially if you are using a counter in the "if keys" section.

## Psychotoolbox Keypress Exercises
Was told to ignore this section.

## Recording Data Exercises
See [ReadingExercises](https://github.com/EGuidry/Psych403/blob/main/Assignment8/ReadingExercises.py)

## Save CSV Exercises
See [SaveExercise](https://github.com/EGuidry/Psych403/blob/main/Assignment8/SaveExercise.py)

## JSON Exercises
Could not get JSON to work.
