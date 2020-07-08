import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
import wave
import sounddevice as sd

fs = 8000

wavetable_size = fs // 40
wavetable = np.ones(wavetable_size)

def karplus_strong_drum(wavetable, n_samples, prob):
    """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
    samples = []
    current_sample = 0
    previous_value = 0
    while len(samples) < n_samples:
        r = np.random.binomial(1, prob)
        sign = float(r == 1) * 2 - 1
        wavetable[current_sample] = sign * 0.5 * (wavetable[current_sample] + previous_value)
        samples.append(wavetable[current_sample])
        previous_value = samples[-1]
        current_sample += 1
        current_sample = current_sample % wavetable.size
    return np.array(samples)


# plt.plot(wavetable)
# print(wavetable)

sample1 = karplus_strong_drum(wavetable, 1 * fs, 0.3)
sd.play(sample1, fs, blocking=True)

print("Hello World")

plt.subplot(211)
plt.plot(sample1)
plt.subplot(212)
plt.plot(sample1)
plt.xlim(0, 1000)