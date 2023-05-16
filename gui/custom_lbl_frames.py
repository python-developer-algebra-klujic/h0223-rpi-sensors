import tkinter as tk
from gui.gui_consts import LABEL_FONT

class FrameDisplayLabel(tk.LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.text='Prikaz rezultata mjerenja'
        self.grid_columnconfigure(
                (0, 1, 2), weight=1
            )
        self.lbl_display_temperature_var = tk.StringVar()
        self.lbl_display_temperature = tk.Label(
            self,
                textvariable=self.lbl_display_temperature_var,
                font=LABEL_FONT)
        self.lbl_display_temperature.grid(row=0, column=0,
                                padx=20, pady=10, sticky='w')
        
        self.lbl_display_pressure_var = tk.StringVar()
        self.lbl_display_pressure = tk.Label(
            self,
                textvariable=self.lbl_display_pressure_var,
                font=LABEL_FONT)
        self.lbl_display_pressure.grid(row=0, column=1,
                                padx=20, pady=10, sticky='w')
        
        self.lbl_display_humidity_var = tk.StringVar()
        self.lbl_display_humidity = tk.Label(
            self,
                textvariable=self.lbl_display_humidity_var,
                font=LABEL_FONT)
        self.lbl_display_humidity.grid(row=0, column=2,
                                padx=20, pady=10, sticky='w')
