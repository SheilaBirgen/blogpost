# Pitcher

## Author
Sheila Birgen Jerono

## Technologies used
    -python
    -pip
    -html
    -css
    -flask
## Installation
To get the code..

1. Cloning the repository:

```bash
https://github.com/SheilaBirgen/blogpost
```

2. Move to the folder and install requirements

```bash
cd blogpost
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.6 manage.py server
```

Open the application on your browser `127.0.0.1:5000`.
## Description
A pitch app is an app that  enables one to sell out their  ideas within a minute
## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           | Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app pitches based on categories and commenting section |
| Select comment button |             **Comment**             |             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

## Known Bugs
There are no known bugs at the moment

## Support and contact Details
You can reach out to me through the github account SheilaBirgen
or on my email as jeronobergen@gmail.com
## CodeBeat Badge

[![codebeat badge](https://codebeat.co/badges/8e5b0d4f-c18b-48c9-a83f-c36390d8d2bd)](https://codebeat.co/projects/github-com-sheilabirgen-blogpost-master)

## License
|@2019 Sheila Birgen |
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)