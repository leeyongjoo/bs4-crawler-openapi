# bs4-crawler-openapi
BeautifulSoup를 이용하여 구현한 파이썬 크롤러
> 사이트에 적힌 메서드들을 수집하여 번역 후에 csv로 저장

파이썬을 공부하며 Notion에 정리하던 중에 메서드를 정리해놓으면 좋겠다고 생각하여  
적당한 자료를 찾아보다가 [programiz](https://www.programiz.com/) 사이트를 찾게 되었음
> programiz 사이트는 프로그래밍 언어(`Python`, `C`, `C++`, `Java`, `Kotlin`, `Swift`, `C#`, `DSA`)에 대한   
튜토리얼과 참고자료가 잘 정리되어있는 영문 사이트

메서드는 잘 정리되어 있으나 설명이 영문이라는 점과 일일이 복사 붙여넣기 하기 번거로움이 존재하여  
이를 해결해 줄 소스코드 구현

## Installation
[pip](https://pip.pypa.io/en/stable/)를 이용하여 라이브러리 설치 *Python Version: 3.8*
```bash
pip install -r requirements.txt
```

## Example

![image](https://user-images.githubusercontent.com/46367323/78461800-01639000-7707-11ea-835c-a30c7705f4d1.png)

- googletrans  
[built-in_utf-8.csv](https://github.com/leeyongjoo/bs4-crawler-openapi/blob/master/sites/programiz_python_methods/google/built-in_utf-8.csv)
![googletrans example](https://user-images.githubusercontent.com/46367323/78461840-599a9200-7707-11ea-8bed-469ec44eb0f7.png)

- papago NMT api  
[built-in_utf-8.csv](https://github.com/leeyongjoo/bs4-crawler-openapi/blob/master/sites/programiz_python_methods/nmt/built-in_utf-8.csv)
![papago example](https://user-images.githubusercontent.com/46367323/78461813-1dffc800-7707-11ea-9efb-21111c172522.png)


## Issue
- 각 API는 일일 할당량이 존재

## References
- [googletrans](https://blog.naver.com/PostView.nhn?blogId=esak97&logNo=221706630976)
- [papago api](https://tariat.tistory.com/383)
- [csv handling](http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221274278923&parentCategoryNo=&categoryNo=35&viewDate=&isShowPopularPosts=false&from=postView)
