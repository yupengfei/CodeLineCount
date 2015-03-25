import os

suffixList = ['java', 'xml', 'go', 'h', 'cpp', 'qml', 'js', 'html']

countMap = {}

def analysisFolder(path):
	fileList = os.listdir(path)
	for fileItem in fileList:
		# print(fileItem)
		if os.path.isfile(path + '/'+ fileItem):
			if '.' in fileItem:
				splitList = fileItem.split(".")
				if splitList[-1] in suffixList:
					print(fileItem)
					fp = open(path + '/' + fileItem)
					lines = fp.readlines()
					if splitList[-1] in countMap:
						countMap[splitList[-1]] += len(lines)
					else:
						countMap[splitList[-1]] = len(lines)
		else:
			analysisFolder(path + '/'+ fileItem)
					# print(type(fileItem))

if __name__ == '__main__':
	analysisFolder('/home/developer/Go/src/CGWorldlineWeb')
	print(countMap)