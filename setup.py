from setuptools import setup, find_packages
        
setup(
    name="swagger-yamltohtml",
    version="0.0.3", 
    author="Matheus Camilo Dev",
    author_email="matheuscamilovelanzuelameira@gmail.com",
    description="Converts a swagger-generated yaml into html code",
    long_description="""
# How to use
## Import and configurate into your code:
example.py
```py
from swagger_yamltohtml.yaml2html import convertYamlInHtml
from os import dirname, realpath
...
converted_html = convertYamlInHtml(dirname(realpath(__file__)))
...

```
## Flags
- ### --yaml-file <yaml-file-path>
To select yaml file to convert in html. Without this flag, input mode is ON!

Ex: 
```
python3 example.py --yaml-file example.yaml
```

<br>

- ### --html-file <html-file-path>
To select base html file for convert. This file must have the same structure as the base. Without this flag, is used default html file!

Ex:
```
python3 example.py --html-file example.html
```""",
    long_description_content_type="text/markdown",
    url="https://github.com/matheus-camilo-dev/swagger-yaml-to-html",
    project_urls={
        "Bug Tracker" : "https://github.com/matheus-camilo-dev/swagger-yaml-to-html/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        'swagger_yamltohtml':[ 
            'static/swagger.html' 
        ]
    },
    install_requires=[ 'PyYAML' ],
    python_requires=">=3.6",
)
