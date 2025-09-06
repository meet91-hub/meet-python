# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 12:46:51 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A, f, phi, t):

    # Generate sine wave using the formula: A * sin(2πft + φ)
    signal = A * np.sin(2 * np.pi * f * t + phi)
    
    # Plot the generated sine wave
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title("Sine Wave")  # Set plot title
    plt.xlabel("Time (s)")  # Label x-axis
    plt.ylabel("Amplitude")  # Label y-axis
    plt.grid(True)  # Enable grid for better readability
    plt.show()  # Display the plot
    
    return signal  # Return the generated signal array

def cosine_wave(A, f, phi, t):

    # Generate cosine wave using the formula: A * cos(2πft + φ)
    signal = A * np.cos(2 * np.pi * f * t + phi)
    
    # Plot the generated cosine wave
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title("Cosine Wave")  # Set plot title
    plt.xlabel("Time (s)")  # Label x-axis
    plt.ylabel("Amplitude")  # Label y-axis
    plt.grid(True)  # Enable grid for better readability
    plt.show()  # Display the plot
    
    return signal  # Return the generated signal array

def exponential_signal(A, a, t):

    # Generate exponential signal using the formula: A * e^(a*t)
    signal = A * np.exp(a * t)
    
    # Plot the generated exponential signal
    plt.figure(figsize=(10, 4))
    plt.plot(t, signal)
    plt.title("Exponential Signal")  # Set plot title
    plt.xlabel("Time (s)")  # Label x-axis
    plt.ylabel("Amplitude")  # Label y-axis
    plt.grid(True)  # Enable grid for better readability
    plt.show()  # Display the plot
    
    return signal  # Return the generated signal array

# Example usage:
if __name__ == "__main__":
    # Create a time array from 0 to 1 second with 1000 points
    t = np.linspace(0, 1, 1000)
    
    # Generate a 5Hz sine wave with amplitude 1 and no phase shift
    sine = sine_wave(A=1, f=5, phi=0, t=t)
    
    # Generate a 3Hz cosine wave with amplitude 1.5 and π/4 phase shift
    cosine = cosine_wave(A=1.5, f=3, phi=np.pi/4, t=t)
    
    # Generate an exponential decay signal
    exp_decay = exponential_signal(A=1, a=-2, t=t)
    
    # Generate an exponential growth signal
    exp_growth = exponential_signal(A=1, a=2, t=t)