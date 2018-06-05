# pylockin
Tiny class for lockin in python

## Dependency
* numpy

## Usage


```
#generate test signal
dt = 0.001
timewindow = 1
fs = 1/dt
f1 = 100
la = LockInAmp(f1, fs)
amplitude = 2

time = np.arange(0, timewindow, dt)
signal = amplitude * np.cos(2*np.pi*f1*time + np.pi)

#apply lock in amp
res = la.lockin(signal)

print(np.abs(res))
print(np.angle(res))
```

The output of the script above will be

```
0
3.14159265
```

You may get more samples in unittest.

## Unittest

Execute following command in the directory of this repo.

```
python -m unittest test_lockin.py
```
