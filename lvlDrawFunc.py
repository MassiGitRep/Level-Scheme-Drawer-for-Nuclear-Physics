import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

################### Defining Functions ##############################################

def drawArrow(_number, _delta_x, _x_max, _energy_label, _y_init, _y_final, _arrow_width, _arrow_head_width, _arrow_head_length, _fig, _subplot, _fontsize, _arrow_color):
    
    _delta_y = _y_final-_y_init
    
    _subplot.arrow(_delta_x*_number, _y_init, 0, _delta_y, width=_arrow_width, head_width=_arrow_head_width, head_length=_arrow_head_length, 
                   head_starts_at_zero=False, length_includes_head=True, color=_arrow_color);
    
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
    
    if(_Draw_GS == 1):    
        drawGS(0,"G.S.","0+",_x_max,_x_fig_start,_x_fig_end,_x_right_label_distance,_x_left_label_distance,mainFigure,mainAx,_fontsize)
    else:
        pass

    for i in range(_start_transitions,_stop_transitions):
        drawArrow(i-_start_transitions,_delta_x,_x_max,transitions_pandas.iloc[i][0],transitions_pandas.iloc[i][1],transitions_pandas.iloc[i][2],
                  _arrow_width,_arrow_head_width,_arrow_head_length,mainFigure,mainAx,_fontsize,_arrow_color)
        
    plt.show()
    #plt.savefig("lvlScheme_secondary.pdf", format="pdf", bbox_inches="tight")
