# Altair Panel

## Overview

This application, written in Python 3, allows using a graphical panel with David Hansel's 
Altair 8800 Simulator. This works with a modified version of the code, which has hooks,
to receive updates to the display, and sending switch commands to the simulator.

This version can be found here: https://github.com/sean-johnston/Altair8800.

This version includes a seperate server listening on port 8080, which will communicate
with the Altair Panel application.

## Dependencies

The application requires the following dependences:

* Python 3: Python 3 needs to be installed, to run the application. I have developed it 
using version 3.12.3. Older versions may work, but are not guaranteed. 

* **Note:** I have found that version 3.9 or older will not work with this code.

* Tkinter: The application is written using the Tkinter graphical user interface. It
is not using any special functionally, and should work on multiple platforms.

    pip3 install tk

* pillow: We need this library to the scale the graphics for the panel.

    pip3 install pillow

## Running

Go to the directory that contains the application, and execute the following on the 
command line:

   python3 altair-panel

You should get a window that looks simuliar to the Altair 8800 panel. At the bottom
of the panel will be a "Connect" button.

## Using the Application

### Start Simulator
To use the application, you need to start and instance of the the modified verson of
the Altair 8800. Once this is started, you can connect to the simulator.

### Connect To Simulator
Press the "Connect" button, on the Altair Panel. This this button should changes to
"Disconnect", and the power switch will change to "On". You can toggle the power
swtich to do the same thing. If a connection is not successful, a message box will 
be displayed, saying that it was not successful.  If this happens, the Altair Panel 
can not connect to the simulator. Confirm that the simulator is running and you are 
using the modified version.

### Panel Switches

By clicking on the data switches (A0-A15), you can toggle the switches to the other
state. This sends a key value to the simulator, and returns the state of the panel,
toggling the switch.

To use the momentary switches (Command switches), you would click above or below the
switch. This will send a key value to the simulator, with the command. If the panel
display changes, the panel will receive update state information. If it changes to
terminal mode, and display output in the simulator's terminal.

Commanding a STOP, will terminate the running application, and return back to the 
the panel. The simulator will send the panel state.

## Resizing The Window

Since some computer screens can be set to a resolution that makes the application
to small to read. There is an option to make the window bigger. By resizing the 
window horizontally, the window will resize proportionally to a bigger or smaller size.

## Changing The Behavior Of Backspace Key

By default the backspace is set the (BS ascii 8). By clicking on the control, 
you can toggle between BS (ascii 8) and DEL (ascii 127). This is the same as
sending a tilda (~) on the terminal.

## Disconnecting From Simulator

To disconnect from the simulator, press the "Disconnnect" button. It will change
to "Connect". If the simulator is terminated, the connecting between the Altair
Panel and the simulator will be closed. A message box will be display, saying
that the connection was lost, and the "Disconnect" button will change to 
"Connect"

## Ready Made Executable

A ready made binary executable is available at the following location, for 
different platfroms:

https://github.com/sean-johnston/altair-panel/releases

On Linux and MacOS, you need to make the file executable. You can do that 
with the following command:

    chmod 755 altair-panel-linux (For Linux)

    chmod 755 altair-panel-mac (For MacOS)

    chmod 755 altiar-panel-freebsd (For FreeBSD)

## Building A Standalone Executable

To build a standalone executable for the application, you will need to install
pyInstaller. You can run the install.sh script to build the executable. The
executable will be in the **dist/** directory, in you project.


