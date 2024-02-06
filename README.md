# CONEL Assignment task 5 Project 1
Assignment for beginner Python class

## Project requirements
>Project 1: Patient Registration System
>
>Create a patient registration system that allows users to add new patients to a record system. The system should prompt the user for patient details such as name, age, gender, and contact number. All patient records should be stored in a file. Implement functions for adding patients and displaying patient information. Test the system with sample data.
>
>Documentation Requirements:
>1. README Files:
>    - Create a separate README file for each project. 
>    - Include a brief project overview and purpose.
>    - Clearly list the functionalities of the project.
>    - Provide step-by-step instructions on how to run the Python code.
>    - Mention any external libraries or dependencies required.
>    - Include sample input and expected output.
>1. Code Comments:
>    - Include comments throughout your code to explain the purpose of functions, loops, and any complex logic.
>    - Use meaningful variable and function names to enhance code readability.
>1. Testing:
>    - Describe the testing process for your projects.
>    - Provide examples of test cases and their expected outcomes.

## Implementation notes and dependencies
We will use the library [Rich](https://github.com/Textualize/rich) for outputting to the console for a nicer UI.

Because the project requires that the patient data be stored in a file, we will use the inbuilt library `csv` to write to a text file in a CSV format. The patient data will be stored in a file called `patient_data.csv` in the project root directory, which will be created on the first run of the script.

For reading the `.env` configuration file, we use `python-dotenv`.

For testing requirements, we will use the inbuilt library `unittest`.

The requirements are included in the `requirements.txt` file, you will use this file when setting up your Python environment.

## Instalation instructions
We recommend you use Windows PowerShell so that the instructions work without changes.

Assuming you have git installed you can clone the project by running

```
git clone https://github.com/mendelcyprys/conel-assignment-5-project-1.git
``` 

Otherwise you can download the files from github.

Then move into the created directory by running

```
cd conel-assignment-5-project-1
```

Then create a virtual environment by running

```
python -m venv .venv
```

Note that this step isn't crucial, and you may need to install `venv` or use a different executable name like `python3`.

If you have installed the virtual environment from the previous step, you will need to activate it in the console by running (for Windows PowerShell)

```
.venv/Scripts/Activate.ps1
```

Now install the project requirements by running

```
pip install -r requirements.txt
```

Rename `.env-example` to `.env` by running

```
mv .env-example .env
```

To test that the installation has worked, you can now try to run the unit tests

```
python -m unittest discover
```

You can run the program by running

```
python main.py
```

Finally you can deactivate the virtual environment by running

```
deactivate
```

## Sample run

![First image](/docs/images/1.png)

![Second image](/docs/images/2.png)