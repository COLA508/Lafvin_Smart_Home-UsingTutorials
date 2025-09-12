Installing The ESP32 Core Board In The Arduino IDE
==================================================

------------------------------------
Add additional boards manager URL
------------------------------------

1. Open the Arduino IDE, click "File" -> "Preferences" in the upper left corner, and copy and paste the following address into the specified input box on the pop-up page.

**https://espressif.github.io/arduino-esp32/package_esp32_index_cn.json**

.. image:: _static/18.URL.png

.. image:: _static/19.URL.png

.. image:: _static/20.URL.png 

2. After entering the URL, click OK.

.. admonition:: Precaution
   :class: note

   After completing this step, you need to close and reopen the Arduino IDE.

------------------------------------
Download the core package for the ESP32 development board
------------------------------------

1. Open the Arduino IDE,Click the second icon on the left to pop up the "BOARDS MANAGER" page.

 .. image:: _static/21.ESP32_CORE.png

2. Enter "ESP32" in the input box and press Enter to search.

3. Find the core package titled "esp32 by Espressif Systems", select version 3.2.0 from the drop-down menu, and click "install" to download and install it.

 .. image:: _static/22.ESP32_CORE.png

4. Please wait for the download progress bar in the lower right corner to complete until the download is complete.

 .. image:: _static/23.ESP32_CORE.png

5. When the download is complete, the message "Successfully installed platform esp32:3.2.0" will be displayed.
 
  .. image:: _static/24.ESP32_CORE.png

6. Check if the download is successful.
Click "Tools"->"board"->"esp32" to check whether there is an esp32 development board available for selection.

  .. image:: _static/25.ESP32_CORE.png



    .. admonition:: Precaution
   :class: note

   We recommend installing ESP32 Core Package version 3.2.0, or using version 3.0 or later. 
   Older versions may be incompatible with the libraries used in this tutorial, causing program errors. 
   If you have an earlier version installed, uninstall it and then reinstall version 3.2.0 of the ESP32 Core Package.
