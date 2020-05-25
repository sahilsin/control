 # Details regarding files in the directory:
 Spice.net is the spice simulation of the design provided for the closed loop system.
 Plotter.py is a python script that plots the output from spice simulation
  
 
 ## Instructions for Simulation and plotting the output.
 
 ### Setup
 --> Use the 'cd' command to move to /feedback/exercises/ee18btech11001/codes/spice 
 
 --> Ensure both Spice.net and Plotter.py exists
 
 --> Ensure ngspice and python matplotlib are installed
 
 
 ### Simulation : 
 -->Enter the following command . This simulates the 'Spice.net' file and creates a 'plot.dat' file.
 ``` 
ngspice Spice.net
```

--> Exit from ngspice cmd line using the following code . This gets you back to the present working directory.
 ``` 
exit
```

--> Enter the following command . This runs  'plotter.py'  which plots a plot of 'plot.dat' file
and save it as 'ee18btech11026_spice_result_buffer.pdf'
``` 
python plotter.py
```
