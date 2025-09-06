# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 12:57:33 2025

@author: Meet
"""

import numpy as np
import matplotlib.pyplot as plt

from signal_ICT_meetmarvaniya_92400133063.unitary_signals import unit_step, unit_impulse, ramp_signal
from signal_ICT_meetmarvaniya_92400133063.trigonometric_signals import sine_wave, cosine_wave
from signal_ICT_meetmarvaniya_92400133063.operations import time_shift, signal_addition, signal_multiplication

def main():
    # 1. Generate and plot unit step and unit impulse signals of length 20
    n = np.arange(0, 20)
    step = unit_step(n)
    impulse = unit_impulse(n)

    # 2. Generate sine wave (amplitude=2, frequency=5 Hz, phase=0) over t=0 to 1 sec
    t = np.linspace(0, 1, 500)
    sine = sine_wave(2, 5, 0, t)

    # 3. Time shift sine wave by +5 units and plot both original and shifted
    shifted_sine = time_shift(sine, 5)
    plt.plot(t, sine, label="Original Sine Wave")
    plt.plot(t, shifted_sine, label="Shifted Sine Wave (+5 units)")
    plt.title("Time Shift on Sine Wave")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 4. Add unit step and ramp signal and plot result
    ramp = ramp_signal(n)
    added_signal = signal_addition(step, ramp)
    plt.stem(n, added_signal)
    plt.title("Addition: Unit Step + Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    # 5. Multiply sine and cosine waves of same frequency and plot the result
    cosine = cosine_wave(2, 5, 0, t)
    multiplied_signal = signal_multiplication(sine, cosine)
    plt.plot(t, multiplied_signal)
    plt.title("Multiplication: Sine x Cosine (same frequency)")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
