# Nuclear Physics Excitation Level Scheme Drawer

#### This is my very first project. It is an elementary Python program intended to help physicists draw nuclear excitation-level schemes.
\
\
The program requires two inputs **.csv** files:

- The first one is the **transitions** file that needs to be filled as follow *(Transition_energy, Starting_level, Ending_level, Spin_parity, Color)*
- The second one is the **levels** file that needs to be filled as follow *(Level_energy, Spin_Parity, Color)*
    
Problems to be solved:

- I found out that the levels file must contain at least two lines otherwise there will be a probelm when loading the file.
   *See Transitions.csv and Levels.csv as examples*
- If matplotlib canvas is closed (pressing X button) after resizing the figure (using the 'Configure Subplots' button) TKinter can't invoke destroy Method and an error is raised. 

\
\
Any suggestion is warmly welcomed!

Cheers,
Max
