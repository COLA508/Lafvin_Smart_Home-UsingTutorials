Install CH340 Driver
===========================
 - The ESP32 controller board used in this kit uses the CH340C USB-to-serial chip, so you need to install the corresponding driver. 

 - If you connect the motherboard to the computer before installing the driver, the computer will not be able to correctly recognize the motherboard and you will see the following interface in the Device Manager.

 .. image:: _static/12.CH340.png

Downloading the driver
----------------------

1. Visit the official website of CH340 Driver `CH340 Driver <https://www.wch.cn/products/ch340.html>`_

2. Select the version that matches your computer system to download. This tutorial uses Windows 11 as an example.

  .. image:: _static/10.CH340.png

3. Select the first Windows version, enter the download page and click the 'Download' button to start downloading.

  .. image:: _static/11.CH340.png

 - In addition, we have prepared the installation package for you, you can directly click the link below to download `Installation Package <https://www.dropbox.com/scl/fi/j6oue7pij59qyy9cwqclh/CH34x_Install_Windows_v3_4.zip?rlkey=xttzwik1qp56naxw8v7ostmkq&e=1&st=kcy0xjl1&dl=0>`_



Installing the driver
----------------------
1. After downloading the driver, open it and click Install.
  
  .. image:: _static/13.CH340.png


2. After successful installation you should see this message.

  .. image:: _static/14.CH340.png
    

.. admonition:: Precautions

  In some cases, you may need to restart Windows after the driver installation is complete to ensure that the driver takes effect.


Checking Correct Driver Installation in Device Manager
-------------------------------------------------------

Once the driver is installed correctly, connect the development board to the computer and you will see the corresponding name and port number in the port settings. For example, the ESP32 development board in this example is connected to COM28


  .. image:: _static/15.CH340.png


Checking Correct Driver Installation in Arduino IDE
-------------------------------------------------------

After connecting the ESP32 development board to your computer, open the Arduino IDE. Go to Tools -> Port and select the corresponding COMx port. 
Make sure this port number matches the one you saw in the Device Manager in the previous step.

 .. image:: _static/16.CH340.png



.. admonition:: Precautions

If you can't find the Arduino CH340 device in your computer's device manager or the Arduino IDE, the driver isn't installed correctly. You can try the following solutions:
 - Uninstall the driver, restart your computer, and then reinstall it.

  .. image:: _static/17.CH340.png

 - Change the USB port or use a different computer.
 - Use a USB cable that supports data transfer （not just power）.
