import dlib
import cv2
import imutils

# 開啟影片檔案
cap = cv2.VideoCapture("V12.avi")
#cap = cv2.VideoCapture(0)

# 取得畫面尺寸
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 使用 XVID 編碼
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
# 建立 VideoWriter 物件，輸出影片至 output.avi，FPS 值為 20.0
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

# 使用 DIB 編碼
# fourcc = cv2.cv.CV_FOURCC("D","I","B"," ")
# 建立 VideoWriter 物件，輸出影片至 output.avi，FPS 值為 20.0
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# Dlib 的人臉偵測器
detector = dlib.get_frontal_face_detector()

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
    #print("cap open")
    ret, frame = cap.read()


    # 偵測人臉
    face_rects, scores, idx = detector.run(frame, 0)
    #face_rects = detector(frame, 0) #圖片

    # 取出所有偵測的結果
    for i, d in enumerate(face_rects):
        x1 = d.left()
        y1 = d.top()
        x2 = d.right()
        y2 = d.bottom()
        text = "%2.2f(%d)" % (scores[i], idx[i])
        
        # 以方框標示偵測的人臉
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4, cv2.LINE_AA)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
        
        # 標示分數
        cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_DUPLEX,
                0.7, (255, 255, 255), 1)

    # 寫入影格
    # out.write(frame)
    
    # 顯示結果
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()