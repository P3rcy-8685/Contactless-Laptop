import cv2, mediapipe as mp, math,time, pyautogui
from ctypes import cast, POINTER
from numba import jit, cuda
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
cap=cv2.VideoCapture(1)
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
temp=100
choice=0
x=50
x1,y=pyautogui.size()
#@jit(target ="cuda")                        
def third():
    pyautogui.moveTo(x1*(xList[8]/w),y*(yList[8]/h))
#@jit(target ="cuda")                        
def drag():
    pyautogui.click(x1*(xList[8]/w),y*(yList[8]/h),1,button="left")        
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
minv,maxv,curr=volume.GetVolumeRange()
def dis(x1,y1,x2,y2):
    return math.hypot(x1-x2,y1-y2)
lx8=[]
lx0=[]
lx5=[]
ly8=[]
ly5=[]
ly0=[]
lx12=[]
lx16=[]
lx20=[]
ly12=[]
ly16=[]
ly20=[]
lx4=[]
ly4=[]
while temp>=0:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    if results.multi_hand_landmarks:
        temp-=1
        if results.multi_hand_landmarks:
                xList=[]
                yList=[]
                for i in results.multi_hand_landmarks:
                    for id,lm in enumerate(i.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        xList.append(cx)
                        yList.append(cy)
                    lx4.append(xList[4])
                    ly4.append(yList[4])
                    lx8.append(xList[8])
                    lx0.append(xList[0])
                    lx5.append(xList[5])
                    lx12.append(xList[12])
                    lx16.append(xList[16])
                    ly12.append(yList[12])
                    ly16.append(yList[16])
                    lx20.append(xList[20])
                    ly20.append(yList[20])
                    ly8.append(yList[8])
                    ly0.append(yList[0])
                    ly5.append(yList[5])
x4=sum(lx4)/100
y4=sum(ly4)/100
x8=sum(lx8)/100
x0=sum(lx0)/100
x5=sum(lx5)/100
x12=sum(lx12)/100
x16=sum(lx16)/100
x20=sum(lx20)/100
y8=sum(ly8)/100
y0=sum(ly0)/100
y5=sum(ly5)/100
y12=sum(ly12)/100
y16=sum(ly16)/100
y20=sum(ly20)/100
ind=dis(x8,y8,x0,y0)
mid=dis(x12,y12,x0,y0)
ring=dis(x16,y16,x0,y0)
pink=dis(x20,y20,x0,y0)
palm=dis(x5,y5,x0,y0)
vol=math.hypot(x4,y8,x8,y4)
print("It's now ready to use")
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
            allHands=[]
            for handtype,handlms in zip(results.multi_handedness,results.multi_hand_landmarks):
                myHand={}
                lmList=[]
                xList=[]
                yList=[]
                for id,lm in enumerate(handlms.landmark):
                    h, w,c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([cx,cy])
                    xList.append(cx)
                    yList.append(cy)
                myHand["lmList"]=lmList
                if handtype.classification[0].label=="Right":
                    myHand["type"]="Left"
                else:
                    myHand["type"]="Right"
                allHands.append(myHand)
            if handtype.classification[0].label=="Right":
                if (dis(xList[16],yList[16],xList[0],yList[0])/dis(xList[5],yList[5],xList[0],yList[0]))>round(ind/palm,1)-0.2:
                    choice=3
                elif (dis(xList[12],yList[12],xList[0],yList[0])/dis(xList[5],yList[5],xList[0],yList[0]))>round(ind/palm,1)-0.2:   
                    pyautogui.hotkey('winleft', 'd')
                    time.sleep(0.5)
                elif (dis(xList[8],yList[8],xList[0],yList[0])/dis(xList[5],yList[5],xList[0],yList[0]))>round(ind/palm,1)-0.2:
                    choice=1
            if choice==0:
                cv2.putText(img=img, text=str("Nothing selected"),org=(60,60), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
            if choice==1:
                cv2.putText(img=img, text=str("Volume Control"),org=(400,400), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
            if choice==2:
                cv2.putText(img=img, text=str("Show desktop"),org=(400,400), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
                
            if choice==3:
                cv2.putText(img=img, text=str("Mouse Control"),org=(400,400), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)   
            if handtype.classification[0].label=="Left":
                if choice==1:
                    if len(allHands)==2:
                        pass
                    else:
                        cv2.circle(img,((xList[8]+xList[4])//2,(yList[8]+yList[4])//2),12,(255,255,255),cv2.FILLED)
                        l=math.hypot(xList[8]-xList[4],yList[8]-yList[4])
                    
                        cv2.line(img,(xList[8],yList[8]),(xList[4],yList[4]),(255,255,255),3)
                        if l<40:#40 is the minimum value
                            cv2.circle(img,((xList[8]+xList[4])//2,(yList[8]+yList[4])//2),12,(0,0,255),cv2.FILLED)
                            #max is 200 so range is 160 for minv to maxv.... so slope will be
                        slope=(maxv-minv)/140
                        x=(l-200)*slope
                        if x>maxv:
                            x=maxv
                        elif x<minv:
                            x=minv
                        volume.SetMasterVolumeLevel(x,None)
                        x=100+(100)/(-minv)*(x)
                elif choice==3:
                    third()
                if len(allHands)==2 and choice==3:
                    drag()
    cv2.putText(img=img, text=str(x),org=(60,60),
                fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
