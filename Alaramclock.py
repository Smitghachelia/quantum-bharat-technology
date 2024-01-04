import tkinter as tk
from tkinter import simpledialog
import time
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Set Alarm Time:")
        self.label.pack(pady=10)

        self.alarm_time = tk.StringVar()
        self.alarm_entry = tk.Entry(root, textvariable=self.alarm_time, font=("Helvetica", 24))
        self.alarm_entry.pack(pady=10)

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.alarm_is_set = False

    def set_alarm(self):
        alarm_time = self.alarm_time.get()

        try:
            time.strptime(alarm_time, "%H:%M")
        except ValueError:
            tk.messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")
            return

        self.alarm_is_set = True
        self.label.config(text=f"Alarm set for {alarm_time}")

    def check_alarm(self):
        while True:
            if self.alarm_is_set:
                current_time = time.strftime("%H:%M")
                if current_time == self.alarm_time.get():
                    self.trigger_alarm()
                    break
            time.sleep(1)

    def trigger_alarm(self):
        tk.messagebox.showinfo("Alarm", "Time to wake up!")
        winsound.Beep(2500, 1000)  # Adjust frequency and duration as needed
        self.alarm_is_set = False
        self.label.config(text="Set Alarm Time:")


if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)

    # Use threading to run the alarm checking loop in the background
    import threading
    alarm_thread = threading.Thread(target=alarm_clock.check_alarm)
    alarm_thread.daemon = True
    alarm_thread.start()

    root.mainloop()
