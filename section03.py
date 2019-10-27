# Section03
# 파이썬 가상환경 개념, 설정 및 pip 사용법, vscode 연동

# 가상환경 만들기
# 1. cmd에서 원하는 경로로 이동후 pyhton -m venve 폴더명 입력
# 2. 해당 폴더에 scripts\activate.bat 실행
# 3. pip 사용법 
#    pip search 패키지명
#    pip install 패키지명 
#    pip uninstall 패키지명
#    pip list 설치된 패키지 목록 조회

# 외부 설치 패키지 테스트
import json # python 2.6 이상 버전에서는 simplejson 이 json 으로 리네임 됨.

test_dict = {'1':95, '4':77,'3':65,'5':100,'2':88}

# simplejson 실행

print(json.dumps(test_dict,sort_keys=True,indent=4 * ' ' ))