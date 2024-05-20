# Nuclear Physics Excitation Level Scheme Drawer

#### This is my very first project. It is an elementary Python program intended to help physicists draw nuclear excitation-level schemes.
\
\
To call the program move to **src** dir and use **$ python3 draw.py**. This will open a GUI that allows the user to upload the **.csv** files containing the level scheme info and to set everything before drawing.
If the upload went well, then the first two fields will become green, otherwise, they will be highlighted in red.


The program requires two inputs **.csv** files:

- The first one is the **transitions** file that needs to be filled as follow *(Transition_energy, Starting_level, Ending_level, Spin_parity, Color)*
- The second one is the **levels** file that needs to be filled as follow *(Level_energy, Spin_Parity, Color)*
    
Problems to be solved:

- I found out that the levels file must contain at least two lines otherwise there will be a problem when loading the file.
   *See Transitions.csv and Levels.csv as examples*
- If matplotlib canvas is closed (pressing X button) after resizing the figure (using the 'Configure Subplots' button) TKinter can't invoke destroy Method and an error is raised. 

GUI preview
![GUI preview](https://github.com/MassiGitRep/Level-Scheme-Drawer-for-Nuclear-Physics/blob/main/images/GUI_new.png)

\
\
Any suggestion is warmly welcomed!

Cheers,
\
Max
