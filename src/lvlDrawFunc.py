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
# drawScheme() is the one function called directly by the program that just 
# call recursively all the other functions to build the level scheme deciding 
# which levels and transitions should be drawn or not.

def drawArrow(_number, _delta_x, _x_max, _energy_label,_energy_label_rotation, _y_init, _y_final, 
              _multipolarity, _arrow_color, _arrow_width, _arrow_head_width, 
              _arrow_head_length, _fig, _subplot, _fontsize,_draw_gs=1,_offset=0):
     
    # _delta_y is the "height" of the transition's arrow
    _delta_y = _y_final-_y_init
    
    if (_multipolarity != _multipolarity): # Check if _multipolairty is Nan
        _multipolarity = ""
    
    if (_arrow_color != _arrow_color): # Check if _arrow_color is Nan
        _arrow_color = "black"

    if (_draw_gs==0):
        pass
    else:
        _offset=0

    _subplot.arrow(_delta_x*_number, _y_init-_offset, 0, _delta_y, width=_arrow_width, 
                   head_width=_arrow_head_width, head_length=_arrow_head_length, 
                   head_starts_at_zero=False, length_includes_head=True, 
                   color=_arrow_color);
    
    _subplot.annotate(str("%.0f" % _energy_label) + " " + str(_multipolarity), 
                      (_delta_x*_number, _y_init-_offset), rotation=_energy_label_rotation, rotation_mode=
                      'anchor', xytext=(_delta_x*_number, _y_init+_delta_y/2.-_offset),
                      fontsize=_fontsize, horizontalalignment='center', 
                      verticalalignment='center',
                      color=_arrow_color,
                      bbox=dict(facecolor="white",edgecolor="white",pad=0.3))
    
    
def drawLevel(_energy, _y_labels_position, _spin_parity, _level_color, _x_max, 
              _x_fig_start, _x_fig_end, _x_right_label_distance, 
              _x_left_label_distance, _fig, _subplot, _fontsize,_draw_gs=1,_offset=0):

    if (_level_color != _level_color or _level_color == ""): # Checking if level color is Nan
        _level_color = "black" 
    
    if (_draw_gs==0):
        _real_energy = _energy
        _energy -=_offset
        _y_labels_position -= _offset
    else:
        _real_energy = _energy 

    _subplot.hlines(_energy, 0, _x_max, color=_level_color, linewidth=1)
    
    _subplot.annotate("%.0f" % _real_energy, xy=(0, _energy), xytext=(_x_fig_start,
                        _y_labels_position), fontsize=_fontsize, 
                        horizontalalignment='right', verticalalignment='center', color=_level_color)  
    _subplot.annotate(_spin_parity, xy=(_x_max, _energy), xytext=(_x_fig_end, 
                        _y_labels_position), fontsize=_fontsize, 
                        horizontalalignment='left', verticalalignment='center', color=_level_color)
    
    if(_spin_parity!=""):
        _spin_label = mpatches.FancyArrowPatch((_x_max, _energy), 
                        (_x_right_label_distance, _y_labels_position), 
                        arrowstyle='-', mutation_scale=20, color=_level_color)
        _subplot.add_patch(_spin_label)
    
    _energy_label = mpatches.FancyArrowPatch((0, _energy), 
                        (_x_left_label_distance,_y_labels_position),
                        arrowstyle='-', mutation_scale=20, color=_level_color)
    _subplot.add_patch(_energy_label)
    
   
def drawGS(_nucleus_name, _nucleus_name_fontsize, _y_position, _energy_label, _spin_parity, _x_max, _x_fig_start, 
           _x_fig_end, _x_right_label_distance, _x_left_label_distance, _fig, 
           _subplot,_fontsize, _color="black", _width=2):
    
    _subplot.hlines(_y_position, 0, _x_max, color=_color, linewidth=_width)
    _subplot.annotate(_energy_label, xy=(0,_y_position), xytext=(_x_fig_start,
                        _y_position), fontsize=_fontsize, 
                        horizontalalignment='right', verticalalignment='center')  
    _subplot.annotate(_spin_parity, xy=(_x_max,_y_position), xytext=(_x_fig_end
                        ,_y_position), fontsize=_fontsize, 
                        horizontalalignment='left', verticalalignment='center')
    _subplot.annotate(_nucleus_name, xy=(_x_max/2.,0),xytext=(_x_max/2.,-2*_fontsize), 
                        fontsize=_nucleus_name_fontsize, horizontalalignment='center', 
                        verticalalignment='top')

    _spin_label = mpatches.FancyArrowPatch((_x_max, _y_position),
                        (_x_right_label_distance, _y_position),arrowstyle='-', 
                        mutation_scale=20, linewidth=_width)
    _subplot.add_patch(_spin_label)
    
    _energy_label = mpatches.FancyArrowPatch((0, _y_position), 
                        (_x_left_label_distance,_y_position),arrowstyle='-', 
                        mutation_scale=20, linewidth=_width)
    _subplot.add_patch(_energy_label)


def drawLevelScheme(_nucleus_name, _nucleus_name_fontsize, _fig, _subplot, levels_pandas, transitions_pandas, _delta_x,
                    _x_max, _x_fig_start, _x_fig_end, _x_right_label_distance,
                    _x_left_label_distance, _fontsize, _start_level, 
                    _stop_level, _start_transitions, _stop_transitions, 
                    _arrow_width, _arrow_head_width, _arrow_head_length, 
                    _arrow_color, _Draw_GS, _Draw_All_Aligned, _energy_label_rotation):
    
    mainFigure = _fig
    mainAx = _subplot
    mainAx.tick_params(left = False, right = False, labelleft = False, 
                       labelbottom = False, bottom = False) 
    mainAx.axis('off')
    mainAx.hlines(-300, _x_fig_start, _x_fig_end, color="white")
    
    # The researcher don't need to be aware of the exact number of levels and 
    # transitions to be able to draw them all -> just put '-1' in the stop 
    # boxes in the GUI
    if(_stop_level == -1):
        _stop_level = levels_pandas.shape[0]
    else:
        pass

    if(_stop_transitions == -1):
        _stop_transitions = transitions_pandas.shape[0]
    else:
        pass

    for i in range(_start_level,_stop_level):
        drawLevel(levels_pandas.iloc[i]['Level energy'],
                  levels_pandas.iloc[i]['Energy Label Position'],
                  str(levels_pandas.iloc[i]['Spin-Parity']),
                  levels_pandas.iloc[i]['Level color'],
                  _x_max,_x_fig_start,_x_fig_end,_x_right_label_distance,
                  _x_left_label_distance,mainFigure,mainAx,_fontsize,_Draw_GS,levels_pandas.iloc[_start_level]['Level energy'])
    
    # Check if G.S. need to be drawn
    if(_Draw_GS == 1):    
        drawGS(_nucleus_name, _nucleus_name_fontsize, 0,"G.S.","0+",_x_max,_x_fig_start,_x_fig_end,
               _x_right_label_distance,_x_left_label_distance,mainFigure,
               mainAx,_fontsize)
    else:
        pass

    if(_Draw_All_Aligned == 0):
        for i in range(_start_transitions,_stop_transitions):
            drawArrow(i-_start_transitions+0.5,_delta_x,_x_max,
                      transitions_pandas.iloc[i]['Transition energy'],
                      _energy_label_rotation,
                      transitions_pandas.iloc[i]['Initial level'],
                      transitions_pandas.iloc[i]['Final level'],
                      transitions_pandas.iloc[i]['Multipolarity'],
                      transitions_pandas.iloc[i]['Transition color'],
                      _arrow_width,_arrow_head_width,_arrow_head_length,
                      mainFigure,mainAx,_fontsize,_Draw_GS,levels_pandas.iloc[_start_level]['Level energy'])
    
    else:
        for i in range(_start_transitions,_stop_transitions):
            drawArrow(1,_delta_x,_x_max,
                      transitions_pandas.iloc[i]['Transition energy'],
                      _energy_label_rotation,
                      transitions_pandas.iloc[i]['Initial level'],
                      transitions_pandas.iloc[i]['Final level'],
                      transitions_pandas.iloc[i]['Multipolarity'],
                      transitions_pandas.iloc[i]['Transition color'],
                      _arrow_width,_arrow_head_width,_arrow_head_length,
                      mainFigure,mainAx,_fontsize,_Draw_GS,levels_pandas.iloc[_start_level]['Level energy'])
