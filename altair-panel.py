import version
from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
from tkinter import ttk
import math
from PIL import Image, ImageTk
import socket

import os
import sys
import json

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

        self.settings={
            "scale": 1.0
        }
        #self.multiplier = 1

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

        # Set the state elements to 0
        self.elements = [0,0,0,0,0]

        # Power Switch
        self.power_switch = {"name": "Power Switch"  ,"handle": None, "pos": (57, 291)}

        # Initialize the GUI
        self.root = Tk()
        self.title = "Altair 8800 Panel (" + version.version + ")"
        self.root.title(self.title)
        self.root.configure(background='black')

        # Make only the horizontal resizable
        self.root.resizable(True, False)

        # Set the socket to None
        self.socket = None

        # String for the connect button
        self.connect_var = StringVar()

        # String for the delete label
        self.delete_var = StringVar()

        # Load panel image
        self.panel_orig = Image.open(resource_path("altair-panel.png"))

        # Load the LED images
        self.led_off_orig    = Image.open(resource_path("led-off.png"))
        self.led_on_orig     = Image.open(resource_path("led-on.png"))
        self.led_on_dim_orig = Image.open(resource_path("led-on-dim.png"))

        # Load the switch images
        self.switch_down_orig   = Image.open(resource_path("switch-down.png"))
        self.switch_middle_orig = Image.open(resource_path("switch-middle.png"))
        self.switch_up_orig     = Image.open(resource_path("switch-up.png"))

        # Build the controls
        self.build_controls(self.settings['scale'])

        self.settings_file = "cfg.json"

        self.root.after(100, self.set_window_size)

        # Set the switch pressed to None
        self.switch_pressed = None

        # Bind the resizing window event
        self.root.bind("<Configure>", self.resizing)

        # Set the initial window size
        self.inital_window_width  = None
        self.inital_window_height = None


    def write_config(self):
        with open(self.settings_file, "w") as outfile:
            json_object = json.dumps(self.settings, indent=4)
            outfile.write(json_object)

    def read_config(self):
        if not os.path.exists(self.settings_file):
            self.write_config()

        with open(self.settings_file, 'r') as openfile:
            self.settings = json.load(openfile)

    def set_window_size(self):
        self.read_config()
        self.clear()
        self.build_controls(self.settings['scale'])

    """
    Code that is run when the window is resized

    event: Resize event
    """
    def resized(self, event):
        # Only handle for main window
        if event.widget == self.root:

            # If the window was initially created
            if self.inital_window_width == None: 

                # Gather the initial window size, so we can scale the
                # window proportionally
                self.inital_window_width = event.width #- self.window_decoration_width
                self.inital_window_height = event.height #- self.window_decoration_height
            else:
                # If the windows has already been created, zoom
                # the window, and resize the horizontal to match
                # proportions
                self.zoom(event.width / self.inital_window_width)
                y=int(((event.width) * (self.inital_window_height/(self.inital_window_width))) )
                if event.height != y: 
                    self.root.geometry('{x}x{y}'.format(x=event.width,y=y))

    """
    Code that runs when the window is being resized

    event: Resize event
    """
    def resizing(self, event):
        if event.widget == self.root:
            if getattr(self, "_after_id", None):
                self.root.after_cancel(self._after_id)
            self._after_id = self.root.after(
                100, lambda: self.resized(event)
            )

    """
    Resize the image based on the mulitplier

    image: The unresized image
    mult: The multiplier to resize the image to
    """
    def resize_image(self, image, mult):
        #image = Image.open(file)
        resized_image = image.resize((int(image.width * mult), int(image.height * mult)))
        return ImageTk.PhotoImage(resized_image)

    """
    Build the controls in the window, based on the 
    multiplier specified.

    multiplier: Multiplier to zoom the window elements
    """
    def build_controls(self, multiplier):
        # Create a font for the controls
        self.font = tkFont.Font(family='Helvetica', size=int(16 * multiplier))

        self.control_area = Frame(self.root)

        # Create a frame for the controls
        self.control_frame = Frame(self.control_area)

        # Add the connect/disconnect button
        self.connect=Button(self.control_frame,textvariable=self.connect_var,command=self.connect_disconnect)
        self.connect["font"] = self.font
        self.connect.pack(side=LEFT,padx=5)

        self.label = Label(self.control_frame,
                 textvariable=self.delete_var,
                 font=self.font,
                 relief=SUNKEN,
                 width=4,
                 justify=CENTER
                )

        self.delete_var.set("")

        # Pack the label into the window
        self.label.pack(padx=5, pady=5)  # Add some padding to the top

        # Pack the controls
        self.control_frame.pack(padx=10, pady=10)
        self.control_area.pack(fill="both", expand=True)

        # Add the canvas
        self.canvas = Canvas(self.root, width=1000 * multiplier, height=400 * multiplier)
        self.canvas.configure(background='black')
        self.canvas.pack()
        
        # Resize the panel bitmap, and display it
        self.panel = self.resize_image(self.panel_orig, multiplier)
        self.canvas.create_image(0, 0, anchor=NW, image=self.panel)

        # Resize the LED images
        self.led_off    = self.resize_image(self.led_off_orig,    multiplier)
        self.led_on     = self.resize_image(self.led_on_orig,     multiplier)
        self.led_on_dim = self.resize_image(self.led_on_dim_orig, multiplier)

        # Resize the switch images
        self.switch_down   = self.resize_image(self.switch_down_orig  , multiplier)
        self.switch_middle = self.resize_image(self.switch_middle_orig, multiplier)
        self.switch_up     = self.resize_image(self.switch_up_orig    , multiplier)

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
        if self.socket is None:
            self.connect_var.set("Connect")
        else:
            self.connect_var.set("Disconnect")

        # Set the switch pressed to None
        self.switch_pressed = None

        self.label.bind("<ButtonPress-1>", self.OnLabelClicked)

        self.set_state()        

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
        self.settings["scale"] = size
        self.write_config()
        self.build_controls(size)
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

        xs = self.power_switch["pos"][0] * self.settings["scale"]
        ys = self.power_switch["pos"][1] * self.settings["scale"]

        # If we pressed a switch toggle switch
        if x >= xs - 10 * self.settings["scale"] and \
                x <= xs + 10 * self.settings["scale"] and \
                y >= ys - 10 * self.settings["scale"] and \
                y <= ys + 30 * self.settings["scale"]:
            self.connect_disconnect()
            return

        if self.socket is None: return

        # Check for momentary switch
        for i in self.cswitch:

            # Get the switch x and y position
            xs = i["pos"][0] * self.settings["scale"]
            ys = i["pos"][1] * self.settings["scale"]
            # Switch up
            if x >= xs - 10 * self.settings["scale"] \
                    and x <= xs + 10 * self.settings["scale"] \
                    and y > ys - 30 * self.settings["scale"] \
                    and y <= ys:
                # Save the switch element
                self.switch_pressed = i
                # Set the switch up
                self.canvas.itemconfig(i["handle"], image = self.switch_up)
                # Send the up key value for that switch
                self.send_switch(i["values"][2])
                return
            # Switch down
            if x >= xs - 10 * self.settings["scale"] \
                    and x <= xs + 10 * self.settings["scale"] \
                    and y > ys \
                    and y <= ys + 30 * self.settings["scale"]:
                # Save the switch element
                self.switch_pressed = i
                # Set the switch down
                self.canvas.itemconfig(i["handle"], image = self.switch_down)
                # Send the down value for that switch
                self.send_switch(i["values"][3])
                return

        # Check for toggle switch
        for i in self.dswitch:
            xs = i["pos"][0] * self.settings["scale"]
            ys = i["pos"][1] * self.settings["scale"]
            # If we pressed a switch toggle switch
            if x >= xs - 10 * self.settings["scale"] \
                    and x <= xs + 10 * self.settings["scale"] \
                    and y >= ys - 10 * self.settings["scale"] \
                    and y <= ys + 30 * self.settings["scale"]:
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
                # Make the connection blocking, for connect
                self.socket.setblocking(True)

                # Connect to server
                self.socket.connect(('127.0.0.1', 8801))

                # SEt the connect button text
                self.connect_var.set("Disconnect")

                # Update the title
                self.root.title(self.title + " - Connected")

                # You on the power switch
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

            # Set connect button text
            self.connect_var.set("Connect")

            # Close the socket
            self.socket.close()
            self.socket = None

            # Update the window title
            self.root.title(self.title)

            # Reset the state
            self.elements = [0,0,0,0,0]
            self.set_state()

            # Turn off the power switch
            self.canvas.itemconfig(self.power_switch["handle"], image = self.switch_up)

    """
    Set the state of the switches and LEDs, based on the elements data 
    """
    def set_state(self):
        # Switches
        dswitch = int(self.elements[0])
        for i in range(0,16):
            if (dswitch & (2 ** i)) != 0:
                self.canvas.itemconfig(self.dswitch[i]["handle"], image = self.switch_up)
            else:
                self.canvas.itemconfig(self.dswitch[i]["handle"], image = self.switch_down)

        flags = int(self.elements[1])
        if self.socket is None:
            # Set unconnected value
            self.delete_var.set("")
        else:
            # Set the value based on actual panel
            if flags & 1:
                self.delete_var.set("DEL")
            else:
                self.delete_var.set("BS")

        # Status
        status = int(self.elements[2])
        for i in range(0,12):
            if (status & (2 ** i)) != 0:
                self.canvas.itemconfig(self.status[i]["handle"], image = self.led_on_dim)
            else:
                self.canvas.itemconfig(self.status[i]["handle"], image = self.led_off)

        # Address bus
        abus = int(self.elements[3])
        for i in range(0,16):
            if (abus & (2 ** i)) != 0:
                self.canvas.itemconfig(self.abus[i]["handle"], image = self.led_on_dim)
            else:
                self.canvas.itemconfig(self.abus[i]["handle"], image = self.led_off)

        # Data bus
        dbus = int(self.elements[4]) 
        for i in range(0,8):
            if (dbus & (2 ** i)) != 0:
                self.canvas.itemconfig(self.dbus[i]["handle"], image = self.led_on_dim)
            else:
                self.canvas.itemconfig(self.dbus[i]["handle"], image = self.led_off)


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
                    self.elements = line.split(',')
                    self.set_state()

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
