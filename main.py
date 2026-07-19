import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 1. Firebase 인증 키 로드 및 초기화
# (다운로드받은 키 파일 경로를 정확히 입력하세요)
cred = credentials.Certificate("path/key/firebase-key.json")
firebase_admin.initialize_app(cred)

# 2. Firestore 클라이언트 생성 (기존 오류 나던 부분 수정)
db = firestore.client()

# 3. 엑셀 파일 읽기
df = pd.read_excel('schoolInfo_data.xlsx')

# 4. 판다스 데이터프레임을 파이썬 딕셔너리 리스트로 변환
data_list = df.to_dict(orient='records')

# 5. Firestore의 'schoolInfo_data' 컬렉션에 데이터 추가
# 데이터가 여러 줄(행)일 테니 반복문으로 하나씩 넣어줍니다.
for data in data_list:
    db.collection("schoolInfo_data").add(data)

print("Firestore에 데이터 업로드 완료!")

"""
with open('schoolInfo_data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)  

"""