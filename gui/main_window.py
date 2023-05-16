import tkinter as tk
from sensors_emu.air_sensors import get_current_measurements
from gui.gui_consts import LABEL_FONT
from gui.custom_lbl_frames import FrameDisplayLabel

class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('RPi Air sensors')
        self.geometry('600x400')
        self.grid_columnconfigure(0, weight=1)


        #region BUTTON
        self.btn_get_measurements = tk.Button(self,
                                 text='Dohvati mjerenja',
                                 command=self.btn_get_measures)
        self.btn_get_measurements.grid(row=0, column=0, columnspan=3,
                                padx=20, pady=10, sticky='ew')
        #endregion


        #region CHECK BUTTONS
        self.frm_checkbuttons = tk.LabelFrame(self,
                text='Izbor senzora')
        self.frm_checkbuttons.grid(row=1, column=0,
                        padx=20, pady=10, sticky='ew')
        self.frm_checkbuttons.grid_columnconfigure(
                (0, 1, 2), weight=1
            )

        self.cb_only_temperature = tk.Checkbutton(
            self.frm_checkbuttons,
            text='Samo temperatura')
        self.cb_only_temperature.grid(row=0, column=0,
                                padx=20, pady=10, sticky='w')

        self.cb_only_pressure = tk.Checkbutton(
            self.frm_checkbuttons,
            text='Samo tlak')
        self.cb_only_pressure.grid(row=0, column=1,
                                padx=20, pady=10, sticky='w')

        self.cb_only_humidity = tk.Checkbutton(
            self.frm_checkbuttons,
            text='Samo vlaznost')
        self.cb_only_humidity.grid(row=0, column=2,
                                padx=20, pady=10, sticky='w')
        #endregion


        #region DISPLAY LABELS
        self.frm_display_labels1 = FrameDisplayLabel(self)
        self.frm_display_labels1.grid(row=2, column=0,
                        padx=20, pady=10, sticky='ew')
        
        self.frm_display_labels2 = FrameDisplayLabel(self)
        self.frm_display_labels2.grid(row=3, column=0,
                        padx=20, pady=10, sticky='ew')
        #endregion


    def btn_get_measures(self):
        current_measurements = get_current_measurements()

        self.frm_display_labels1.lbl_display_temperature_var.set(
            current_measurements.get_temp_celsius()
        )

        self.frm_display_labels1.lbl_display_pressure_var.set(
            current_measurements.get_pressure_hpa()
        )
        self.frm_display_labels1.lbl_display_humidity_var.set(
            current_measurements.get_humidity()
        )

        self.frm_display_labels2.lbl_display_temperature_var.set(
            current_measurements.get_temp_celsius()
        )

        self.frm_display_labels2.lbl_display_pressure_var.set(
            current_measurements.get_pressure_hpa()
        )
        self.frm_display_labels2.lbl_display_humidity_var.set(
            current_measurements.get_humidity()
        )
