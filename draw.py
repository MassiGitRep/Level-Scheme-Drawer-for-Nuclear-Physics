import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from lvlDrawFunc import *
        
 
class SetParameters(tk.Tk):

    def __init__(self):
    
        super().__init__()
        self.title("Nuclear Physics Level Scheme")
        self.geometry("600x500")
        
        self.Upload_button = tk.Button(text="Upload", command=self.UploadFiles)
        self.Draw_button = tk.Button(text="Draw", command=self.Draw)

        self.Draw_GS = tk.BooleanVar(self, 1)
        self.Draw_GS_button = tk.Checkbutton(self, text="Draw G.S.", variable=self.Draw_GS, onvalue=1, offvalue=0)
        self.Uploaded_flag = tk.BooleanVar(self,0)
        self.XMax = tk.DoubleVar(self,5)
        self.Width_const = tk.DoubleVar(self,0.05)

        self.Transition_file = tk.StringVar(self,"../files/transitions.csv")
        self.Level_file = tk.StringVar(self,"../files/levels.csv")
        self.Arrow_width = tk.DoubleVar(self,0.001)
        self.Arrow_head_width = tk.DoubleVar(self,0.005*self.XMax.get())
        self.Arrow_head_length = tk.DoubleVar(self,40)
        self.Min_vert_label_dist = tk.DoubleVar(self,80)
        self.Fontsize = tk.IntVar(self,16)
        self.Arrow_color = tk.StringVar(self,"black")
        self.Start_level = tk.IntVar(self,0)
        self.Stop_level = tk.IntVar(self,-1)
        self.Start_transition = tk.IntVar(self,0)
        self.Stop_transition = tk.IntVar(self,-1)
        self.DeltaX = tk.DoubleVar(self)

        self.create_widget()

        self.Transition_file.trace_add("write", self.PrintUpdatedValue)
        self.Level_file.trace_add("write", self.PrintUpdatedValue)
        self.Arrow_width.trace_add("write", self.PrintUpdatedValue)
        self.Arrow_head_width.trace_add("write", self.PrintUpdatedValue)
        self.Arrow_head_length.trace_add("write", self.PrintUpdatedValue)
        self.Min_vert_label_dist.trace_add("write", self.PrintUpdatedValue)
        self.Fontsize.trace_add("write", self.PrintUpdatedValue)
        self.Arrow_color.trace_add("write", self.PrintUpdatedValue)
        self.Start_level.trace_add("write", self.PrintUpdatedValue)
        self.Stop_level.trace_add("write", self.PrintUpdatedValue)
        self.Start_transition.trace_add("write", self.PrintUpdatedValue)
        self.Stop_transition.trace_add("write", self.PrintUpdatedValue)

    def create_widget(self):

        self.Transition_file_label = tk.Label(self, text="Transition Filename: ")
        self.Level_file_label = tk.Label(self, text="Level Filename: ")
        self.Arrow_width_label = tk.Label(self, text="Arrow Width: ")
        self.Arrow_head_width_label = tk.Label(self, text="Arrow Head Width: ")
        self.Arrow_head_length_label = tk.Label(self, text="Arrow Head Length: ")
        self.Min_vert_label_dist_label = tk.Label(self, text="Minimum Vertical Level Separation: ")
        self.Fontsize_label = tk.Label(self, text="Fontsize: ")
        self.Arrow_color_label = tk.Label(self, text="Arrow Color: ")
        self.Start_level_label = tk.Label(self, text="Start Level: ")
        self.Stop_level_label = tk.Label(self, text="Stop Level: ")
        self.Start_transition_label = tk.Label(self, text="Start Transition: ")
        self.Stop_transition_label = tk.Label(self, text="Stop Transition: ")

        self.Transition_file_entry = tk.Entry(self, textvariable=self.Transition_file)
        self.Level_file_entry = tk.Entry(self, textvariable=self.Level_file)
        self.Arrow_width_entry = tk.Entry(self, textvariable=self.Arrow_width)
        self.Arrow_head_width_entry = tk.Entry(self, textvariable=self.Arrow_head_width)
        self.Arrow_head_length_entry = tk.Entry(self, textvariable=self.Arrow_head_length)
        self.Min_vert_label_dist_entry = tk.Entry(self, textvariable=self.Min_vert_label_dist)
        self.Fontsize_entry = tk.Entry(self, textvariable=self.Fontsize)
        self.Arrow_color_entry = tk.Entry(self, textvariable=self.Arrow_color)
        self.Start_level_entry = tk.Entry(self, textvariable=self.Start_level)
        self.Stop_level_entry = tk.Entry(self, textvariable=self.Stop_level)
        self.Start_transition_entry = tk.Entry(self, textvariable=self.Start_transition)
        self.Stop_transition_entry = tk.Entry(self, textvariable=self.Stop_transition)

        self.Transition_file_label.grid(row=0, column=0, padx=5, pady=5)
        self.Level_file_label.grid(row=1, column=0, padx=5, pady=5)
        self.Arrow_width_label.grid(row=6, column=0, padx=5, pady=5)
        self.Arrow_head_width_label.grid(row=7, column=0, padx=5, pady=5)
        self.Arrow_head_length_label.grid(row=8, column=0, padx=5, pady=5)
        self.Min_vert_label_dist_label.grid(row=9, column=0, padx=5, pady=5)
        self.Fontsize_label.grid(row=10, column=0, padx=5, pady=5)
        self.Arrow_color_label.grid(row=11, column=0, padx=5, pady=5)
        self.Start_level_label.grid(row=12, column=0, padx=5, pady=5)
        self.Stop_level_label.grid(row=13, column=0, padx=5, pady=5)
        self.Start_transition_label.grid(row=14, column=0, padx=5, pady=5)
        self.Stop_transition_label.grid(row=15, column=0, padx=5, pady=5)

        self.Transition_file_entry.grid(row=0, column=1, padx=5, pady=5)
        self.Level_file_entry.grid(row=1, column=1, padx=5, pady=5)
        self.Arrow_width_entry.grid(row=6, column=1, padx=5, pady=5)
        self.Arrow_head_width_entry.grid(row=7, column=1, padx=5, pady=5)
        self.Arrow_head_length_entry.grid(row=8, column=1, padx=5, pady=5)
        self.Min_vert_label_dist_entry.grid(row=9, column=1, padx=5, pady=5)
        self.Fontsize_entry.grid(row=10, column=1, padx=5, pady=5)
        self.Arrow_color_entry.grid(row=11, column=1, padx=5, pady=5)
        self.Start_level_entry.grid(row=12, column=1, padx=5, pady=5)
        self.Stop_level_entry.grid(row=13, column=1, padx=5, pady=5)
        self.Start_transition_entry.grid(row=14, column=1, padx=5, pady=5)
        self.Stop_transition_entry.grid(row=15, column=1, padx=5, pady=5)

        self.Upload_button.grid(row=0, column=2, padx=50, pady=5)
        self.Draw_button.grid(row=8, column=2, padx=50, pady=5)
        self.Draw_GS_button.grid(row=16, column=0, padx=5, pady=5)
    
    def PrintUpdatedValue(self, *args):
        pass
        
    
    def UploadFiles(self, *args):
        try:
            global levels_pandas 
            global transitions_pandas
            global _number_of_transitions
            global _number_of_levels 
            global _x_fig_start                                            
            global _x_fig_end                                      
            global _x_left_label_distance                                   
            global _x_right_label_distance

            levels_pandas = pd.read_csv(self.Level_file.get(), names=['Level energy','Spin-Parity','Energy Label Position'], 
                                        dtype={'Level energy': float,'Spin-Parity': str})
            levels_pandas = levels_pandas.sort_values(by=['Level energy'])                  
            levels_pandas = levels_pandas.reset_index(drop=True)    
            
            transitions_pandas = pd.read_csv(self.Transition_file.get(), dtype=float, names=["Transition energy","Initial level","Final level"])
            transitions_pandas = transitions_pandas.sort_values(by=["Initial level", "Transition energy"], ascending=True)
            transitions_pandas = transitions_pandas.reset_index(drop=True)

            if(self.Stop_level.get() == -1):                                                      
                self.Stop_level.set(levels_pandas.shape[0]) 
            else:                                                                       
                pass                                                                    
                                                                    
            if(self.Stop_transition.get() == -1):                                                
                self.Stop_transition.set(transitions_pandas.shape[0])
            else:
                pass 
            
            levels_pandas.at[0,'Energy Label Position'] = levels_pandas.iloc[0]['Level energy']
                                                                                    
            # differentiating energies value and labels                                     
            for i in range(1,levels_pandas.shape[0]):                                       
                    if(abs(levels_pandas.iloc[i][0]-levels_pandas.iloc[i-1][2])<self.Min_vert_label_dist.get() or 
                       levels_pandas.iloc[i][0]<levels_pandas.iloc[i-1][2]):
                        levels_pandas.at[i,'Energy Label Position'] = levels_pandas.iloc[i-1][2]+self.Min_vert_label_dist.get()
                                                                                    
                    else:                                                                   
                        levels_pandas.at[i,'Energy Label Position'] = levels_pandas['Level energy'][i]
                                                                                    
            levels_pandas.fillna('', inplace=True)   
            
            _x_fig_start = -self.XMax.get()*self.Width_const.get()
            _x_fig_end = self.XMax.get() + self.XMax.get()*self.Width_const.get()
            _x_left_label_distance = -self.XMax.get()*self.Width_const.get()
            _x_right_label_distance = self.XMax.get() + self.XMax.get()*self.Width_const.get()
            self.DeltaX.set(self.XMax.get()/(self.Stop_transition.get()-self.Start_transition.get()))

            self.Transition_file_label.config(fg='black')
            self.Transition_file_entry.config({'background':'white'})
            self.Level_file_label.config(fg='black')
            self.Level_file_entry.config({'background':'white'})

            self.Uploaded_flag.set(1)

            print("File Uploaded! ")

        except:
            print("Something went wrong while uploading the file")
            self.Transition_file_label.config(fg='red')
            self.Transition_file_entry.config({'background':'red'})
            self.Level_file_label.config(fg='red')
            self.Level_file_entry.config({'background':'red'})

    def Draw(self, *args):
        
        if(self.Uploaded_flag.get() == 1):
            plt.rcParams['figure.figsize'] = [250,170]
            self.DeltaX.set(self.XMax.get()/(self.Stop_transition.get()-self.Start_transition.get()))
            drawLevelScheme(levels_pandas, transitions_pandas,self.DeltaX.get(), self.XMax.get(), _x_fig_start, _x_fig_end, _x_right_label_distance,
                        _x_left_label_distance, self.Fontsize.get(), self.Start_level.get(), self.Stop_level.get(), self.Start_transition.get(), 
                        self.Stop_transition.get(), 
                        self.Arrow_width.get(), self.Arrow_head_width.get(), self.Arrow_head_length.get(), self.Arrow_color.get(), self.Draw_GS.get())
        else:
            print("No file to draw. Please upload a valid file before drawing!")


if __name__ == "__main__":
    
    app = SetParameters()
    app.mainloop()
