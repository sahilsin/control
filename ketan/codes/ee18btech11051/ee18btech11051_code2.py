import subprocess
import shlex
import control
import numpy as np
alpha = 5
t = 1/(5*2.6)

#    Original T.F.
s1 = control.tf([25], [1, 6, 5, 0])

#    Single Pass Compensated T.F.
s2 = control.tf( np.polymul([25], [alpha*t, 1]), np.polymul([1, 6, 5, 0], [t, 1]) )

#    Double Pass Compensated T.F.
s3 = control.tf(25* np.polymul([alpha*t, 1], [alpha*t, 1]), np.polymul([t, 1], np.polymul([1, 6, 5, 0], [t, 1])))

gainMargin, phaseMargin, PhaseCrossover, GainCrossover = control.margin(s3)
print('Gain Margin: ',gainMargin)
print('Phase Margin: ',phaseMargin)
print('Phase Crossover Frequency',PhaseCrossover)
print('Gain Crossover Frequency',GainCrossover)
