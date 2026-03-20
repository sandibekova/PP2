<<<<<<< HEAD

=======PP2 PROJECT
---
# Practice 6 – File Handling, Directories and Built-in Functions

## Overview

This project demonstrates basic Python concepts including file handling, directory management, and commonly used built-in functions.

---

## 1. File Handling

### write_files.py

This script creates and writes data to a file using the `open()` function with write mode `"w"`. If the file already exists, its content is overwritten. It also demonstrates append mode `"a"` to add new content to the end of the file without removing existing data.

File modes used:

* `"r"`: read
* `"w"`: write (overwrites file)
* `"a"`: append
* `"x"`: create (fails if file exists)

---

### read_files.py

This script demonstrates different ways to read file content:

* `read()` reads the entire file as a single string
* `readline()` reads one line at a time
* `readlines()` returns a list of all lines in the file

---

### copy_delete_files.py

This script uses:

* `shutil.copy()` to copy files
* `os.remove()` to delete files
* `os.path.exists()` to check if a file exists before attempting deletion

---

## 2. Directory Management

### create_list_dirs.py

This script demonstrates working with directories:

* `os.mkdir()` creates a single directory
* `os.makedirs()` creates nested directories
* `os.listdir()` lists files and folders in the current directory
* `os.getcwd()` returns the current working directory
* `os.chdir()` changes the current directory
* `os.rmdir()` removes an empty directory

---

### move_files.py

This script demonstrates:

* Moving files using `shutil.move()`
* Copying files using `shutil.copy()`
* Creating directories using `os.makedirs()`

---

## 3. Built-in Functions

### map_filter_reduce.py

This script demonstrates:

* `map()` applies a function to each element of a list
* `filter()` selects elements that satisfy a condition
* `reduce()` combines elements into a single value (requires `functools`)

---

### enumerate_zip_examples.py

`enumerate()` is used to iterate over a list while keeping track of the index.

`zip()` is used to combine elements from multiple lists into pairs.

Example output:

1. Alice scored 85
2. Bob scored 92
3. Charlie scored 78

---

### Type Checking and Conversion

* `isinstance()` checks the type of a variable
* `int()`, `float()`, and `str()` are used to convert between data types

Example:
A string value like `"100"` can be converted into an integer using `int()`.

---

## How to Run

Run each script using:

python file_handling/write_files.py
python file_handling/read_files.py
python file_handling/copy_delete_files.py
python directory_management/create_list_dirs.py
python directory_management/move_files.py
python builtin_functions/map_filter_reduce.py
python builtin_functions/enumerate_zip_examples.py

---

## Notes

* Using `with open()` ensures that files are automatically closed
* Always check if a file exists before deleting it
* `map()` and `filter()` return iterators, so they are often converted to lists
* `reduce()` must be imported from the `functools` module

---

## Conclusion

This project covers essential Python concepts including working with files, managing directories, and using built-in functions. These concepts are important for building real-world applications.
