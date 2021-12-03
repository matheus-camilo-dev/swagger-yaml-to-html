# Swagger Standalone

This package converts yaml generated by swagger into html code!

### To build and send package

First, configure and start the python virtual environment!

Remove `dist` and `src/swagger_yamltohtml.egg-info` folders, if they exist:
```
rm -R dist
rm -R src/swagger_yamltohtml.egg-info
```

At least, change the version number in `setup.py`.

Install/Update this packages:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
```

Run in the root directory for build package:
```
python3 -m build
```

## Using test.pypi

After, run the command and insert your test.pypi credentials or your api token:
```
python3 -m twine upload --repository testpypi dist/*
```

- ### To Install package

To install run below code:
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps swagger-yamltohtml --extra-index-url https://pypi.org/simple PyYAML
```

## Using py.pi

After, run the command and insert your test.pypi credentials or your api token:
```
python3 -m twine upload dist/*
```

- ### To Install package

To install run below code:
```
python3 -m pip install swagger-yamltohtml
```

## How to use
### Import and configurate into your code:
example.py
```py
from swagger_yamltohtml.yaml2html import convertYamlInHtml
from os import dirname, realpath
...
converted_html = convertYamlInHtml(dirname(realpath(__file__)))
...

```
### Flags
- #### --yaml-file <yaml-file-path>
To select yaml file to convert in html. Without this flag, input mode is ON!

Ex: 
```
python3 example.py --yaml-file example.yaml
```

<br>

- #### --html-file <html-file-path>
To select base html file for convert. This file must have the same structure as the base. Without this flag, is used default html file!

Ex:
```
python3 example.py --html-file example.html
```