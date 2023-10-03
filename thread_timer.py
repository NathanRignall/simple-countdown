import sys
import time
from datetime import datetime
import pandas as pd

from PySide6.QtCore import QThread, Signal

from ui_main import Ui_MainWindow

class thread_timer(QThread):    
    timerValue = Signal(str)
    timerText = Signal(str)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        
        self.ui = Ui_MainWindow()
        self.status = True

        self.times = pd.read_csv('times.csv')

    def countdown(self, stop):
        difference = stop - datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)

        string = str(count_hours).zfill(2) + ":" + str(count_minutes).zfill(2) + ":" + str(count_seconds).zfill(2)

        return string

    def run(self):
        # loop forever until status is false
        index = 0

        # loop over all the rows in the csv to find start index
        for i in range(len(self.times)):
            x = self.times.loc[i, "time"]
            datetime_object = datetime.strptime(x, '%d/%m/%Y %H:%M:%S')

            if  datetime.now() <= datetime_object:
                index = i
                break

        # loop forever until status is false
        while self.status:
            try:
                x = self.times.loc[index, "time"]
                datetime_object = datetime.strptime(x, '%d/%m/%Y %H:%M:%S')

                self.timerValue.emit(self.countdown(datetime_object))
                self.timerText.emit(self.times.loc[index, "text"])
                time.sleep(0.5)

            except KeyError:
                self.timerValue.emit('FINISH')
                self.timerText.emit('')
                time.sleep(60)

            if datetime.now() >= datetime_object:
                self.timerValue.emit('00:00:00')
                self.timerText.emit(self.times.loc[index, "text"])

                index += 1
                time.sleep(10)

            time.sleep(0.01)


        sys.exit(-1)