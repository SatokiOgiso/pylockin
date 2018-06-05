import numpy as np

class LockInAmp:
    def __init__(self, lockInFreq, fs):
        self._lockInFreq = lockInFreq
        self._fs = fs

    def lockin(self, signal, out_format="complex"):
        reference_timestamp = np.arange(0, len(signal), 1) * 1/self._fs
        reference_signal = np.exp(- 1j * 2* np.pi * self._lockInFreq * reference_timestamp)

        complex_amplitude = np.dot(signal,  reference_signal) *2/len(signal)

        return complex_amplitude
