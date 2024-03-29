###############################################################################
##     Level Scheme Drawer for Nuclear Physics by Massimiliano Luciani       ##
###############################################################################

# This program is a semi-automatic drawer of nuclei's excitation level schemes 
# with the aim of simplyfing the process of building nuclear level schemes 
# figure such as those used during public talks and presentations.
# I firstly thought about this program as a tool for my PhD project but then 
# realized that it could be usefull to other researchers, so decided to publish
# it as an opensource software.

# If used properly, the program should plot a level scheme composed by those 
# levels and transitions passed within the input files. Please note that if 
# there are too many levels and transitions, the figure may appear too shrinked
# and/or compressed.

# In order to function correctly, the software needs 2 input csv files (e.g. 
# levels.csv and transitions.csv)
#
# Transitions.csv must be filled as follow 
# [Transition_energy, Starting_level, Ending_level] 
# where Transitions_energy is the real value of the transition's energy, 
# Starting_level and Ending_level are respectively the energies referring to 
# the starting and ending state involved in the transition.
#
# Levels.csv must be fille as follow [Level_energy, Spin_Parity] where the 
# former parameter is the energy value and the latter the spin-parity of the 
# excited state of interest.



import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Here below are defined all the necessary functions for the drawing part of 
# the code: drawArrow() and drawLevel(), as name suggest, just respectively 
# draw lines corresponding to gamma-ray transitions and excited levels.
#
# G.S. and (possibly) binding-level are treated differently to gave the 
# possibility to draw them wherever one wants but the functions behavior are 
# the same as drawLevel().
#
# drawScheme() is the one function called directly by the program that just 
# call recursively all the other functions to build the level scheme deciding 
# which levels and transitions should be drawn or not.

def drawArrow(_number, _delta_x, _x_max, _energy_label, _y_init, _y_final, _arrow_width, _arrow_head_width, _arrow_head_length, _fig, _subplot, _fontsize, _arrow_color):
    
    # _delta_y is the "height" of the transition's arrow
    _delta_y = _y_final-_y_init
    
    _subplot.arrow(_delta_x*_number, _y_init, 0, _delta_y, width=_arrow_width, head_width=_arrow_head_width, head_length=_arrow_head_length, 
                   head_starts_at_zero=False, length_includes_head=True, color=_arrow_color);
    
    # if condition to handle both str and float type for _energy_label
    if(type(_energy_label) == str):
        _subplot.annotate(_energy_label, (_delta_x*_number, _y_init), rotation=0, rotation_mode='anchor', 
                      xytext=(_delta_x*_number, _y_init+0.01*_y_init), fontsize=_fontsize, 
                          horizontalalignment='center', verticalalignment='bottom')
    else:
        _subplot.annotate("%.0f" % _energy_label, (_delta_x*_number, _y_init), rotation=60, rotation_mode='anchor', 
                      xytext=(_delta_x*_number, _y_init+0.01*_y_init), fontsize=_fontsize, 
                          horizontalalignment='left', verticalalignment='bottom')

    
def drawLevel(_energy, _y_labels_position, _spin_parity, _x_max, _x_fig_start, _x_fig_end, _x_right_label_distance, _x_left_label_distance, _fig, _subplot, _fontsize, _color="black"):
    
    _subplot.hlines(_energy, 0, _x_max, color=_color, linewidth=1)
    
    _subplot.annotate("%.0f" % _energy, xy=(0, _energy), xytext=(_x_fig_start,_y_labels_position), fontsize=_fontsize, 
                      horizontalalignment='right', verticalalignment='center')  
    _subplot.annotate(_spin_parity, xy=(_x_max, _energy), xytext=(_x_fig_end, _y_labels_position), fontsize=_fontsize, 
                      horizontalalignment='left', verticalalignment='center')
    
    if(_spin_parity!=""):
        _spin_label = mpatches.FancyArrowPatch((_x_max, _energy), (_x_right_label_distance, _y_labels_position),
                                       arrowstyle='-', mutation_scale=20)
        _subplot.add_patch(_spin_label)
    
    _energy_label = mpatches.FancyArrowPatch((0, _energy), (_x_left_label_distance,_y_labels_position),
                                   arrowstyle='-', mutation_scale=20)
    _subplot.add_patch(_energy_label)
    

def drawBinding(_y_position, _energy_label, _spin_parity, _fig, _subplot, _x_max, _x_fig_start, _x_fig_end, _x_right_label_distance, _x_left_label_distance, _fontsize, _color="black", _width=2):
    
    _subplot.hlines(_y_position, 0, _x_max, color=_color, linewidth=_width)
    _subplot.annotate(str(_energy_label), xy=(0, _y_position), xytext=(_x_fig_start,_y_position), fontsize=_fontsize,
                      horizontalalignment='right', verticalalignment='center')  
    _subplot.annotate(_spin_parity, xy=(_x_max, _y_position), xytext=(_x_fig_end, _y_position), fontsize=_fontsize, 
                      horizontalalignment='left', verticalalignment='center')
    
    _spin_label = mpatches.FancyArrowPatch((_x_max, _y_position), (_x_right_label_distance, _y_position),
                                       arrowstyle='-', mutation_scale=20, linewidth=_width)
    _subplot.add_patch(_spin_label)
    
    _energy_label = mpatches.FancyArrowPatch((0, _y_position), (_x_left_label_distance,_y_position),
                                   arrowstyle='-', mutation_scale=20, linewidth=_width)
    _subplot.add_patch(_energy_label)
    
    
def drawGS(_y_position, _energy_label, _spin_parity, _x_max, _x_fig_start, _x_fig_end, _x_right_label_distance, _x_left_label_distance, _fig, _subplot,_fontsize, _color="black", _width=2):
    
    _subplot.hlines(_y_position, 0, _x_max, color=_color, linewidth=_width)
    _subplot.annotate(_energy_label, xy=(0,_y_position), xytext=(_x_fig_start,_y_position), fontsize=_fontsize,
                      horizontalalignment='right', verticalalignment='center')  
    _subplot.annotate(_spin_parity, xy=(_x_max,_y_position), xytext=(_x_fig_end,_y_position), fontsize=_fontsize, 
                      horizontalalignment='left', verticalalignment='center')
    _subplot.annotate(r"42Ca", xy=(_x_max/2.,0), xytext=(_x_max/2.,-2*_fontsize), 
                      fontsize=_fontsize, horizontalalignment='center', verticalalignment='top')

    _spin_label = mpatches.FancyArrowPatch((_x_max, _y_position), (_x_right_label_distance, _y_position),
                                       arrowstyle='-', mutation_scale=20, linewidth=_width)
    _subplot.add_patch(_spin_label)
    
    _energy_label = mpatches.FancyArrowPatch((0, _y_position), (_x_left_label_distance,_y_position),
                                   arrowstyle='-', mutation_scale=20, linewidth=_width)
    _subplot.add_patch(_energy_label)


def drawLevelScheme(levels_pandas, transitions_pandas, _delta_x, _x_max, _x_fig_start, _x_fig_end, _x_right_label_distance, _x_left_label_distance, _fontsize, _start_level, _stop_level, _start_transitions, _stop_transitions, _arrow_width, _arrow_head_width, _arrow_head_length, _arrow_color, _Draw_GS):
    mainFigure, mainAx = plt.subplots()
    plt.tick_params(left = False, right = False , labelleft = False , labelbottom = False, bottom = False) 
    plt.axis('off')

    mainAx.hlines(-300, _x_fig_start, _x_fig_end, color="white")
    
    # The researcher don't need to be aware of the exact number of levels and 
    # transitions to be able to draw them all -> just put '-1' in the stop boxes in the GUI
    if(_stop_level == -1):
        _stop_level = levels_pandas.shape[0]
    else:
        pass

    if(_stop_transitions == -1):
        _stop_transitions = transitions_pandas.shape[0]
    else:
        pass

    for i in range(_start_level,_stop_level):
        drawLevel(levels_pandas.iloc[i][0],levels_pandas.iloc[i][2],str(levels_pandas.iloc[i][1]),_x_max,_x_fig_start,_x_fig_end,_x_right_label_distance,_x_left_label_distance,mainFigure,mainAx,_fontsize)
    
    # Check if G.S. need to be drawn
    if(_Draw_GS == 1):    
        drawGS(0,"G.S.","0+",_x_max,_x_fig_start,_x_fig_end,_x_right_label_distance,_x_left_label_distance,mainFigure,mainAx,_fontsize)
    else:
        pass

    for i in range(_start_transitions,_stop_transitions):
        drawArrow(i-_start_transitions,_delta_x,_x_max,transitions_pandas.iloc[i][0],transitions_pandas.iloc[i][1],transitions_pandas.iloc[i][2],
                  _arrow_width,_arrow_head_width,_arrow_head_length,mainFigure,mainAx,_fontsize,_arrow_color)
        
    plt.show()
    #plt.savefig("lvlScheme_secondary.pdf", format="pdf", bbox_inches="tight")
