import subprocess
import shlex
import control
sys = control.tf(25,[1, 6, 5, 0])
gainMargin, phaseMargin, PhaseCrossover, GainCrossover = control.margin(sys)
print('Gain Margin: ',gainMargin)
print('Phase Margin: ',phaseMargin)
print('Phase Crossover Frequency',PhaseCrossover)
print('Gain Crossover Frequency',GainCrossover)
