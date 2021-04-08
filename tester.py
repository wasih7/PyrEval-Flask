import requests
f = open('/home/wasih7/Test/PyrEval/Raw/peers/S1.txt', 'r')
summ = f.read()

files = {'answer': (summ, 'ans ans')}
response = requests.post('http://localhost:5000/getIndividualScore', data = files)

