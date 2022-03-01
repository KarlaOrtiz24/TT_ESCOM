import cv2
from pymongo import MongoClient

cliente = MongoClient('localhost')
db = cliente['KAYI']
senas = db['Señas']

documento = senas.find({})

n = 53
print (documento[n]['nombre'])
capture = cv2.VideoCapture(documento[n]['data'])

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        cv2.imshow(documento[0]['nombre'], frame)
        if (cv2.waitKey(30) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()