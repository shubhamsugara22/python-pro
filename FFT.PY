from scipy.fft import fft, fftfreq
import numpy as np
from matplotlib import pyplot as plt
from scipy.io.wavfile import write

SAMPLE_RATE = 44100
DURATION = 5


def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate*duration, endpoint=False)
    frequencies = x*freq

    y = np.sin((2*np.pi)*frequencies)
    return x, y


x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
# plt.plot(x, y)
# plt.show()

_, nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
_, noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)

noise_tone = noise_tone*0.3

mixed_tone = nice_tone + noise_tone
normalized_tone = np.int16((mixed_tone/mixed_tone.max())*32767)
plt.plot(normalized_tone[:1000])
plt.show()
#write("mysinewave.wav", SAMPLE_RATE, normalized_tone)


N = SAMPLE_RATE * DURATION
yf = fft(normalized_tone)
xf = fftfreq(N, 1/SAMPLE_RATE)

plt.plot(xf, np.abs(yf))
plt.show()

points_per_freq = len(xf) / (SAMPLE_RATE/2)

target_idx = int(points_per_freq * 4000)

yf[target_idx - 1:target_idx+2] = 0

plt.plot(xf, np.abs(yf))
plt.show()
