import cv2
import mediapipe as mp
import time


class FaceMeshDetector:
    def __init__(self, staticMode=False, numFaces=1, reLandmarks=False, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode =staticMode
        self.numFaces = numFaces
        self.reLandmarks = reLandmarks
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.numFaces, self.reLandmarks, self.minDetectionCon, self.minTrackCon)
        self.drawSpecs = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)

    def findFaceDetector(self, img, draw=True):

        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawSpecs, self.drawSpecs)

                face = []
                for id, lm in enumerate(faceLms.landmark):
                    #print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 0.5, (0, 255, 0), 1)

                    #print(id, x, y)
                    face.append([x, y])
                faces.append(face)
        return img, faces


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceMeshDetector()
    pTime = 0
    while True:
        success, img = cap.read()
        img, faces = detector.findFaceDetector(img)
        if len(faces)!=0:
            print(len(faces))

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(10)


if __name__=="__main__":
    main()