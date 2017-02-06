
import numpy as np
import cv2


class IdentificadorFacial:

	def input_camera(self):
		idd = raw_input('Introduzca el ID del usuario: ')
		muestraInt = 0
		detector= cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
		cap = cv2.VideoCapture(0)

		while(True):
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			faces = detector.detectMultiScale(gray, 1.3, 5)
			if(len(faces)!=0):
				for (x,y,w,h) in faces:
					cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
					cv2.imwrite("dataSet/"+idd +'_'+ str(muestraInt) + ".jpg", gray[y:y+h,x:x+w])
					muestraInt+=1
			cv2.imshow('frame',img)
			# Si pulsa la letra q o a tomado mas de 20 fotos termina.
			if cv2.waitKey(10) & 0xFF == ord('q'):
				break
			# break if the sample number is morethan 20
			elif muestraInt>20:
				break
		# Cerramos la ventana y dejamos libre la webCam
		cap.release()
		cv2.destroyAllWindows()
			
	def input_folder():
		pass



if __name__ == '__main__':
	faciale = IdentificadorFacial()
	faciale.input_camera()