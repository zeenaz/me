TODO: Reflect on what you learned this week and what is still unclear.

### 1 - what is IO mean?

Input and Output

### 2 - file type setup

"The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be:

- 'r' when the file will only be read,
- 'w' for only writing (an existing file with the same name will be erased),
- 'a' opens the file for appending; any data written to the file is automatically added to the end.
- 'r+' opens the file for both reading and writing.

The mode argument is optional; 'r' will be assumed if it's omitted."

### 3 - close the file

close the file and save it, otherwise errors occurring

`../folderpath` it means folder up

### 4 - with block

1. encoding: `utf-8` what is this?

Unicode, you can put emoji here!

1. with block, you don't have to close it

```python
def be_cool_and_safe_for_ever(name, file_path):

mode = "w"
with open(file_path, mode, encoding="utf-8") as history_book:
	history_book.write(name + "try to write 🙃 ✔️ 🐼 ⨀ ½ ∞ ∴")
```

### 5 - read file

1. \n means new line
2. \t means new tab
3. this function do not change the file, only read

```python
def who_is_cool(file_path):
	mode = "r"
	with open(file_path, mode, encoding="utf-8") as history_book:
		response = history_book.read()

	print("f"historians have recored that:\n\t{response}")
```

### 6 -

Save some json to a file.

Args:

`something_for_your_kids_to_find` (`dict`): A dictionary of facts.

`file_path` (`str`): The path to where you want to save the `json`.

```python
def bury_time_capsule(something_for_your_kids_to_find, file_path):

```
