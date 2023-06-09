### 建立分類器辨識物件
``face_cascade = cv2.CascadeClassifier(path)`` 
> - path : opencv 內建分類器資源檔(.xml) 

### 使用分類器辨識物件
``faces = face_cascade.detectMultiScale(img, scaleFactor, minNeighbors, [minSize], [maxSize])`` 
> - img : 要辨識的影像檔案
> - scaleFactor : 圖像比例的縮小倍數，適度放大可以讓匹配更嚴格; 反之更寬鬆 (預設值1.1，必須大於1.0)
> - minNeighbors : 每個區塊的特徵值皆會比對，設定多少個特徵數才算匹配成功 (預設值3)
> - minSize : 最小辨識區塊，小於此將被忽略
> - maxSize : 最大辨識區塊，大於此將被忽略

<hr>

## LBPH(Local Binary Pattern Histogram) 人臉辨識
主要使用區域(局部)紋理特徵完成人臉辨識

### 原理
以像素點為中心的強度當作閾值，若相鄰像素點的強度大於等於閾值，相鄰像素點值為1 (否則為0)。將相鄰點二值化後，從任意位置開始序列化，所得之序列值 (二進位轉十進位) 即為目前像素點的中心值。處理完所有像素點後，就可以得到影像特徵圖，其直方圖為LBPH直方圖。


### 建立 LBPH 人臉辨識物件
``model = cv2.face.LBPHFaceRecognizer_create([radius], [neighbors], [grid_x], [grid_y], [threshold])`` 
> - radius : 圓形局部的半徑 (預設值1)
> - neighbors : 圓形局部的相鄰點個數 (預設值8)
> - grid_x : 每單元格在水平方向的個數 (預設值8)
> - grid_y : 每單元格在垂直方向的個數 (預設值8)
> - threshold : 人臉辨識時使用的閾值 (建議使用預設值)

### 訓練 LBPH 人臉辨識
``model.train(src, labels)``
> - src : 人臉影像樣本
> - labels : 影像樣本對應的標籤

### 儲存 LBPH 訓練數據
``model.save(filename)``
> - filename : 使用 .xml 或 .yml 當副檔名

### 執行 LBPH 人臉辨識
``model.predict(src) -> label, confidence`` 
> - src : 需要辨識的人臉影像
> - label : 樣本匹配最高的標籤索引值
> - confidence: 匹配度評分，若是0代表完全相同; 大於0小於50代表可以接受; 大於80代表匹配程度差

<hr>

## Eigenfaces 人臉辨識
主要使用主成份分析(Principle Component Analysis, PCA)

### 原理
將所有人的所有訓練影像當作一個個體，每一個人臉用降維方式處理成一維的向量，拋棄無關緊要的部分，提取相關和有用的成份，即為主成份。重複執行以下過程: **從新的影像提取主成份 -> 將這些主成份與訓練數據集的元素列作比較 -> 找出最匹配 -> 回傳最匹配的關聯標籤**

### 建立 Eigenfaces 人臉辨識物件
``model = cv2.face.EigenFaceRecognizer_create([num_components], [threshold])``
> - num_components : PCA方法中要保留的份量個數 (建議使用預設值)
> - THRESHOLD : 人臉辨識時的閾值 (建議使用預設值)

### 訓練 Eigenfaces 人臉辨識
``model.train(src, labels)``
> - src : 人臉影像樣本
> - labels : 影像樣本對應的標籤

### 執行 Eigenfaces 人臉辨識
``model.predict(src) -> label, confidence`` 
> - src : 需要辨識的人臉影像
> - label : 樣本匹配最高的標籤索引值
> - confidence: 匹配度評分，範圍值在0~20000，若是0代表完全相同; 大於0小於5000代表可以接受

<hr>

## Fisherfaces 人臉辨識
Eigenfaces 演算法的改良版本

### 原理
主成份分析 (PCA) 會一次查看所有人的所有訓練影像，從這些人中提取主成份，這個方法關注的不是一個人的特徵，是代表訓練數據所有人的特徵。因此 Eigenfaces 方法的缺點是具有急遽變化的影像 (例:光線變化)，有可能會主導其餘的影像。<br>
Fisherfaces 演算法提取區分一個人與其他人的有用特徵，會防止一個人的特徵成為主導。

### 建立 Fisherfaces 人臉辨識物件
``model = cv2.face.EigenFaceRecognizer_create([num_components], [threshold])``
> - num_components : PCA方法中要保留的份量個數 (建議使用預設值)
> - THRESHOLD : 人臉辨識時的閾值 (建議使用預設值)

### 訓練 Fisherfaces 人臉辨識
``model.train(src, labels)``
> - src : 人臉影像樣本
> - labels : 影像樣本對應的標籤

### 執行 Fisherfaces 人臉辨識
``model.predict(src) -> label, confidence`` 
> - src : 需要辨識的人臉影像
> - label : 樣本匹配最高的標籤索引值
> - confidence: 匹配度評分，範圍值在0~20000，若是0代表完全相同; 大於0小於5000代表可以接受