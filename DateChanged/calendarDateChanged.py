def calendarDateChanged(self):
    print("The calendar date was changed.")
    dateSelected = self.calendarWidget.selectedDate().toPyDate()
    print("Date selected:", dateSelected)
    self.updateTaskList(dateSelected)