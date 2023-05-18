import tkinter as tk
from sensors_emu_services.air_sensors import get_current_measurements
from gui.gui_consts import BUTTON_FONT
from gui.custom_lbl_frames import FrameDisplayLabel, FrameCheckboxLabel
from gui.air_measurement_cards import AirMeasurementCards
from database.db_manager import get_measurements, get_measurement

class MainWindow(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('RPi Air sensors')
        self.geometry('900x900')
        self.grid_columnconfigure((0, 1), weight=1)


        #region BUTTON
        self.btn_get_measurements = tk.Button(self,
                                 text='Dohvati mjerenja',
                                 font=BUTTON_FONT,
                                 command=self.btn_get_measures)
        self.btn_get_measurements.grid(row=0, column=0, columnspan=2,
                                padx=20, pady=10, sticky='ew')
        #endregion


        #region CHECK BUTTONS
        self.frm_checkbuttons = FrameCheckboxLabel(self)
        self.frm_checkbuttons.grid(row=1, column=0, columnspan=2,
                        padx=20, pady=10, sticky='ew')
        #endregion


        #region DISPLAY LABELS
        self.frm_display_labels1 = FrameDisplayLabel(self)
        self.frm_display_labels1.grid(row=2, column=0, columnspan=2,
                        padx=20, pady=10, sticky='ew')
        

        self.measurements = get_measurements()
        for i, measure in enumerate(self.measurements):
            self.frm_measure_card = AirMeasurementCards(
                self, measurement_data=measure
            )
            if i == 0 and i % 2 == 0:
                self.frm_measure_card.grid(row=3 + i, column=0,
                            padx=20, pady=10, sticky='ew')
            else:
                self.frm_measure_card.grid(row=3 + i, column=1,
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
