# Tools for simulating taxi protocols

This tool currently implements the GWP5043 format of taxi data, notifying of fare start/end etc

It is a very simple POC based around send data over a serial connection, in the lab this is a serial over IP connection however this can be any seriaal connection

![Serial Over IP](https://github.com/scattym/python-tool-taxisim/blob/master/misc/SerialOverIP.png?raw=true)

Although it's just using the python serial lib so will work directly also.

![Serial](https://github.com/scattym/python-tool-taxisim/blob/master/misc/Serial.png?raw=true)

# Install

```python
python setup.py install
```
# Run

```python
$ taxisim -h 
usage: taxisim [-h] [-a] [-b] [-c] [-d DEVICE] [-n] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -a, --occupied        Send occupied message. (default: False)
  -b, --vacancy         Send vacancy message. (default: False)
  -c, --print-command   Send print message. (default: False)
  -d DEVICE, --device DEVICE
                        The serial port device to open. Defaults to lab serial2ip entry. (default: rfc2217://10.1.1.6:9990)
  -n, --dry-run         Don't send data on serial link. Just print to the screen. (default: False)
  -v                    Increase the logging level. Can specify this option multiple times for more detail. (default: 0)
```
