# 🧩 Modules and Pip in Python

## 📘 Introduction

**Modules** are like a **code library** which can be used to **borrow the code written by somebody else** in our Python program.  
They help us reuse existing functionality instead of writing everything from scratch.

There are two types of modules in Python:

---

## 🧠 Types of Modules

### • Built-in Modules - 
                        These modules are **ready to import and use** and **ship with the Python interpreter**.  
    There is **no need to install** such modules explicitly.

✅ **Examples:**
- `math`  
- `random`  
- `os`  
- `datetime`

**Example Usage:**
```python
import math
print(math.sqrt(25))  # Output: 5.0
```

###  • External Modules -
                        These modules are imported from a third party file or can be installed using a package manager lilie pip or conda. Since this code is written by someone else, we can install different versions of a same module with time
   • we can install modules and packages using 
    pip install package/module_name
        ex 1- pip install pandas    
        ex 2- pip install scikit-learn
        ex 3 - pip install Tensorflow

 • Using a modules in python(usage)
we use the import syntax to import a module in python . here is the example
```
import pandas
# read and work with the file names 'words.csv'
pandas.read_csv('words.csv')

````

similarly we can install other modules and look into their documentation for usage instructions. we will find ourselves doing this in the 
later part of this course
