import os
import sys
from termcolor import colored
if sys.version_info[0] == 2:
    import ConfigParser as configparser
else:
    import configparser
    PYTHON_VERSION = 3
#first locate stanford directory
pyreval_dir = os.path.join(os.getcwd(), 'PyrEval')

config = configparser.ConfigParser()
config.read(os.path.join(pyreval_dir, 'parameters.ini'))
stanford_dir = config.get('Paths', 'StanfordDir')


files = os.listdir(stanford_dir)
print(files)
coreNlpDir = ""
for filename in files:
	if (os.path.isdir(os.path.join(stanford_dir, filename)) and 'stanford' in filename):
		coreNlpDir = os.path.join(stanford_dir, filename)
		break
print (coreNlpDir)
if coreNlpDir != "":
	os.chdir(coreNlpDir)
	command = 'java -Xmx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000'
	os.system(command)

else:
	text = colored('No Stanford CoreNLP Present!\n\n', 'red', attrs = ['bold'])
	print(text)
