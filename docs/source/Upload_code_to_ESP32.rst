Upload Code To ESP32
============================

After completing the above steps, ensure that the CH340 serial port driver has been installed, the ESP32 core package has been downloaded and installed, and the required library files have been imported. At this point, you can upload the code to the ESP32 development board and start running the program.

Download the code
--------------------

Click this link to download the sample code we have prepared in advance.
`Download Code <https://www.dropbox.com/scl/fi/j6oue7pij59qyy9cwqclh/CH34x_Install_Windows_v3_4.zip?rlkey=xttzwik1qp56naxw8v7ostmkq&e=1&st=kcy0xjl1&dl=0>`_

Click "File"->"Open" in sequence. In the pop-up page, locate the storage location of the code you just downloaded, select the corresponding code, and click the 'Open' button to complete the opening.

.. image:: _static/36.upload.png

.. image:: _static/37.upload.png  


.. admonition:: Precaution
   :class: note

   - If the folder name you downloaded the code to doesn't match the code file name, a prompt will pop up when you import the code, asking if you want to 'create a folder with the same name and move the file into it'. Select 'OK' to confirm. 
   - If this prompt doesn't appear, you can ignore it. 

   .. image:: _static/38.upload.png

Select a development board
--------------------------

Select "Tools"->"Board"->"esp32"->"ESP32 Dev Module" in sequence.

.. image:: _static/33.upload.png


Select the  serial port 
--------------------------

Select the correct serial port and click "Tools" -> "Port" -> "COMx". COMx should be consistent with the port of the development board that is actually connected.

.. image:: _static/34.port.png


Check whether the serial port and development board are selected correctly
------------------------------------------------------------------------------
 - Please refer to the diagram to check whether the selected serial port and development board model are correct. 
 - If you find that the selection is wrong or not selected, please return to the previous steps and set it again.

 .. image:: _static/35.upload.png

Upload Code
----------

Click the upload icon in the Arduino IDE and the system will automatically upload the code to the ESP32 development board.

 .. image:: _static/39.upload.png

The Output window of the Arduino IDE will display the progress of the code compilation and upload. The compilation process may be slow, so please be patient and wait until the code is successfully uploaded to the development board.

 .. image:: _static/40.upload.png



When the Arduino IDE Output window displays the message "Leaving... Hard resetting via RTS pin...", the code has been uploaded successfully. Press the RST reset button on the ESP32 development board to start running the program.

 .. image:: _static/41.upload.png




.. admonition:: Precaution
   :class: note

 If code fails to upload to the ESP32 development board, follow these steps to troubleshoot:
 - Confirm that the port selected in Tools -> Port in the Arduino IDE corresponds to the port of the connected ESP32 development board.
 - Confirm that the correct ESP32 development board model is selected in Tools -> Board.
 - Make sure the CH340 serial port driver (or other required USB driver) is correctly installed and that the development board is recognized in the device manager.
 - Try changing the USB port or USB data cable to ensure that it supports data transmission.
 - Confirm that the ESP32 core package is installed and all required libraries have been imported.
 - If the library version does not match the tutorial, compilation or upload failures may occur. Please use the recommended version.
 - Confirm that no other programs are using the serial port, such as the serial monitor or other serial tools.
 - If the upload fails, press the RST button on the ESP32 development board to try uploading again.
