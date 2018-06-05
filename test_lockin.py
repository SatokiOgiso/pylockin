
import unittest
import numpy as np
from lockin import LockInAmp

class TestLockInAmp(unittest.TestCase):
    def test_sin(self):
        #generate test signal
        dt = 0.001
        timewindow = 1
        fs = 1/dt
        f1 = 100
        la = LockInAmp(f1, fs)

        time = np.arange(0, timewindow, dt)
        signal = np.sin(2*np.pi*f1*time)

        #apply lock in amp
        res = la.lockin(signal)

        self.assertAlmostEqual(np.abs(res), 1)
        self.assertAlmostEqual(np.angle(res), - np.pi/2)

    def test_cos(self):
        #generate test signal
        dt = 0.001
        timewindow = 1
        fs = 1/dt
        f1 = 100
        la = LockInAmp(f1, fs)

        time = np.arange(0, timewindow, dt)
        signal = np.cos(2*np.pi*f1*time)

        #apply lock in amp
        res = la.lockin(signal)

        self.assertAlmostEqual(np.abs(res), 1)
        self.assertAlmostEqual(np.angle(res), 0)

    def test_cos_phased_pi4(self):
        #generate test signal
        dt = 0.001
        timewindow = 1
        fs = 1/dt
        f1 = 100
        la = LockInAmp(f1, fs)

        time = np.arange(0, timewindow, dt)
        signal = np.cos(2*np.pi*f1*time + np.pi/4)

        #apply lock in amp
        res = la.lockin(signal)

        self.assertAlmostEqual(np.abs(res), 1)
        self.assertAlmostEqual(np.angle(res), np.pi/4)

    def test_cos_phased_pi2(self):
        #generate test signal
        dt = 0.001
        timewindow = 1
        fs = 1/dt
        f1 = 100
        la = LockInAmp(f1, fs)

        time = np.arange(0, timewindow, dt)
        signal = np.cos(2*np.pi*f1*time - np.pi/2)

        #apply lock in amp
        res = la.lockin(signal)

        self.assertAlmostEqual(np.abs(res), 1)
        self.assertAlmostEqual(np.angle(res), - np.pi/2)


    def test_cos_amplitude(self):
        #generate test signal
        dt = 0.001
        timewindow = 1
        fs = 1/dt
        f1 = 100
        la = LockInAmp(f1, fs)
        amplitude = 2

        time = np.arange(0, timewindow, dt)
        signal = amplitude * np.cos(2*np.pi*f1*time - np.pi/2)

        #apply lock in amp
        res = la.lockin(signal)

        self.assertAlmostEqual(np.abs(res), amplitude)
        self.assertAlmostEqual(np.angle(res), - np.pi/2)


    def test_cos_with_noise(self):
        #generate test signal
        dt = 0.001
        timewindow = 1
        fs = 1/dt
        f1 = 100
        la = LockInAmp(f1, fs)

        time = np.arange(0, timewindow, dt)
        signal = np.cos(2*np.pi*f1*time)

        np.random.seed(0)
        signal = signal + np.random.randn(len(signal))

        #apply lock in amp
        res = la.lockin(signal)

        self.assertAlmostEqual(np.abs(res), 1, delta=0.05)
        self.assertAlmostEqual(np.angle(res), 0, delta=0.05)

if __name__ == "__main__":
    unittest.main()
