import tkinter as tk
from tkinter import messagebox


class FocusClock:
    def __init__(self, master):
        self.master = master
        master.title("专注时钟")
        
        self.focus_time = tk.IntVar(value=25)
        self.break_time = tk.IntVar(value=5)
        self.is_running = False
        self.total_seconds = 0
        self.timer = None

        tk.Label(master, text="专注时间（分钟）:").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.focus_time).grid(row=0, column=1)

        tk.Label(master, text="休息时间（分钟）:").grid(row=1, column=0)
        tk.Entry(master, textvariable=self.break_time).grid(row=1, column=1)

        self.start_button = tk.Button(master, text="开始", command=self.start_timer)
        self.start_button.grid(row=2, column=0)

        self.pause_button = tk.Button(master, text="暂停", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.grid(row=2, column=1)

        self.reset_button = tk.Button(master, text="重置", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.grid(row=2, column=2)

        self.time_label = tk.Label(master, text="00:00", font=("Arial", 30))
        self.time_label.grid(row=3, columnspan=3)

    def start_timer(self):
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.run_focus()

    def run_focus(self):
        self.total_seconds = self.focus_time.get() * 60
        self.update_timer()

    def run_break(self):
        self.total_seconds = self.break_time.get() * 60
        self.update_timer()

    def update_timer(self):
        if self.is_running:
            minutes, seconds = divmod(self.total_seconds, 60)
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            if self.total_seconds > 0:
                self.total_seconds -= 1
                self.timer = self.master.after(1000, self.update_timer)
            else:
                self.master.after_cancel(self.timer)
                if self.is_running:
                    self.is_running = False
                    messagebox.showinfo("提示", "专注时间结束，休息一下吧！")
                    self.run_break()

    def pause_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.master.after_cancel(self.timer)

    def reset_timer(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.master.after_cancel(self.timer)
        self.time_label.config(text="00:00")


root = tk.Tk()
app = FocusClock(root)
root.mainloop()
