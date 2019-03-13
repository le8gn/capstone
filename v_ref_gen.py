# This function generates the velocity profile for MPC. The velocity profile is an
# array of velocity values, which illustrates the change of velocity from current
# one to that of front car. The size of array is the horizon of MPC.

# The inputs of this function are vf (the velocity of front car), ve (the velocity 
# of ego car), and d (the distance between two cars). It will return velocity 
# profile only in safe conditions (distance is greater than safe distance, and 
# deacceleration is in the max deacceleration boundary). Otherwise it will publish
# a True boolean message as a ROS node called "takeover_msg" to a ROS topic called 
# "takeover_bool".

import numpy as np

def v_ref_gen(vf,ve,d):
    miu = 0.8; # The coefficient of friction
    v_ref = ev*np.ones(N); # Initialize the default velocity profile as all ego velocity
    deacc_max = -2.0; # The max deacceleration 

    d_brake = abs((ve**2-vf**2)/(2*deacc_max)); # The braking distance for max deacceleration
    d_safe = d_brake + abs(ve-vf)*1; # The safe distance is longer than assumed 
                                     # braking distance, adding one second to add
                                     # more safety consideration
    if (vf < ve):
        v_ref[0] = ve;
        v_ref[N-1] = vf;
        
        if d >= d_safe:

            for i in range(1,N-1):
                v_ref[i] = v_ref[i-1]-(ve-vf)/(N-2); # Do linear deacceleration
                                                     # to be the front car velocity
                    
        else: # Send message to driver take-over
            pass #!!!Insert Publisher (GO COMMAND) Here!!!
                
    else:
        pass
    
    return v_ref

