import tkinter as tk
from database.entities.air_measurements import AirMeasurement
from gui.gui_consts import *


class AirMeasurementCards(tk.LabelFrame):
    def __init__(self, master, measurement_data: AirMeasurement) -> None:
        super().__init__(master)

        self.measurement_data = measurement_data
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.scrollbar = tk.Scrollbar(self)


        self.lbl_measurement_title = tk.Label(
            self, font=LABEL_FONT,
            text='Datum mjerenja:'
        )
        self.lbl_measurement_title.grid(row=0, column=0,
                                       padx=10, pady=10, sticky='e')
        
        self.lbl_measurement_date_var = tk.StringVar()
        self.lbl_measurement_date_var.set(self.measurement_data.time_stamp)
        self.lbl_measurement_date = tk.Label(
            self, font=LABEL_FONT,
            textvariable=self.lbl_measurement_date_var
        )
        self.lbl_measurement_date.grid(row=0, column=1, columnspan=2,
                                       padx=10, pady=10, sticky='w')


        self.lbl_temperature_title = tk.Label(
            self, font=LABEL_FONT,
            text='Temperatura:'
        )
        self.lbl_temperature_title.grid(row=1, column=0,
                                       padx=10, pady=10, sticky='ew')
        
        self.lbl_pressure_title = tk.Label(
            self, font=LABEL_FONT,
            text='Tlak:'
        )
        self.lbl_pressure_title.grid(row=1, column=1,
                                       padx=10, pady=10, sticky='ew')
        
        self.lbl_humidity_title = tk.Label(
            self, font=LABEL_FONT,
            text='Vlaznost:'
        )
        self.lbl_humidity_title.grid(row=1, column=2,
                                       padx=10, pady=10, sticky='ew')


        self.lbl_temperature_var = tk.StringVar()
        self.lbl_temperature_var.set(self.measurement_data.get_temp_celsius())
        self.lbl_temperature = tk.Label(
            self, font=LABEL_FONT,
            textvariable=self.lbl_temperature_var
        )
        self.lbl_temperature.grid(row=2, column=0,
                                       padx=10, pady=10, sticky='ew')
        
        self.lbl_pressure_var = tk.StringVar()
        self.lbl_pressure_var.set(self.measurement_data.get_pressure_hpa())
        self.lbl_pressure = tk.Label(
            self, font=LABEL_FONT,
            textvariable=self.lbl_pressure_var
        )
        self.lbl_pressure.grid(row=2, column=1,
                                       padx=10, pady=10, sticky='ew')
        
        self.lbl_humidity_var = tk.StringVar()
        self.lbl_humidity_var.set(self.measurement_data.get_humidity())
        self.lbl_humidity = tk.Label(
            self, font=LABEL_FONT,
            textvariable=self.lbl_humidity_var
        )
        self.lbl_humidity.grid(row=2, column=2,
                                       padx=10, pady=10, sticky='ew')