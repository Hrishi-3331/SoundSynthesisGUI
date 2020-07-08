# SoundSynthesisGUI

Steps to set up project:

1. Create a project directory. For example create a directory SoundProject.

2. Create a virtual environment inside the project directory dedicated to this project.For this, go to project directory and open terminal in directory by typing cmd or powershell on the address bar of directory.
Then inside terminal write following commands:

```sh
  virtualenv pyenv
```

3. Once virtual environment is created clone the project in root directory. (Make sure you have git installed in your PC)

```sh
  git clone https://github.com/Hrishi-3331/SoundSynthesisGUI.git
```

After cloning your project structure should look like this:

```sh
  SoundProject
   | - pyenv
   | - SoundSynthesisGUI
```

4. Open the cloned project in pycharm. In the project settings, set the Python interpretor to the virtualenv that we created i.e. pyenv.

5. Inside the terminal of Pycharm enter the following command:

```sh
  pip install requirements.txt
```

Project is now ready to run. Run the main file to test the sound. To test the GUI run interface.py inside GUI directory.


Let me know if you faace any issues while setting up the project on your PC.
