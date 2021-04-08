## Installation

You just need to install [flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)! If you have python 3, you just need to run `pip install flask` or use `pip3`, depending on your setup.

## Run

Following flask's [basic tutorial](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application), run 
```
export FLASK_APP=hello.py
flask run
```

## Requests

An easy tool to make different kinds of test  requests is [Postman](https://www.postman.com/downloads/). Here's what the request configuration looks like for the current flask code setup ![flask setup image](https://github.com/Visheshk/pyreval-flask/raw/main/Screen%20Shot%202021-04-03%20at%205.44.36%20PM.png). 
A simpler way to test the current setup is to use curl: 
```
curl -X POST -F "question=test question" -F "answer=ans ans" http://localhost:5000/test
```

## How it works
Currently, the server checks for POST on /test, and tries to parse it as a form data. It passes the answer field of the form data to the imported script test.py's function. testfn from test.py checks that it was given a string, then concatenates ttt at the ending and prints it to the console.

## Attaching to pyreval
My imagined expectation is that instead of import test, the server script will import pyreval, and given specific POST requests (for instance, to /getBulkScore, or to /getIndividualScore), will call specific functions in the pyreval script. The getIndividualScore corresponding function will take the answer string (and possibly even question ID or question-category-ID, if different sets of questions are measured against different pyramids), and return the corresponding score related info. This return can be any python object and doesn't need to be a string. The notebook will handle the rest~

## Updates:

1. First, download PyrEval (from new_impl branch) and copy the folder to this repo/directory.
2. PyrEval now has a function in pyreval_flask,py, getIndividualScore(str) which will take as an input a text summary (string) and will return a dictionary structure which just contains the raw scores (coverage, quality, etc.) as of now.
3. PyrEval was first made as a package by adding, __init__.py to it. The parameters.ini file under PyrEval folder, then need to be modified as follows:
	1. The BaseDir argument should now point to the absolute location of PyrEval, i.e. /path/to/this/repo/PyrEval/
	2. An argument, PyramidPath is now added for entering the absolute path of the pyramid file on the local system. This is because at the time of scoring, no pyramid is built.
	3. An argument, NumModels has now been added which represents the number of reference summaries which were used to build the pyramid (under PyramidPath)
4. To run, first start the server using: flask run
5. Then, in another terminal, need to run the script: python3 tester.py:
	1. Edit line 2 (f = open('...')) according to the path of the input text file summary which needs to be scored
6. PyrEval will then be called and the steps will be run (split, decomposition, score) and the final results returned as an ordered dictionary
The above should run fine with Python3
