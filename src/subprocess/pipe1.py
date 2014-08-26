import subprocess
childOut = subprocess.Popen(["python","out.py"], stdout=subprocess.PIPE)
childIn = subprocess.Popen(["python", "in.py"], stdin=childOut.stdout, stdout=subprocess.PIPE)
print childIn.stdout.read()
