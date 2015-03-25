import os
import codecs

suffixList = ['java', 'go', 'h', 'cpp', 'qml', 'js', 'html']

countMap = {}

def analysisFolder(path, coding):
	fileList = os.listdir(path)
	for fileItem in fileList:
		# print(fileItem)
		if os.path.isfile(path + '/'+ fileItem):
			if '.' in fileItem:
				splitList = fileItem.split(".")
				if splitList[-1] in suffixList:
					print(fileItem)
					fp = codecs.open(path + '/' + fileItem, encoding=coding)
					lines = fp.readlines()
					if splitList[-1] in countMap:
						countMap[splitList[-1]] += len(lines)
					else:
						countMap[splitList[-1]] = len(lines)
		else:
			analysisFolder(path + '/'+ fileItem, coding)
					# print(type(fileItem))

if __name__ == '__main__':
	analysisFolder('/home/developer/Downloads/i3/A_SRC', 'GB18030')
	print(countMap)