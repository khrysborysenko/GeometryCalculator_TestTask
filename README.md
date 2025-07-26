# GeometryCalculator_TestTask

Geometry Calculator is a console application that parses text input describing 2D geometric shapes and calculates their area and perimeter. 

Supports the following shapes:
 - Square
 - Rectangle (axis-aligned)
 - Circle
 - Triangle

A project structure that is easy to extend to add more shapes or functions:

<img width="276" height="457" alt="image" src="https://github.com/user-attachments/assets/90784690-ef15-41e1-bc6a-8cc49c00ca0f" />

After running main.py, the user will be prompted to choose the input type (keyboard or file). If no file name is entered, the program will automatically use the default data file, process the input, and display the calculation results:

<img width="448" height="491" alt="image" src="https://github.com/user-attachments/assets/0e48bff9-4388-4cd2-acec-bf102d7832ac" />

When using the program, it is important to enter data in the correct form. Otherwise, the program may perceive it as invalid data (but you will be prompted to try entering again)
Examples of correct input: 
 - Square TopRight 1 1 Side 1
 - Rectangle TopRight 2 2 BottomLeft 1 1
 - Circle Center 1 1 Radius 1
 - Triangle Point1 0 0 Point2 1 1 Point3 2 0

A total of 25 tests were created and successfully executed to verify the correct functionality of the program, including its core methods and validation checks for input data:

<img width="1192" height="181" alt="image" src="https://github.com/user-attachments/assets/81e7d634-d8d2-4805-8ac9-cfeb54de3e11" />
