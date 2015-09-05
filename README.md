Pymal
==============

Pymal is a Python malware with base64 encoded communication.

# How to use 

You have to generate an executable to send to the victim :

## Generating malware Executables with PyInstaller:

Linux: sudo apt-get install python2.7 build-essential python-dev zlib1g-dev upx
Windows: http://www.activestate.com/activepython (fully packaged installer file)

Install Pywin32, Setuptools, PyInstaller

After install:

Next we can run the following command to generate the python executable script: python pyintaller.py –onefile malware.py

This will process the python script, pull the necessary import dependencies, and generate a new folder containing a malware.txt, a malware.spec, and a malware.exe. The malware.exe can now be used, and the .txt and .spec can be removed.

After building the executable:

The Python script has now been compiled into a Windows PE file and can be executed on Windows without using a Python interpreter.  This allows you to more easily move your code between instances of Windows without worrying about dependencies.

Send The malware.exe to your friends (don't do that !!!)

## Run the server

Before sending the malware.exe to your friend you have to setup your server to listen to incomming connection from the Client (Victim). Change the IP and port and Run :

```
python Commandserver.py
```
