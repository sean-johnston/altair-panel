import version
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
from tkinter import ttk
import socket

import os
import sys

"""
Get the resource path to a resource

This is used for when you use pyInstaller to create
a standalone executable. If it is not a standalone
executable, the path is the current working directory.

relative_path: Resource within the project
"""
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

"""
Class that encapulates the logic for the panel
""" 
class Panel:
    """
    Initialize the class
    """
    def __init__(self):

        self.multiplier = 1

        v = version.version

        # Setup the status LEDs
        self.status = [
            {"name": "INT"  , "handle": None, "pos": (456, 68)},
            {"name": "WO"   , "handle": None, "pos": (419, 68)},
            {"name": "STACK", "handle": None, "pos": (382, 68)},
            {"name": "HLTA" , "handle": None, "pos": (343, 68)},
            {"name": "OUT"  , "handle": None, "pos": (309, 68)},
            {"name": "M1"   , "handle": None, "pos": (272, 68)},
            {"name": "INP"  , "handle": None, "pos": (235, 68)},
            {"name": "MEMR" , "handle": None, "pos": (200, 68)},
            {"name": "PROT" , "handle": None, "pos": (162, 68)},
            {"name": "INTE" , "handle": None, "pos": (125, 68)},
            {"name": "WAIT" , "handle": None, "pos": (162, 145)},
            {"name": "HLDA" , "handle": None, "pos": (125, 145)}
        ]

        # Setup the data bus LEDs
        self.dbus = [
            {"name": "D0" ,"handle": None, "pos": (880, 68)},
            {"name": "D1" ,"handle": None, "pos": (843, 68)},
            {"name": "D2" ,"handle": None, "pos": (806, 68)},
            {"name": "D3" ,"handle": None, "pos": (751, 68)},
            {"name": "D4" ,"handle": None, "pos": (714, 68)},
            {"name": "D5" ,"handle": None, "pos": (677, 68)},
            {"name": "D6" ,"handle": None, "pos": (622, 68)},
            {"name": "D7" ,"handle": None, "pos": (585, 68)}
        ]

        # Setup the address bus LEDs
        self.abus = [
            {"name": "A0"  ,"handle": None, "pos": (880, 145)},
            {"name": "A1"  ,"handle": None, "pos": (843, 145)},
            {"name": "A2"  ,"handle": None, "pos": (806, 145)},
            {"name": "A3"  ,"handle": None, "pos": (751, 145)},
            {"name": "A4"  ,"handle": None, "pos": (714, 145)},
            {"name": "A5"  ,"handle": None, "pos": (677, 145)},
            {"name": "A6"  ,"handle": None, "pos": (622, 145)},
            {"name": "A7"  ,"handle": None, "pos": (585, 145)},
            {"name": "A8"  ,"handle": None, "pos": (548, 145)},
            {"name": "A9"  ,"handle": None, "pos": (493, 145)},
            {"name": "A10" ,"handle": None, "pos": (456, 145)},
            {"name": "A11" ,"handle": None, "pos": (419, 145)},
            {"name": "A12" ,"handle": None, "pos": (360, 145)},
            {"name": "A13" ,"handle": None, "pos": (327, 145)},
            {"name": "A14" ,"handle": None, "pos": (290, 145)},
            {"name": "A15" ,"handle": None, "pos": (235, 145)}
        ]

        # Setup the data switches
        self.dswitch = [
            {"name": "SW0"  ,"handle": None, "pos": (880, 216), "key": "0"},
            {"name": "SW1"  ,"handle": None, "pos": (843, 216), "key": "1"},
            {"name": "SW2"  ,"handle": None, "pos": (806, 216), "key": "2"},
            {"name": "SW3"  ,"handle": None, "pos": (751, 216), "key": "3"},
            {"name": "SW4"  ,"handle": None, "pos": (714, 216), "key": "4"},
            {"name": "SW5"  ,"handle": None, "pos": (677, 216), "key": "5"},
            {"name": "SW6"  ,"handle": None, "pos": (622, 216), "key": "6"},
            {"name": "SW7"  ,"handle": None, "pos": (585, 216), "key": "7"},
            {"name": "SW8"  ,"handle": None, "pos": (548, 216), "key": "8"},
            {"name": "SW9"  ,"handle": None, "pos": (493, 216), "key": "9"},
            {"name": "SW10" ,"handle": None, "pos": (456, 216), "key": "a"},
            {"name": "SW11" ,"handle": None, "pos": (419, 216), "key": "b"},
            {"name": "SW12" ,"handle": None, "pos": (360, 216), "key": "c"},
            {"name": "SW13" ,"handle": None, "pos": (327, 216), "key": "d"},
            {"name": "SW14" ,"handle": None, "pos": (290, 216), "key": "e"},
            {"name": "SW15" ,"handle": None, "pos": (235, 216), "key": "f"}
        ]

        # Setup the command switches
        self.cswitch = [
            {"name": "AUX2"                 ,"handle": None, "pos": (752, 291),"values": (14,15,"s","l")},
            {"name": "AUX1"                 ,"handle": None, "pos": (678, 291),"values": (12,13,"U","u")},
            {"name": "PROTECT/UNPROTECT"    ,"handle": None, "pos": (604, 291),"values": (10,11,"Q","q")},
            {"name": "RESET/CLR"            ,"handle": None, "pos": (530, 291),"values": ( 8, 9,"R",".")},
            {"name": "DEPOSIT/DEPOSIT NEXT" ,"handle": None, "pos": (456, 291),"values": ( 6, 7,"P","p")},
            {"name": "EXAMINE/EXAMINE NEXT" ,"handle": None, "pos": (382, 291),"values": ( 4, 5,"X","x")},
            {"name": "STEP/SLOW"            ,"handle": None, "pos": (308, 291),"values": ( 2, 3,"t",".")},
            {"name": "STOP/RUN"             ,"handle": None, "pos": (233, 291),"values": ( 1, 0,"\033","r")}
        ]

        # Power Switch
        self.power_switch = {"name": "Power Switch"  ,"handle": None, "pos": (57, 291)}

        # Initialize the GUI
        self.root = Tk()
        self.root.title("Altair 8800 Panel")

        # String for the connect button
        self.connect_var = StringVar()

        # Setup values for scale combo box, and
        # set the inital value
        self.combo_box_values = ["1x", "2x", "3x"]
        self.zoom_var = StringVar()
        self.zoom_var.set(self.combo_box_values[0])

        self.delete_var = StringVar()

        # Build the controls
        self.build_controls(self.multiplier)

        # Set the switch pressed to None
        self.switch_pressed = None

        # Set the socket to None
        self.socket = None

    """
    Build the controls in the window, based on the 
    multiplier specified.

    multiplier: Multiplier to zoom the window elements
    """
    def build_controls(self, multiplier):
        # Create a font for the controls
        self.font = tkFont.Font(family='Helvetica', size=16 * multiplier)

        # Create a frame for the controls
        self.control_frame = Frame(self.root)

        # Add the connect/disconnect button
        self.connect=Button(self.control_frame,textvariable=self.connect_var,command=self.connect_disconnect)
        self.connect["font"] = self.font
        self.connect.pack(side=LEFT,padx=10)

        # Create a scale combo box
        self.combo = ttk.Combobox(self.control_frame,
            state="readonly",
            values=self.combo_box_values,
            textvariable=self.zoom_var,
            width=4
        )
        self.combo["font"] = self.font
        self.combo.pack(side=LEFT)
        self.root.option_add("*TCombobox*Listbox*Font", self.font)

        # Add event handler for combo box
        self.combo.bind("<<ComboboxSelected>>", self.combo_select)

        self.label = Label(self.control_frame,
                 textvariable=self.delete_var,
                 font=self.font,
                 relief=SUNKEN,
                 width=4,
                 justify=CENTER
                )

        self.delete_var.set("")

        # Pack the label into the window
        self.label.pack(padx=20, pady=5)  # Add some padding to the top

        # Pack the controls
        self.control_frame.pack(padx=10, pady=10)

        # Add the canvas
        self.canvas = Canvas(self.root, width=1000 * multiplier, height=400 * multiplier)
        self.canvas.pack()
        
        #Set the resizable property False
        self.root.resizable(False, False)
    
        # Load the panel bitmap, and display it
        self.img = PhotoImage(file=resource_path("altair-panel.png")).zoom(multiplier, multiplier)
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)

        # Load the LED images
        self.led_off = PhotoImage(file=resource_path("led-off.png")).zoom(multiplier, multiplier)
        self.led_on = PhotoImage(file=resource_path("led-on.png")).zoom(multiplier, multiplier)
        self.led_on_dim = PhotoImage(file=resource_path("led-on-dim.png")).zoom(multiplier, multiplier)

        # Load the switch images
        self.switch_down = PhotoImage(file=resource_path("switch-down.png")).zoom(multiplier, multiplier)
        self.switch_middle = PhotoImage(file=resource_path("switch-middle.png")).zoom(multiplier, multiplier)
        self.switch_up = PhotoImage(file=resource_path("switch-up.png")).zoom(multiplier, multiplier)

        # Create the images on the canvas
        for i in self.status:
            i["handle"] = self.canvas.create_image(
                tuple([multiplier*x for x in i["pos"]]), image=self.led_off
            )
        for i in self.dbus:
            i["handle"] = self.canvas.create_image(
                tuple([multiplier*x for x in i["pos"]]), image=self.led_off
            )
        for i in self.abus:
            i["handle"] = self.canvas.create_image(
                tuple([multiplier*x for x in i["pos"]]), image=self.led_off
            )
        for i in self.dswitch:
            i["handle"] = self.canvas.create_image(
                tuple([multiplier*x for x in i["pos"]]), image=self.switch_down
            )
        for i in self.cswitch:
            i["handle"] = self.canvas.create_image(
                tuple([multiplier*x for x in i["pos"]]), image=self.switch_middle
            )

        self.power_switch["handle"] = self.canvas.create_image(
            tuple([multiplier*x for x in self.power_switch["pos"]]), image=self.switch_up
        )

        # Bind the mouse to the canvas to allow clicking for the switches
        self.canvas.bind("<ButtonPress-1>", self.OnMouseDown)
        self.canvas.bind("<ButtonRelease-1>", self.OnMouseUp)

        # Initialize the string for the connect/disconnect button
        self.connect_var.set("Connect")

        # Set the switch pressed to None
        self.switch_pressed = None

        # Set the socket to None
        self.socket = None

        self.label.bind("<ButtonPress-1>", self.OnLabelClicked)

    """
    Handle combo box select event

    event: combo box event
    """
    def combo_select(self, event):
        self.zoom(int(self.zoom_var.get().replace("x","")))

    """
    Clear the elements on the window
    """
    def clear(self):
        for l in self.root.pack_slaves(): l.destroy()

    """
    Zoom the window
    """
    def zoom(self, size):
        self.clear()
        self.multiplier = size
        self.build_controls(self.multiplier)
        pass

    """
    Set a key value to on the socket

    key: Key value to send
    """
    def send_switch(self, key):
        # Send the key over the socket to the server
        self.socket.send(key.encode())


    """
    Handle the mouse click event for the delete state
    label

    event: Object with the mouse event
    """
    def OnLabelClicked(self, event):
        if self.socket is not None:
            self.send_switch('~')

    """
    Handle the mouse down event for the canvas

    event: Object with the mouse event
    """
    def OnMouseDown(self, event):
        # Get the mouse x and y position
        x, y = event.x, event.y

        xs = self.power_switch["pos"][0] * self.multiplier
        ys = self.power_switch["pos"][1] * self.multiplier
        # If we pressed a switch toggle switch
        if x >= xs - 10 * self.multiplier and x <= xs + 10 * self.multiplier and y >= ys - 10 * self.multiplier and y <= ys + 30 * self.multiplier:
            self.connect_disconnect()
            return

        if self.socket is None: return

        # Check for momentary switch
        for i in self.cswitch:

            # Get the switch x and y position
            xs = i["pos"][0] * self.multiplier
            ys = i["pos"][1] * self.multiplier
            # Switch up
            if x >= xs - 10 * self.multiplier and x <= xs + 10 * self.multiplier and y > ys - 30 * self.multiplier and y <= ys:
                # Save the switch element
                self.switch_pressed = i
                # Set the switch up
                self.canvas.itemconfig(i["handle"], image = self.switch_up)
                # Send the up key value for that switch
                self.send_switch(i["values"][2])
                return
            # Switch down
            if x >= xs - 10 * self.multiplier and x <= xs + 10 * self.multiplier and y > ys and y <= ys + 30 * self.multiplier:
                # Save the switch element
                self.switch_pressed = i
                # Set the switch down
                self.canvas.itemconfig(i["handle"], image = self.switch_down)
                # Send the down value for that switch
                self.send_switch(i["values"][3])
                return

        # Check for toggle switch
        for i in self.dswitch:
            xs = i["pos"][0] * self.multiplier
            ys = i["pos"][1] * self.multiplier
            # If we pressed a switch toggle switch
            if x >= xs - 10 * self.multiplier and x <= xs + 10 * self.multiplier and y >= ys - 10 * self.multiplier and y <= ys + 30 * self.multiplier:
                # Send the key value for that switch
                self.send_switch(i["key"])
                return

    """
    Handle the mouse up event from the canvas

    event: Object with the mouse event. (Not used)
    """
    def OnMouseUp(self, event):
        # If we have pressed a momentary switch
        if self.switch_pressed is not None:
            # Change it back to the middle position
            self.canvas.itemconfig(self.switch_pressed["handle"], image = self.switch_middle)
            # Clear the press
            self.switch_pressed = None

    """
    Connect or disconnect the socket. If the connect/disconnect button is pressed, and we
    are not connected, an attempt is made to connect to the socket. If the socket is 
    connected, the socket is disconnected. 
    """
    def connect_disconnect(self):

        if self.socket is None:
            # Create a socket object
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Attempt to connect to a server
            try:
                self.socket.setblocking(True)
                self.socket.connect(('127.0.0.1', 8080))
                self.connect_var.set("Disconnect")
                self.root.title("Altair 8800 Panel - Connected")
                self.canvas.itemconfig(self.power_switch["handle"], image = self.switch_down)

                # Set the socket to non-blocking mode
                self.socket.setblocking(False)
            except BlockingIOError:
                # Connection is in progress, handle it later
                pass
            except ConnectionRefusedError:
                self.socket = None
                messagebox.showerror("Error", "Connection refused by server.")

        else:
            # Disconnect from the socket
            self.connect_var.set("Connect")
            self.socket.close()
            self.socket = None
            self.root.title("Altair 8800 Panel")
            self.canvas.itemconfig(self.power_switch["handle"], image = self.switch_up)

    """
    Update the panel when something has changed on it. I message is sent
    from the server, when the panel is updated.
    """
    def update(self):
        # Process only if the socket is valid
        if self.socket is not None:
            try:
                # Get data from the socket
                data = self.socket.recv(1024)
                if not data: 
                    # If the server dropped the connect, close it
                    # and display a message box
                    self.socket.close()
                    self.socket = None
                    messagebox.showerror("Error", "Connection has been closed.")
                    self.connect_var.set("Connect")
                else:
                    # Get all the lines that have been sent
                    lines = data.decode("utf-8").rstrip().split("\r\n")

                    # We only need the last one
                    line = lines[len(lines)-1]

                    # Break up the line into elements
                    elements = line.split(',')

                    # Switches
                    dswitch = int(elements[0])
                    for i in range(0,16):
                        if (dswitch & (2 ** i)) != 0:
                            self.canvas.itemconfig(self.dswitch[i]["handle"], image = self.switch_up)
                        else:
                            self.canvas.itemconfig(self.dswitch[i]["handle"], image = self.switch_down)

                    flags = int(elements[1])
                    if flags & 1:
                        self.delete_var.set("DEL")
                    else:
                        self.delete_var.set("BS")

                    # Status
                    status = int(elements[2])
                    for i in range(0,12):
                        if (status & (2 ** i)) != 0:
                            self.canvas.itemconfig(self.status[i]["handle"], image = self.led_on_dim)
                        else:
                            self.canvas.itemconfig(self.status[i]["handle"], image = self.led_off)

                    # Address bus
                    abus = int(elements[3])
                    for i in range(0,16):
                        if (abus & (2 ** i)) != 0:
                            self.canvas.itemconfig(self.abus[i]["handle"], image = self.led_on_dim)
                        else:
                            self.canvas.itemconfig(self.abus[i]["handle"], image = self.led_off)

                    # Data bus
                    dbus = int(elements[4]) 
                    for i in range(0,8):
                        if (dbus & (2 ** i)) != 0:
                            self.canvas.itemconfig(self.dbus[i]["handle"], image = self.led_on_dim)
                        else:
                            self.canvas.itemconfig(self.dbus[i]["handle"], image = self.led_off)
            except BlockingIOError:
                # No data available, handle it later
                pass
            except ConnectionResetError:
                # If the server dropped the connect, close it
                # and display a message box
                self.socket.close()
                self.socket = None
                messagebox.showerror("Error", "Connection has been closed.")
                self.connect_var.set("Connect")

        # Call the function after 100 ms
        self.root.after(100, self.update)

def main():

    panel = Panel()
    panel.update()

    mainloop()
 
if __name__ == '__main__':
    main()
