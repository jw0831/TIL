# 가상 환경에서 실
# open cv 설치
# pip install --upgrade opencv-contrib-python
# high-gui 에러 로인한 창 실행 imshow() 문제 해결
# pip install opencv-contrib-python-headless
import cv2
import numpy as np
img_path = "/Users/jinwon-kim/Desktop/python class/20.11.20/image/"

run = 22

if run == 1:
    # camera 실행
    print(cv2.__version__)
    capture = cv2.VideoCapture(1)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame) #VideoFrame 윈도우 창의 이름
        if cv2.waitKey(1) > 0: break

    capture.release()
    cv2.destroyAllWindows()
elif run == 2:
    image = cv2.imread(img_path+"dog1.jpg", cv2.IMREAD_ANYCOLOR)
    cv2.imshow("dog", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 3:
    capture = cv2.VideoCapture(img_path+"earth.mp4")
    # capture.isOpened()
    while True:
        if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open("image/earth.mp4")

        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)

        if cv2.waitKey(33) > 0: break

    capture.release()
    cv2.destroyAllWindows()
elif run == 4:
    src = cv2.imread(img_path+"dog2.jpg", cv2.IMREAD_COLOR)
    dst = cv2.flip(src, 0)

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 5:
    src = cv2.imread(img_path+"dog1.jpg", cv2.IMREAD_COLOR)

    height, width, channel = src.shape
    dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)
    dst2 = cv2.pyrDown(src)

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.imshow("dst2", dst2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 6:
    src = cv2.imread(img_path+"dog3.jpg", cv2.IMREAD_COLOR)

    dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.imshow("dst2", dst2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 7:
    src = cv2.imread(img_path+"dog2.jpg", cv2.IMREAD_COLOR)

    dst = src.copy()
    dst = src[100:600, 200:700]

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 8:
    src = cv2.imread(img_path+"dog3.jpg", cv2.IMREAD_COLOR)

    dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 9:
    src = cv2.imread(img_path + "dog3.jpg", cv2.IMREAD_COLOR)
    dst = cv2.bitwise_not(src)  # cv2.bitwise_and 연산자 or xor 등등

    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif run == 10:
    # 이진화
    src = cv2.imread(img_path+"dog1.jpg", cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 11:
    src = cv2.imread(img_path+"dog2.jpg", cv2.IMREAD_COLOR)

    dst = cv2.blur(src, (20, 20), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 12:
    src = cv2.imread(img_path+"dog1.jpg", cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(src, 100, 255)  # 컬러
    # 100 (임계값) 이하에 해당되는 가장자리는 제외하겠다
    # 255 이상에 포함된 가장자리는 가장자리로 포함

    # 회색으로 받음
    sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
    laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

    cv2.imshow("canny", canny)  # 윤곽선 (자동차 번호판 인식할때)
    cv2.imshow("sobel", sobel)
    cv2.imshow("laplacian", laplacian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 13:
    src = cv2.imread(img_path+"dog1.jpg", cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    cv2.imshow("h", h)
    cv2.imshow("s", s)
    cv2.imshow("v", v)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 14:
    #특정 색상만 출력
    src = cv2.imread(img_path+"fruits.jpg", cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
    upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
    added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

    red = cv2.bitwise_and(hsv, hsv, mask=added_red)
    red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

    cv2.imshow("red", red)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 15:
    src = cv2.imread(img_path+"fruits.jpg", cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    h = cv2.inRange(h, 8, 20)  # 범위 설정 : (단일채널이미지, 최소값, 최대값)
    # 8~20 사이는 주황색b
    orange = cv2.bitwise_and(hsv, hsv, mask=h)
    orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)

    cv2.imshow("orange", orange)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 16:
    src = cv2.imread(img_path+"ham.jpg", cv2.IMREAD_COLOR)
    b, g, r = cv2.split(src)
    inversebgr = cv2.merge((r, g, b))

    cv2.imshow("b", b)
    cv2.imshow("g", g)
    cv2.imshow("r", r)
    cv2.imshow("inverse", inversebgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 채널별로 나누고 합친다. (split & merge)
elif run == 17:
    # 넘파이로 활용
    src = cv2.imread(img_path+"ham.jpg", cv2.IMREAD_COLOR)
    # [높이, 너비, 채널]
    b = src[:, :, 0]  # b channel
    g = src[:, :, 1]  # g channel
    r = src[:, :, 2]  # r channel
    h, w, c = src.shape
    zero = np.zeros((h, w, 1), dtype=np.uint8)  # 1에 해당하는 부분이 0으로 채워진다.
    a = cv2.merge((b, g, zero))
    cv2.imshow("no red",a)  # red 채널 영역이 모두 흑백이미지로 변경됨
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 18:
    # drawing
    src = np.zeros((768, 1366, 3), dtype=np.uint8)

    cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)
    cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)
    cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)
    cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

    pts1 = np.array([[100, 500], [300, 500], [200, 600]])
    pts2 = np.array([[600, 500], [800, 500], [700, 600]])
    cv2.polylines(src, [pts1], True, (0, 255, 255), 2)
    cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)

    cv2.putText(src, "TEST", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)
    # 글자크기 2

    cv2.imshow("src", src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 19:
    # 영상 저장
    import datetime
    capture = cv2.VideoCapture(img_path+"earth.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    record = False

    while True:
        if (capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
            capture.open(img_path+"earth.mp4")

        ret, frame = capture.read()
        cv2.imshow("VideoFrame", frame)

        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        key = cv2.waitKey(33)

        if key == 27:
            break
        elif key == 26:
            print("캡쳐")
            cv2.imwrite(img_path + str(now) + ".png", frame)
        elif key == 24:
            print("녹화 시작")
            record = True
            video = cv2.VideoWriter(img_path + str(now) + ".avi", fourcc, 20.0,
                                    (frame.shape[1], frame.shape[0]))
        elif key == 3:
            print("녹화 중지")
            record = False
            video.release()

        if record == True:
            print("녹화 중..")
            video.write(frame)

    capture.release()
    cv2.destroyAllWindows()

elif run == 20:
    src = cv2.imread(img_path+"contours.png", cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binary = cv2.bitwise_not(binary)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    cv2.startWindowThread()
    for i in range(len(contours)):
        cv2.drawContours(src, [contours[i]], 0, (0, 0, 255), 2)
        cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
        print(i, hierarchy[0][i])
        cv2.imshow("src", src)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

elif run == 21:
    # 컵 사진의 코너 검출
    src = cv2.imread(img_path+"cup.jpg")
    dst = src.copy()
    #none type error는 경로상에 해당 이미지가 없을때 나타난다.
    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    # 단일 채널의 이미지 회색이 들어가야 한다. 현재 최대 100개의 코너를 찾겠다고 설정.
    # 0.01은 코너의 품질 (0-1사이의 값: 일반적으로 0.01~0.2)
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)

    for i in corners:
        cv2.circle(dst, tuple(i[0]), 3, (0, 0, 255), 2)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif run == 22:
    # 윤곽선 읽는 코드
    src = cv2.imread(img_path+"convex.png")
    dst = src.copy()

    gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    for i in contours:
        hull = cv2.convexHull(i, clockwise=True)
        cv2.drawContours(dst, [hull], 0, (0, 0, 255), 2)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()