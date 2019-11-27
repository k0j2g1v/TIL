from flask import Flask , render_template, request
import random, requests
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello Flask'
  return render_template('index.html')

@app.route('/dohyen')
def dohyen():
  return '저는 무술가입니다.'

@app.route('/html')
def html():
  return '<h1>태그를 사용할수 있어요!'

@app.route('/html_multiline')
def html_multiline():
    return """
    <ol>
        <li>하이하이</li>
        <li>안녕안녕</li>
    </ol>
    """

# 동적 라우팅 (Variable Routing)
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'안녕, {name}?'
    return render_template('greeting.html', html_name=name)

# 세제곱을 돌려주는 cube 페이지 작성
# 사용자한테 숫자를 받아서, 세제곱한 결과를 보여주는 페이지

@app.route('/cube/<int:number>')
def cube(number):
  result = number ** 3 
  # return str(number**3)
  return render_template('cube.html', result=result,number=number)

@app.route('/movies')
def movies():
    movie_list = ['82년생김지영', '조커', '앤드게임', '궁예']
    return render_template('movies.html', movies=movie_list)


@app.route('/ping')
def ping():
  return render_template('ping.html')

@app.route('/pong')
def pong():
  user_name = request.args.get('user_name')
  return render_template('pong.html', user_name=user_name)

# fake server
@app.route('/naver')
def naver():
  return render_template('naver.html')

@app.route('/google')
def google():
  return render_template('google.html')

@app.route('/vonvon')
def vonvon():
  return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
# 사용자가 입력한 데이터를 가져온다
  user_name = request.args.get('user_name')
# 사용자에게 보여줄 여러가지 특성들 리스트를 만든다
  first_list = ['행복해','슬퍼','화나','미쳐']
  second_list = ['손으','발','숟가락으','머리카락으']
  third_list = ['밥을먹는다','전화한다','소리지른다','운다','정리한다']
# 리스트에서 랜덤으로 하나씩 선택한다
  first = random.choice(first_list)
  second = random.choice(second_list)
  third = random.choice(third_list)
# 가공한 정보를 템플릿에 담아서 사용자에게 ㅗ여준다
  return render_template('godmademe.html', user_name=user_name,first=first,second=second,third=third)

@app.route('/ASCII')
def ASCII():
  return render_template('ASCIIFont.html')

@app.route('/ASCIIFontMonitor')
def ASCIIMake():
  
  # 사용자가 입력한 form 데이터를 가져온다
  word = request.args.get('word')  
  # ARTII API로 요청을 보내서, 응당 결과를 변수에 담는다. (폰트 정보들)
  fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
  # 가져온 폰트들을 리스트 형태로 바꾼다
  fonts = fonts.split('\n')
  # 폰트 하나를 랜덤으로 선택한다.
  font = random.choice(fonts)
  # 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 담아서 API를 요천한다
  result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
  # 최종 결과물을 사용자에게 돌려준다.
  return render_template('ASCIIFontMonitor.html', result = result)


# end of file
# debug모드를 활성화 시켜서 새로고침을 생략

if __name__ == '__main__':
  app.run(debug=True)