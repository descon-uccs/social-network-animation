# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:45:37 2022

@author: Philip Brown
"""

from animate_schelling import create_example, display_animation, load_json_file
                                


# first I'll call create_example to build the animation data:
data = create_example(n=20,num_frames=50)

# then I'll pass the data to display_animation to actually do the animation:
anim = display_animation(data,frame_ms=30,fignum=13,saveFile=None)
# note that saveFile=None, which means it won't create a gif of the animation

# another alternative lets you create your animation data, save it to disk, then load it back for animation later:

# first we have to create the data and save it as json:   
create_example(n=20,num_frames=50,fname='anim_data.json')

# now we can load it back into Python:
data_from_json = load_json_file('anim_data.json')

# now we can pass it back to display_animation just like before.
# this time, I'll create the gif but NOT display the animation in Python (by not assigning the function return to a variable):
display_animation(data,frame_ms=30,fignum=14,saveFile='anim.gif')