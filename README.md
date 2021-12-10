# List Capture Devices on Windows using DirectShow
This is a simple and lightweight Python extension that allows developers to enumerate capture devices. The device names can be used to open capture devices with, for instance, [PyAV](https://pyav.org/). The extension can be used as follows:

```python
from windows_capture_devices import get_capture_devices
import av

if __name__ == "__main__":
    device_list = get_capture_devices()

    # TODO: pyav example 
```

We use this extension in the `WebcamSource` of our [**multisensor-pipeline**](https://github.com/DFKI-Interactive-Machine-Learning/multisensor-pipeline).

## Setup

* From PyPI (recommended)
  ```commandline
  pip install windows-capture-devices
  ```
* From source (we recommend to use an Anaconda environment for building the package)
  ```commandline
  python setup.py build install
  ```

## Credits
This repository is forked from https://github.com/yushulx/python-capture-device-list.