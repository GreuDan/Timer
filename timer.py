from tkinter import *
from tkinter import messagebox
import calendar
import os
from datetime import datetime


class Themplate:
    def __init__(self):
        self.array_objects = []
        self.array_condition = []

    def create_default_look(self):
        self.app_frame = Frame(canvas, bg="yellow")
        self.app_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        self.label1 = Label(canvas, text="This month is \n" + datetime.now().strftime('%B'), font='Helvetica 18 bold',
                            bg="yellow")
        canvas.create_window(500, 135, window=self.label1)

        self.label2 = Label(canvas, text="INSERT DAY:", bg="yellow")
        canvas.create_window(150, 210, window=self.label2)

        self.label3 = Label(canvas, text='', bg="white", width=100, height=20)
        canvas.create_window(500, 450, window=self.label3)

    def set_Insert_minute(self):
        self.label2 = Label(canvas, text="INSERT MINUTES:", bg="yellow")
        canvas.create_window(600, 210, window=self.label2)
        self.set_object_to_destroy(self.label2)

    def set_Insert_hour(self):
        self.label1 = Label(canvas, text="INSERT HOUR: ", bg="yellow")
        canvas.create_window(385, 210, window=self.label1)
        self.set_object_to_destroy(self.label1)

    def set_Insert_event(self):
        self.label0 = Label(canvas, text="INSERT EVENT:", bg="yellow")
        canvas.create_window(150, 260, window=self.label0)
        self.set_object_to_destroy(self.label0)

    def set_object_to_destroy(self, x):
        self.array_objects.append(x)

    def destroy_objects(self):
        for i in range(len(self.array_objects)):
            self.array_objects[i].destroy()


class date_and_time:
    def __init__(self):
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.temps = 0
        self.array_objects = []
        self.array_labels = []
        self.array_condition = []
        self.name = 0
        self.verify = 0

    def set_object(self, x):
        self.array_objects.append(x)

    def objects_to_destroy(self):
        for i in range(len(self.array_objects)):
            self.array_objects[i].destroy()

    def set_Days_Hours_Minutes(self, a, b, c, d):
        self.day = int(a)
        self.hour = int(b)
        self.minute = int(c)
        self.temps = int(d)

    def set_Minute(self, x):
        self.minute = x

    def get_Days_Hours_Minutes(self):
        return self.day, self.hour, self.minute, self.temps

    def set_labels_to_destroy(self, x):
        self.array_labels.append(x)

    def get_labels_to_destroy(self):
        for i in range(len(self.array_labels)):
            self.array_labels[i].destroy()

    def verify_status_event(self, timeformat):
        if (timeformat == "07:00:00:00"):
            messagebox.showinfo("Curent event status", "You have less then 1 week until " + self.name)
        else:
            if (timeformat == "01:00:00:00"):
                messagebox.showinfo("Curent event status", "You have less then 1 day  until " + self.name)
            else:
                if (timeformat == "00:06:00:00"):
                    messagebox.showinfo("Curent event status", "You have less then 6 hours  until " + self.name)
                else:
                    if (timeformat == "00:01:00:00"):
                        messagebox.showinfo("Curent event status", "You have less then 1 hours  until " + self.name)
                    else:
                        if (timeformat == "00:00:30:00"):
                            messagebox.showinfo("Curent event status",
                                                "You have less then half an hours  until " + self.name)
                        else:
                            if (timeformat == "00:00:00:00"):
                                messagebox.showinfo("Curent event status", "Event reached " + self.name)

    def set_nume_event(self):
        self.nume_event = Entry(canvas)
        self.nume_event.pack()
        canvas.create_window(255, 260, window=self.nume_event)
        self.set_object(self.nume_event)

    def get_nume_event(self):
        self.name = self.nume_event.get()
        return self.nume_event.get()

    def set_object_to_destroy_after_condition(self, x):
        self.array_condition.append(x)

    def destroy_objects_after_condition(self):
        for i in range(len(self.array_condition)):
            self.array_condition[i].destroy()

    def __del__(self):
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.temps = 0


class Saves(date_and_time, Themplate):
    def __init__(self):
        date_and_time.__init__(self)
        Themplate.__init__(self)
        self.c1 = 0
        self.date = 0
        self.name = 0
        self.ok = 0
        self.alert_save = 0
        self.save_buttons = []
        self.count_emptys = []
        self.saved_values = []
        self.save_event = []
        self.save_count = 0
        self.Saved = Button(canvas, text="Saved events", bg="yellow", command=self.when_Saved_is_clicked)
        self.Saved.pack()
        canvas.create_window(190, 320, window=self.Saved)
        self.destroy_save = self.Saved

    def reset_button(self):
        def reset_saves():
            if (os.path.isfile('save.txt')):
                os.remove('save.txt')
            else:
                messagebox.showwarning("YOU DON'T HAVE SAVED EVENTS", "SAVE AN EVENT AT LAST")

        self.reset = Button(canvas, text="Reset Saves", bg="yellow", command=reset_saves)
        self.reset.pack()
        canvas.create_window(270, 320, window=self.reset)

    def when_Saved_is_clicked(self):
        if os.path.isfile('save.txt'):
            saved = Toplevel(root)
            saved.geometry("300x300")
            saved.title("Saved Events")
            saved.resizable(False, False)
            canvas_saved = Canvas(saved, height=200, width=300, bg="black")
            canvas_saved.pack(fill=BOTH, expand=YES)
            save_frame = Frame(canvas_saved, bg="yellow")
            save_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
            self.alert_save += 1

            with open('save.txt', 'r')as f:
                self.saved_values = f.read()
                self.saved_values = self.saved_values.split(',')
            c1 = 0
            a1 = []
            b1 = []
            for j in range(10):
                a1.append(j)
                b1.append(j)

            def this_does_select_event_button(j):
                self.name = self.saved_values[j]
                self.date = self.saved_values[j + 1]
                save_d = []
                save_d = self.date.split(':')
                curent_object = self.get_ok()
                if (curent_object <= 4):
                    d, h, m, t = int(save_d[0]), int(save_d[1]), int(save_d[2]), 0
                    s_d = '{:02d}:{:02d}:{:02d}:{:02d}'.format(d, h, m, 0)

                    hours_for_exception = h
                    minutes_for_exception = m
                    d -= datetime.now().day
                    h -= datetime.now().hour
                    m -= datetime.now().minute
                    if (d >= 0):
                        l = Label(canvas, text='', bg="white")
                        l1 = Label(canvas, text=self.name, bg="white")
                        l2 = Label(canvas, text=s_d, bg="white")

                        self.set_object_to_destroy_after_condition(l)
                        self.set_object_to_destroy_after_condition(l1)
                        self.set_object_to_destroy_after_condition(l2)
                        canvas.create_window(210, curent_object * 50 + 350, window=l1)
                        canvas.create_window(500, curent_object * 50 + 350, window=l2)
                        canvas.create_window(775, curent_object * 50 + 350, window=l)

                        if (h < 0):
                            h = 24 - datetime.now().hour + hours_for_exception
                            d -= 1
                            if (d < 0):
                                messagebox.showwarning("Event had passed", "It cannot be set")
                                self.destroy_objects_after_condition()
                                saved.destroy()

                        if (m < 0):
                            h -= 1
                            if (h < 0):
                                h = 23 - datetime.now().hour + hours_for_exception
                                d -= 1
                                if (d < 0):
                                    messagebox.showwarning("Event had passed", "It cannot be set")
                                    self.destroy_objects_after_condition()
                                    saved.destroy()
                            m = 60 - datetime.now().minute + minutes_for_exception
                            s = datetime.now().second
                        else:
                            s = datetime.now().second
                        if (d == 0 & h == 0):
                            if (m < 0): m = 0
                        t = m * 60 - s
                        self.set_Days_Hours_Minutes(d, h, m, t)
                        if (t < 0):
                            messagebox.showwarning("NO EVENT", "EVENT PASSED")
                            self.destroy_objects_after_condition()
                        else:
                            self.save_button(curent_object)

                            def time():
                                d, h, m, t = self.get_Days_Hours_Minutes()
                                m, s = divmod(t, 60)
                                timeformat = '{:02d}:{:02d}:{:02d}:{:02d}'.format(d, h, m, s)
                                try:
                                    l.config(text=timeformat)
                                except:
                                    return 0
                                if (t == 0):
                                    if (d > 0):
                                        if (h == 0):
                                            h = 23
                                            t = 3600
                                            d -= 1
                                            m, s = divmod(t, 60)
                                    if (h > 0 & t == 0):
                                        h -= 1
                                        t = 3600
                                        m, s = divmod(t, 60)
                                self.verify_status_event(timeformat)
                                t -= 1
                                if (d == 0):
                                    if (h == 0):
                                        if (m == 0):
                                            if (s == 0):
                                                self.destroy_objects_after_condition()
                                                return 0
                                self.set_Days_Hours_Minutes(d, h, m, t)
                                l.after(1000, time)

                            time()
                            if (curent_object <= 4):
                                self.set_ok()
                            self.reset.destroy()
                            saved.destroy()
                            self.Saved.destroy()
                    else:
                        messagebox.showwarning("Event had passed", "It cannot be set")
                        saved.destroy()
                else:
                    messagebox.showwarning("MAXIMUM LIMIT REACHED",
                                           "You've reached the maximum limit of timers")

            for j in range(len(self.saved_values) - 1):
                if (j % 2 == 0):
                    a1[c1] = Label(saved, text=self.saved_values[j] + "," + self.saved_values[j + 1], bg="yellow")
                    a1[c1].pack()
                    canvas_saved.create_window(100, 60 + 20 * c1, window=a1[c1])
                    b1[c1] = Button(saved, text="Select event", bg="yellow",
                                    command=lambda j=j: this_does_select_event_button(j))
                    b1[c1].pack()
                    canvas_saved.create_window(200, 60 + 20 * c1, window=b1[c1])
                    c1 += 1
                    j += 2
        else:
            messagebox.showwarning("YOU DON'T HAVE SAVED EVENTS", "SAVE AN EVENT AT LAST")

    def get_days_hours_minutes(self):
        save_d = self.date.split(":")

    def set_Save(self, name, date):
        self.date = date
        self.name = name

    def get_date_to_save(self):
        return self.date

    def destroy_save_button(self, count):
        self.save_buttons[count].destroy()

    def save_button(self, i):
        def put_event(a1, b1):
            with open('save.txt', 'a') as f:
                f.write(a1 + ',')
                f.write(b1 + ',')

        if (len(self.save_event) == 5):
            self.save_event[i] = Button(canvas, text="SAVE EVENT", bg="white", activebackground="blue",
                                        activeforeground="yellow",
                                        command=lambda a1=self.name, b1=self.date: put_event(a1, b1))
        else:
            self.save_event.append(
                Button(canvas, text="SAVE EVENT", bg="white", activebackground="blue", activeforeground="yellow",
                       command=lambda a1=self.name, b1=self.date: put_event(a1, b1)))
        self.save_buttons.append(self.save_event[i])
        if (self.alert_save == 1):
            self.alert_save -= 1
        else:
            self.save_event[i].pack()
            canvas.create_window(580, i * 50 + 350, window=self.save_event[i])

    def set_ok(self):
        self.ok += 1

    def get_ok(self):
        return self.ok

    def get_len_of_empty_spaces(self):
        return len(self.count_emptys)

    def set_Count_empty(self, x):
        self.count_emptys.append(x)

    def get_empty_space(self):
        return self.count_emptys[len(self.count_emptys) - 1]

    def delet_an_empty_space(self):
        self.count_emptys.pop()


def this_does_set_timer_button():
    if save.get_ok() <= 4:
        curent_object = save.get_ok()
    else:
        curent_object = save.get_empty_space()
        save.delet_an_empty_space()
    if a[curent_object].get_nume_event():
        app_template.destroy_objects()

        d, h, m, t = a[curent_object].get_Days_Hours_Minutes()

        s_d = '{:02d}:{:02d}:{:02d}:{:02d}'.format(d, h, m, 0)
        save.set_Save(a[curent_object].get_nume_event(), s_d)
        l = Label(canvas, text='', bg="white")
        l1 = Label(canvas, text=a[curent_object].get_nume_event(), bg="white")
        l2 = Label(canvas, text=save.get_date_to_save(), bg="white")

        a[curent_object].set_object_to_destroy_after_condition(l)
        a[curent_object].set_object_to_destroy_after_condition(l1)
        a[curent_object].set_object_to_destroy_after_condition(l2)

        canvas.create_window(210, curent_object * 50 + 350, window=l1)
        canvas.create_window(500, curent_object * 50 + 350, window=l2)
        canvas.create_window(775, curent_object * 50 + 350, window=l)
        save.save_button(curent_object)

        hours_for_exception = h
        minutes_for_exception = m
        d -= datetime.now().day
        h -= datetime.now().hour
        m -= datetime.now().minute

        if h < 0 & d > 0:
            h = 24 - datetime.now().hour + hours_for_exception
            d -= 1
        if m < 0:
            h -= 1
            if h < 0:
                h = 23 - datetime.now().hour + hours_for_exception
                d -= 1
            m = 60 - datetime.now().minute + minutes_for_exception
            s = datetime.now().second
        else:
            s = datetime.now().second
        if (d == 0 & h == 0):
            if (m < 0): m = 0
        t = m * 60 - s
        a[curent_object].set_Days_Hours_Minutes(d, h, m, t)
        a[curent_object].objects_to_destroy()
        if (t < 0):
            messagebox.showwarning("NO EVENT", "EVENT PASSED")
            a[curent_object].destroy_objects_after_condition()
            save.destroy_save_button(curent_object)
            a[curent_object].objects_to_destroy()
        else:
            def time():
                d, h, m, t = a[curent_object].get_Days_Hours_Minutes()
                m, s = divmod(t, 60)
                timeformat = '{:02d}:{:02d}:{:02d}:{:02d}'.format(d, h, m, s)
                l.config(text=timeformat)
                if (t == 0):
                    if (d > 0):
                        if (h == 0):
                            h = 23
                            t = 3600
                            d -= 1
                            m, s = divmod(t, 60)
                    if (h > 0 & t == 0):
                        h -= 1
                        t = 3600
                        m, s = divmod(t, 60)
                a[curent_object].verify_status_event(timeformat)
                t -= 1
                if (d == 0):
                    if (h == 0):
                        if (m == 0):
                            if (s == 0):
                                a[curent_object].destroy_objects_after_condition()
                                save.destroy_save_button(curent_object)
                                save.set_Count_empty(curent_object)
                                return 0
                a[curent_object].set_Days_Hours_Minutes(d, h, m, t)
                l.after(1000, time)

            time()
            if (curent_object <= 4):
                save.set_ok()
    else:
        messagebox.showwarning("NO EVENT NAME", "SET EVENT NAME")


def set_day():
    def select_date(event):

        def minut_seter(event):
            a[curent_object].set_Days_Hours_Minutes(variable.get(), variable1.get(), variable2.get(), 0)

        def right_minutes(event):

            def minut_seter(event):
                a[curent_object].set_Days_Hours_Minutes(variable.get(), variable1.get(), variable2.get(), 0)

            curent_object = save.get_ok()
            if (curent_object <= 4):
                if (int(variable1.get()) > datetime.now().hour or int(variable.get()) > datetime.now().day):
                    c_m = 0
                else:
                    c_m = datetime.now().minute + 1
                mint = []
                for j in range(60 - c_m):
                    if (c_m < 10):
                        mint.append("0" + str(c_m))
                    else:
                        mint.append(str(c_m))
                    c_m += 1
                app_template.set_Insert_minute()
                variable2 = StringVar(canvas)
                variable2.set(mint[0])
                opt2 = OptionMenu(canvas, variable2, *mint, command=minut_seter)
                app_template.set_object_to_destroy(opt2)
                opt2.configure(bg="yellow")
                opt2.pack()
                canvas.create_window(700, 210, width=70, window=opt2)
                a[curent_object].set_Days_Hours_Minutes(variable.get(), variable1.get(), variable2.get(), 0)

        count_spaces = save.get_len_of_empty_spaces()
        curent_object = save.get_ok()
        if (curent_object <= 4 | count_spaces != 0):
            if (curent_object > 4):
                curent_object = save.get_empty_space()
            a[curent_object].set_nume_event()
            app_template.set_Insert_event()
            if (int(variable.get()) > datetime.now().day):
                c_h = 0
            else:
                c_h = datetime.now().hour

            hours = []
            for j in range(23 - c_h + 1):
                if (c_h < 10):
                    hours.append("0" + str(c_h))
                else:
                    hours.append(str(c_h))
                c_h += 1
            variable1 = StringVar(canvas)
            variable1.set(hours[0])
            app_template.set_Insert_hour()
            opt1 = OptionMenu(canvas, variable1, *hours, command=right_minutes)
            app_template.set_object_to_destroy(opt1)
            opt1.pack()
            opt1.configure(bg="yellow")
            canvas.create_window(460, 210, width=70, window=opt1)
            if (int(variable.get()) > datetime.now().day):
                c_m = 0
            else:
                c_m = datetime.now().minute + 1
            mint = []
            for j in range(60 - c_m):
                if (c_m < 10):
                    mint.append("0" + str(c_m))
                else:
                    mint.append(str(c_m))
                c_m += 1
            app_template.set_Insert_minute()
            variable2 = StringVar(canvas)
            variable2.set(mint[0])
            opt2 = OptionMenu(canvas, variable2, *mint, command=minut_seter)
            app_template.set_object_to_destroy(opt2)
            opt2.pack()
            opt2.configure(bg="yellow")
            canvas.create_window(700, 210, width=70, window=opt2)
            a[curent_object].set_Days_Hours_Minutes(variable.get(), variable1.get(), variable2.get(), 0)
            set_timer = Button(canvas, text="Set timer", bg="yellow", activebackground="blue",
                               activeforeground="yellow",
                               command=this_does_set_timer_button)
            app_template.set_object_to_destroy(set_timer)
            set_timer.pack()
            canvas.create_window(830, 210, window=set_timer)
        else:
            if (save.get_ok() > 4 & save.get_len_of_empty_spaces() == 0):
                messagebox.showinfo("MAXIMUM LIMIT REACHED",
                                    "You've reached the maximum limit of timers")

    days = []
    c_d = datetime.now().day
    for x in range(calendar.monthrange(datetime.now().year, datetime.now().month)[1] - c_d):
        if (c_d < 10):
            days.append("0" + str(c_d))
        else:
            days.append(str(c_d))
        c_d += 1

    variable = StringVar(canvas)
    variable.set(days[0])
    opt = OptionMenu(canvas, variable, *days, command=select_date)
    opt.configure(bg="yellow")
    opt.pack()
    canvas.create_window(250, 210, width=70, window=opt)


root = Tk()
root.title("Countdown")
root.resizable(False, False)

canvas = Canvas(root, height=1000, width=1000, bg="black")
canvas.pack(fill=BOTH, expand=YES)

a = []
for i in range(5):
    a.append(date_and_time())

app_template = Themplate()
app_template.create_default_look()

save = Saves()
save.reset_button()
set_day()

root.mainloop()
