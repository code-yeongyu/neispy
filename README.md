# neispy : 나이스 급식 조회 파이썬 코드

neispy는 neis+python의 합성어로써, 나이스의 급식을 파이썬 코드를 통해 파싱해오는 코드를 담고 있습니다.
또한 본 프로젝트에서는 텔레그램 봇과의 연동도 지원합니다.

# 파일 설명

[neispy.py](https://github.com/kim-yeon-gyu-exlock/neispy/blob/master/neispy.py)는 급식을 파싱해오는 핵심 코드를 담고있습니다.

get_meals(day, school)함수를 통해서, 온전히 급식내용만을 담은 string을 반환 받을 수 있습니다.

day의 값은 integer, 정수로써 0, 1, 2, 3, 4 중 하나의 값을 포함해야 합니다. 이는 순서대로 월, 화, 수, 목, 금 을 의미합니다.
schoolcode는 Neis에서 처리시에 사용되는 학교 코드로서, [meatwatch](https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do)와 같은 곳에서 학교코드를 얻으실 수 있습니다.

[main.py](https://github.com/kim-yeon-gyu-exlock/neispy/blob/master/main.py)는 위의 nesipy.py의 텍스트 wrapper입니다.
요일과 학교코드를 입력받아, get_meals()함수를 실행하고 반환결과를 출력 합니다.

[telegram main.py](https://github.com/kim-yeon-gyu-exlock/neispy/blob/master/telegram%20main.py)는 neispy.py의 텔레그램 봇 wrapper입니다.

텔레그램 봇의 api활용은 [공식 텔레그램 봇 문서](https://core.telegram.org/bots/api)를 확인 하시길 바라며, api_key 설정은 [api_key.py](https://github.com/kim-yeon-gyu-exlock/neispy/blob/master/api_key.py) 파일에서 하실 수 있습니다.
