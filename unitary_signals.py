# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 12:44:21 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    """Generate a unit step signal"""
    # Create the unit step signal: 1 for n >= 0, 0 otherwise
    signal = np.array([1 if i >= 0 else 0 for i in n])
    
    # Plot the signal using stem plot
    plt.stem(n, signal)
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    
    return signal

def unit_impulse(n):
    """Generate a unit impulse signal"""
    # Create the unit impulse signal: 1 only at n = 0, 0 elsewhere
    signal = np.array([1 if i == 0 else 0 for i in n])
    
    # Plot the signal
    plt.stem(n, signal)
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    
    return signal

def ramp_signal(n):
    """Generate a ramp signal"""
    # Create the ramp signal: n for n >= 0, 0 otherwise
    signal = np.array([i if i >= 0 else 0 for i in n])
    
    # Plot the signal
    plt.stem(n, signal)
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    
    return signal  # Added missing return statement

# Example usage:
if __name__ == "__main__":
    # Create a time axis from -5 to 5
    n = np.arange(-5, 6)
    
    # Generate signals
    step = unit_step(n)
    impulse = unit_impulse(n)
    ramp = ramp_signal(n)