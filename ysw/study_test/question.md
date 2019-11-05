def check_date(text):
    for char in text:
        assert char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]

    assert len(char)  ==8




- *arg는 튜플형태로 input값들 주고 *kwargs는 key, value로 연결해줌

- 작동을 어떻게 시키는 거지?
   또한 text를 받으면 분명 for 구조를 못쓰지않나?
  함수가 겹쳐있는데 check_date(text)를 실행하면 맨위에것만 하고싶은데 왜 아래것으로 잡히나
  오버라이딩인가?

- assert char in [str(e) for e in range(start, end+1)]구문     해석은 내 해석이 맞는가?

- assert는 구지 리스트로 안줘도 검사가능? 
__checkdate.py 임__

-  tokens 에 개념?
-  staticmethod로 작성하면 구지 인스턴스 만들지 않아도 사용가능.

- (a) 패턴이 나타내는 문자열의 집합은 패턴 그 자체이다. 예를 들어서, 패턴이 ’1’이라면 나타내는 문자 열도 ’1’ 하나이다.
즉 어떻게 검사를 한다는 이야기?

