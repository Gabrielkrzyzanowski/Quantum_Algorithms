#!/usr/bin/env python3  

"""
A Python scrip that...

Parameters
---------


Output
--------- 

""" 

import argparse 
import numpy as np 

class VQE_Class: 
    def __init__(self, 
                 Argument: float = None
                 )-> None: 
        self.argument=Argument


if __name__=='__main__': 
    #Run the algorithm 

    parser = argparse.ArgumentParser(description= 'Script to test the routines using VQE Algorithm to solve TSP problems.') 

    #Positional Arguments
    #parser.add_argument('pressure_set_point', type=float, help='The pressure setpoint (in GPa) sent to the PID')
    #parser.add_argument('file_name', type=str, help='The name of the file where the data will be saved ')  

    args=parser.parse_args() 
    
    

