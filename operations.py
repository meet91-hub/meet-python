# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 12:49:09 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

def time_shift(signal, k):

    shifted = np.roll(signal, k)
    
    # Plot both original and shifted signals for comparison
    plt.figure(figsize=(10, 4))
    plt.plot(signal, label="Original")
    plt.plot(shifted, label=f"Shifted by {k}")
    plt.title("Time Shift Operation")
    plt.xlabel("n")  # Sample index
    plt.ylabel("Amplitude")
    plt.legend()  
    plt.grid(True)  
    plt.show()
    
    return shifted

def time_scale(signal, k):
    
    # Simple down-sampling implementation (for k > 1)
    # For k < 1 (expansion), this implementation doesn't handle fractional scaling
    if k <= 0:
        raise ValueError("Scaling factor k must be positive")
    
    scaled = signal[::k]  # Take every k-th sample
    
    x_axis = np.arange(0, len(scaled) * k, k)
    
    # Plot both original and scaled signals
    plt.figure(figsize=(10, 4))
    plt.plot(signal, label="Original")
    plt.plot(x_axis, scaled, label=f"Scaled by {k}")
    plt.title("Time Scaling Operation")
    plt.xlabel("n")  # Sample index
    plt.ylabel("Amplitude")
    plt.legend()  
    plt.grid(True)  # Add grid for better readability
    plt.show()
    
    return scaled

def signal_addition(signal1, signal2):
    
    # Check if signals have the same length
    if len(signal1) != len(signal2):
        raise ValueError("Signals must be of the same length for addition")
    
    # Element-wise addition of two signals
    result = signal1 + signal2
    
    # Plot all three signals: the two inputs and their sum
    plt.figure(figsize=(10, 4))
    plt.plot(signal1, label="Signal 1")
    plt.plot(signal2, label="Signal 2")
    plt.plot(result, label="Added Signal")
    plt.title("Signal Addition")
    plt.xlabel("n")  # Sample index
    plt.ylabel("Amplitude")
    plt.legend()  # Show legend to identify each signal
    plt.grid(True)  # Add grid for better readability
    plt.show()
    
    return result

def signal_multiplication(signal1, signal2):
   
    # Check if signals have the same length
    if len(signal1) != len(signal2):
        raise ValueError("Signals must be of the same length for multiplication")
    
    # Element-wise multiplication of two signals
    result = signal1 * signal2
    
    # Plot all three signals: the two inputs and their product
    plt.figure(figsize=(10, 4))
    plt.plot(signal1, label="Signal 1")
    plt.plot(signal2, label="Signal 2")
    plt.plot(result, label="Multiplied Signal")
    plt.title("Signal Multiplication")
    plt.xlabel("n")  # Sample index
    plt.ylabel("Amplitude")
    plt.legend()  # Show legend to identify each signal
    plt.grid(True)  # Add grid for better readability
    plt.show()
    
    return result

# Example usage:
if __name__ == "__main__":
    # Create a sample signal
    n = np.arange(0, 50)
    original_signal = np.sin(2 * np.pi * n / 20)
    
    # Test time shift
    shifted = time_shift(original_signal, 10)
    
    # Test time scaling
    scaled = time_scale(original_signal, 2)
    
    # Create another signal for addition and multiplication
    signal2 = 0.5 * np.cos(2 * np.pi * n / 15)
    
    # Test signal addition
    added = signal_addition(original_signal, signal2)
    
    # Test signal multiplication
    multiplied = signal_multiplication(original_signal, signal2)