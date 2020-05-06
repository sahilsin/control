import subprocess
import shlex
import matplotlib.pyplot as plt
from scipy import signal
from scipy.interpolate import interp1d

#T.F. = k(s+2)/(s^4 + 12s^3 + 47s^2 + (60+k)s + 2k)
k=69.2
sys = signal.lti([k,2*k], [1,12,47,60+k, 2*k])
t,res = signal.step(sys)



peak_os = max(res)
steady_state = 1
over_shoot_percent = ((peak_os-steady_state)/steady_state)*100

#Finding tpeak
#Using interpolation
t_as_fn_of_res = interp1d(t, res)
tpeak = t_as_fn_of_res(peak_os)


plt.plot(t,res)
plt.plot(tpeak,peak_os,'o', label='_nolegend_')
plt.text(tpeak,peak_os,'({}, {})'.format(tpeak.round(2),peak_os.round(2)))
plt.axhline(y = 1,xmin=0,xmax= 1,color = 'k',linestyle='dashed')
plt.xlabel('Time')
plt.grid()

print("Steady State Value=",round(steady_state,2))
print("Peak Value = ",peak_os.round(2))
print("Percent Overshoot=",over_shoot_percent.round(2))


plt.savefig('./figs/ee18btech11038/ee18btech11038_os.pdf')
plt.savefig('./figs/ee18btech11038/ee18btech11038_os.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11038/ee18btech11038_os.pdf"))

