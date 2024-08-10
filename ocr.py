import os
from PIL import Image
import pyocr
import cv2

#環境変数「PATH」にTesseract-OCRのパスを設定。
#Windowsの環境変数に設定している場合は不要。
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path

#pyocrにTesseractを指定する。
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#文字を抽出したい画像のパスを選ぶ
img = cv2.imread('engjpn2.png')

# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二値化処理（適応的閾値処理）
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# 輪郭を検出
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 境界を引く位置を検出
# 各単語の輪郭のx座標の最大値を取得
x_positions = [cv2.boundingRect(c)[0] + cv2.boundingRect(c)[2] for c in contours]
x_positions.sort()

# 境界位置を探す（中央に最も近い最大x座標を境界とする）
middle_x = img.shape[1] // 2
boundary_x = min(x_positions, key=lambda x: abs(x - middle_x))

# 画像を左右に分割
left_img = img[:, :boundary_x]
right_img = img[:, boundary_x:]

# numpy.ndarrayをPillowのImageオブジェクトに変換
left_img = Image.fromarray(cv2.cvtColor(left_img, cv2.COLOR_BGR2RGB))
right_img = Image.fromarray(cv2.cvtColor(right_img, cv2.COLOR_BGR2RGB))

#画像の文字を抽出
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text_eng = tool.image_to_string(left_img, lang="eng", builder=builder)
text_jpn = tool.image_to_string(right_img, lang="jpn", builder=builder)

print(text_eng)
print(text_jpn)