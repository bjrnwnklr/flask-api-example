# flask-api-example
Simple Flask API example, based on my [Flask Docker template](https://github.com/bjrnwnklr/flask-docker).

# Sources

[Flask-RESTful documentation](https://flask-restful.readthedocs.io/en/latest/)
[Miguel Grinberg - Designing a RESTful API using Flask-RESTful](https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful)
[Flask-SQLAlchemy - Quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)


# Directory structure

```
flask-api-example
|   .env
|   .gitignore
|   boot.sh
|   config.py
|   docker-compose.yml
|   docker-requirements.txt
|   Dockerfile
|   LICENSE
|   MANIFEST.in
|   README.md
|   requirements.txt
|   setup.py
|       
\---flaskapi
    |   forms.py
    |   routes.py
    |   __init__.py
    |   
    +---static
    |       style.css
    |       
    +---templates
    |       index.html
    |
    \---tests
            apitest.py
```

# API key

Generate an API key using the `uuid.uuid4()` function. This generates a random UUID. A string representation can be generated using `str(uuid)`.


# Build and run

Build and run the Docker container with the following commands:

```shell
$ docker build --tag flask-api-example .
$ docker run --name flask --detach --publish 8000:5000 --env-file=.env --rm flask-api-example
```



# Error messages

If you receive the following error message when running the Docker container:

`standard_init_linux.go:219: exec user process caused: no such file or directory`

Change the CRLF in VSCode to LF and save the `boot.sh` file with a Unix line ending.