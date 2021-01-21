## ALPS plotter tools
These code is used for plot HP-GL files on several older plotters and plotter typewriters which uses ALPS 4 pen plot mechanism

The plot.py is used for SHARP CE-515P plotter, which has standard parallel port and (partially) support DXY-GL

The plot-fortec.py is used for Fortec ET-318C plotter typewriter, which also has standard parallel port and some DXY-GL support.

Both machine has moving range from 999 to 999, like if you transfer command “M1000,1000” it will not work, the CE-515P has approx. 100dpi and ET-318C is about 200dpi

I use them in my Inkspace workflow which can save HP-GL for print, make sure you enter the correct dpi and check the “Center zero point” option.

The usage is pretty simple, just run the script with python like:

    python plot.py columbia.hpgl output.txt
And the you will get the “output.txt” with all DXY-GL command sequence for plotting, include initialize and re-center command added by the script.

And then you can send then to your parallel port, personally I’m using an common USB-Parallel printer adapter

    cat output.txt > /dev/usb/lp0
Since in the Linux parallel port is a device file, you can bypass the step of write the command sequence directly to parallel port, for example

    python plot.py columbia.hpgl /dev/usb/lp0
Since there are several other plotters and plotter typewriters are using same ALPS 4 pen mechanism, for example:
- Printers: Atari 1020, Commodore 1520, SHARP CE-516p, Tandy GCP-115
- Plotter typewriters: Brother BP-30, Panasonic RK-P400C

These machine might use with these scripts with very small modification, but I didn’t tested because I don’t have all the hardware.