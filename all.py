import pickle
import subprocess
from cmd import Cmd

class MyPrompt(Cmd):
	def __init__(self):
		super(MyPrompt, self).__init__()
		with open('gps.pkl', 'rb') as r:
			self.gps_dict = pickle.load(r)

	def do_exit(self, inp):
		print("Bye Bye")
		return True

	def do_search_logno(self, inp):
		logno = input('logno (eg: 7477): ')
		subprocess.call('node final.js '+str(logno), shell=True)

	def do_search_title(self, inp):
		title = input('title (eg: 甘蔗): ')
		subprocess.call('node final_title.js '+str(title), shell=True)

	def do_visualize(self, inp):
		# TODO
		logno = input('logno (eg: 7477): ')
		print('visualize on google map')
		if logno in self.gps_dict:
			obj = self.gps_dict[logno]
			if obj is None:
				print('Location not found!')
			else:
				print('Number of location: {}'.format(len(obj)))
				for x in obj:
					print(x)
		else:
			print('Logno not found!')

	def default(self, inp):
		print("unknown input: {}".format(inp))

def doormatPattern(rows, columns): 
    width = columns 
    for i in range (0, int (rows / 2)): 
        pattern = "|*|" * ((2 * i) + 1) 
        print (pattern.center (width, '-')) 
    print ("Blockchain Search Engine".center (width, '-')) 
    i = int (rows / 2) 
    while i > 0: 
        pattern = "|*|" * ((2 * i) - 1) 
        print (pattern.center (width, '-')) 
        i = i-1
    return

if __name__ == '__main__':
    rows = 7
    columns = rows * 10 
    doormatPattern(rows, columns) 
    MyPrompt().cmdloop()
