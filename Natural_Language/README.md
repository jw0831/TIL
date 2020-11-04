# ruler(자)salmon(연어)

## 컴퓨터가 인간의 언어(자연어)를 이해할수 있도록 처리하는 분야

작성자: 김진원

토이프로젝트 : **트럼프 바이든 2020 선거예측**을 진행

- 자연어 처리의 순서와 깊은 이해를위해 작성하게 되었습니다. 

## 추천 사이트:

>[(필독) 자연어 처리 기초정리](http://hero4earth.com/blog/learning/2018/01/17/NLP_Basics_01/)
>
>- [(필독)자연어 블로그](https://ratsgo.github.io/blog/categories/)
>- [딥러닝 기반 자연어처리 기법의 최근 연구 동향](https://ratsgo.github.io/natural%20language%20processing/2017/08/16/deepNLP/)
>- [NLP의 기본 절차와 Lexical Analysis](https://ratsgo.github.io/natural%20language%20processing/2017/03/22/lexicon/)
>
>[(필독) NLTK(natural language toolkit)와 WordNet으로 자연어 처리하기 맛보기](https://rfriend.tistory.com/546)
>
>- WordNet은 방대한 영어 어휘와, 유의어 **데이터베이스**다.
>
>[데이터 사이언스 스쿨: NLTK 자연어 처리 패키지](https://datascienceschool.net/03%20machine%20learning/03.01.01%20NLTK%20자연어%20처리%20패키지.html)
>
>- 이거 보고 전처리 및 워드클라우드 생성
>
>[NLTK를 이용한 자연어 처리 블로그](https://happygrammer.github.io/nlp/nltk/)
>
>[인공지능 개발자 모임](http://aidev.co.kr/nlp/7860)
>
>- [NLTK 개발자들이 직접 쓴 자연어 처리 책의 공개 버전: Natural Language Processing with Python](http://www.nltk.org/book/)
>
>[문서에서 핵심 단어를 찾는 TF-IDF 알고리즘](http://aidev.co.kr/2209)
>
>[파이썬 형태소 분석으로 워드클라우드 그리기](https://thinkwarelab.wordpress.com/2016/08/30/파이썬-형태소-분석으로-워드클라우드-그리기/)
>
>[한국어 분석을 위한 pure python code](https://github.com/lovit/soynlp?fbclid=IwAR1eBxqn2MhEG2urLqQqx3j0crSr4TUIiT_SrQozGzsBoWIrOA5jkdJ-xVw)
>
>- 한국어 분석을 위한 pure python code 입니다. 학습데이터를 이용하지 않으면서 데이터에 존재하는 단어를 찾거나, 문장을 단어열로 분해, 혹은 품사 판별을 할 수 있는 비지도학습 접근법을 지향합니다.
>- 처리과정 살펴보기
>
>
>
>[자연어 언어모델 'BERT' 1강](https://www.youtube.com/watch?v=qlxrXX5uBoU&feature=emb_title)
>
>선생님 추천 site:
>
>- [soynlp](https://github.com/lovit/soynlp)
>  - 한국어
>
>감성분석
>
>[(Kaggle) Airline Sentiment Analysis](https://www.kaggle.com/welkin10/airline-sentiment-analysis)
>
>[Sentiment Analysis with Text Mining](https://towardsdatascience.com/sentiment-analysis-with-text-mining-13dd2b33de27)
>
>문서덩어리 (document clusters)
>
>- [위키피디아/wikipedia](https://dumps.wikimedia.org/kowiki/latest/)

# [자연어 관련 용어](http://hero4earth.com/blog/learning/2018/01/17/NLP_Basics_01/)

- Document(문서)
- Corpus(말뭉치): 텍스트(문서)의 집합
- Token(토큰): 단어처럼 의미를 가지는 요소
- Morphemes(형태소): 의미를 가지는 언어에서 최소 단위
- POS(품사): ex) Nouns, Verbs
- Stopword(불용어): I, my, me, 조사, 접미사와 같이 자주 나타나지만 실제 의미에 큰 기여를 하지 못하는 단어들
- Stemming(어간 추출): 어간만 추출하는 것을 의미(running, runs, run -> run)
- Lemmatization(음소표기법): 앞뒤 문맥을 보고 단어를 식별하는 것
- TDM : Term Document Matrix
  - ![TDM](https://qph.fs.quoracdn.net/main-qimg-27639a9e2f88baab88a2c575a1de2005)

# 자연어 처리 단계

## [어휘분석 절차](https://ratsgo.github.io/natural%20language%20processing/2017/03/22/lexicon/)

크게 **문장분리(sentence splitting)**, **토크나이즈(tokenize), Morphological analysis**, **포스태깅** 네 단계로 나뉜다.

- **Sentence splitting**
  - 컴퓨터 입장에서 **말뭉치(corpus)** 는 의미없는 글자들의 나열일 겁니다. 우선 이를 문장 단위로 끊어서 입력해야 합니다. 일반적으로는 마침표(.)나 느낌표(!), 물음표(?) 등 기준으로도 충분히 문장분리를 잘 수행할 수 있습니다. 하지만 토픽모델링 같은 특정 알고리즘이나 방법론의 경우 문장분리를 반드시 수행하지 않아도 됩니다.
- **Tokenize**
  - **토큰(token)** 이란 의미를 가지는 문자열을 뜻합니다. 토큰은 형태소(뜻을 가진 최소 단위)나 그보다 상위 개념인 **단어**(자립하여 쓸 수 있는 최소 단위)까지 포함합니다. **토크나이징(tokenizing)** 이란 문서나 문장을 분석하기 좋도록 토큰으로 나누는 작업입니다. 영어의 경우 공백만으로도 충분히 토큰을 나눌 수 있다고 합니다. 물론 ‘-‘(state-of-the-art vs state of the art)이나 합성어(Barack Obama) 등 처리를 세밀히 해줘야 하는 문제가 남아있긴 하지만요. 띄어쓰기를 거의 하지 않는 중국어의 경우 토큰 분석 작업이 난제로 꼽힙니다.
- **Morphological analysis**
  - Text Normalization
  - 대문자 -> 소문자 : **folding**
  - **stemming, lemmatization**
- **Part of speech Tagging**
  - 토큰의 품사 정보를 할당
  - 의사결정나무(Decision Trees), 은닉 마코프 모델(Hidden Markov Models), 서포트벡터머신(Support Vector Machines) 등이 여기에 해당합니다. [KoNLPy](http://konlpy.org/) 같은 한국어 기반의 포스태거들은 문장분리, 토크나이즈, lemmatization, 포스태깅에 이르기까지 전 과정을 한꺼번에 수행해 줍니다.

# 데이터 전처리

- Tokenizing
  - 자연어를 어떤 단위로 살펴볼 것인가.
  - 어절
  - 형태소 : 의미를 가진 최소 단위
  - n-gram
  - WordPiece : 버트에서 사용하는 tokenizing기법
- Lexical analysis
  - 어휘 분석
  - 형태소 분석
  - 개체명 인식
  - 상호 참조
- Syntactic analysis
  - 구문 분석
- Semantic analysis
  - 의미 분석

# 자연어처리는 분류 문제 (감성분석 포함)

자연어에서 어떻게 특징을 추출하는가? 

- 가장큰 대표예제 -> 원핫인코딩
  - 단점: 백터가 계속 증가한다. 단어의 의미를 좌표평면에 표현할수 없다.
- Word2vec: 
  - 자연어 의미를 벡터 공간에 임베딩 -> 한 단어의 주변 단어들을 통해, 그 단어의 의미를 파악
  - input - hidden layer - output

word embedding의 방법론에 따른 특징

- Sparse representation
  - One-hot encoding
  - n개의 단어에 대한 n차원의 벡터
  - 단어가 커질 수록 무한대 차원의 벡터가 생성
  - 주로 신경망의 입력단에 사용
  - 의미 유추 불가능
  - 차원의 저주
  - One-hot vector의 차원 축소를 통해 특징을 분류하고자 하는 접근도 있음
- Dense representation
  - word embedding : **word2vec**
  - 한정된 차원으로 표현 가능
  - 의미 관계 유추 가능
  - 비지도 학습으로  단어의 의미 학습 가능

**워드 임베딩** : gensim (word2vec), **fasttext** (gensim라이브러리에 포함됨)

- n-gram 벡터의 평균을 통해 단어 벡터를 획득
  - Orange, Oranges(OOV)  out of vocabulary가 들어와도 orange와 굉장히 유사하기 때문에 orange로 인식!
- 29:30초 (유튜브강의)

- [fasttext](https://research.fb.com/fasttext/), fasttext.cc 를 활용하면  
  - 딥러닝에서 가장큰 한계점이 OOV인데 fasttext를 활용하면 oov에 대해서도 어느정도 정보처리가 가능해서 word2vec으로 만들어 놓은 벡터들을 fasttext로 교체해서 활용하기도함
  - **OOV에 강하다!**
  - 워드 임베딩은 fasttext를 추천
- 워드임베딩 활용 예제: word2vec의 벡터 공간을 피처로 활용

- 단점: 
  - 의미가 여러개인 한단어에 대해서 학습하는게 불가능하다. (의미가 무너짐: 주변단어만을 이용해서 학습이 이용되기 때문에)



# TF-IDF 알고리즘

- TF-IDF(Term Frequency-Inverse Document Frequency)는 문서(Document)내에서 단어(Term)의 중요도를 빈도(Frequency)를 사용해서 계산하는 방법입니다.

  - 뉴스 기사에서 가장 핵심이 되는 단어가 무엇인지 찾는 방법을 생각해 보겠습니다. 우선 가장 먼저 떠오르는 것은 전체 문서에서 가장 많이 반복되는 단어를 구하는 것입니다. 예를 들어 인공지능에 대한 기사라면 당연히 인공지능이란 용어가 여러번 사용될 것입니다. 이것이 바로 **TF**입니다. 

  - 이 문서에 많이 반복되지만 다른 문서에도 동일하게 여러번 나오는 단어들은 크게 중요하지 않다고 판단할 수 있습니다. 그래서 각 단어가 문서 전체에 나오는 빈도를 구한 다음 이를 역으로 곱하면 그 단어의 중요도를 감소시킬 수 있습니다. 이것이 **IDF**입니다.

    <img src="http://aidev.co.kr/files/attach/images/1318/209/002/5930b490e292fcc26d6eefa768b803d4.png" alt="tf-idf알고리즘 공식" style="zoom:70%;" />

  - 수식은 위와 같습니다. w는 문서 y에서 단어 x의 중요도입니다. 오른쪽의 IDF 부분을 로그로 계산한 것은 숫자가 너무 커지는 것을 방지하기 위해서 입니다. 로그 함수의 특성상 입력에 비해 출력이 서서히 증가하기 때문입니다.

- [(필독) 개념과 역사](http://www.bloter.net/archives/264262)
- [tf-idf 에 대해 알아봅시다](https://thinkwarelab.wordpress.com/2016/11/14/ir-tf-idf-에-대해-알아봅시다/)
- **TF-IDF** 를 통해 특정 단어가 가지는 중요도를 워드클라우드로 시각화 해보기

# word2vec

> [wevi: word embedding visual inspector 통해 직접 함수api를 설정, 시각화 해보자!](https://ronxin.github.io/wevi/)
>
> [응용사례](https://word2vec.kr)
>
> [word2vec 으로 문장 분류하기](https://ratsgo.github.io/natural%20language%20processing/2017/03/08/word2vec/)
>
> [nlp_github](https://lovit.github.io/category/#/nlp)
>
> - [Word / Document embedding (Word2Vec / Doc2Vec)](https://lovit.github.io/nlp/representation/2018/03/26/word_doc_embedding/)
>
> - [Document vectors 와 word vectors 를 함께 시각화 하기 (Doc2vec 공간의 이해)](https://lovit.github.io/nlp/2019/06/18/joint_visualization_of_worddoc/)
> - [Joint visualization for News and words](https://github.com/lovit/joint_visualization_of_words_and_docs/)
>
> [skip-gram](https://www.sallys.space/blog/2018/04/05/Word2vec,-skip-gram-model/)
>
> - 구글 연구팀은 논문에 두개의 모델을 제시했습니다. CBoW와 Skip-gram으로 CBow는 주변의 단어를 이용해 하나의 단어는 찾아내는 방법이고 Skip-gram은 하나의 단어에서 여러 단어를 예측하는 방법입니다. 결과적으로는 좋은 성능을 보이는 Skip-gram이 대세라고 합니다. 논문의 성능표를 보면 의미 분석에서는 다른 모델보다 월등히 좋은 성능을 보입니다.
>
> [(필독) Word2Vec의 학습 방식 (feat.skip-gram)](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/30/word2vec/)
>
> - [skip-gram모델&튜닝 기법](https://reniew.github.io/22/)
>
> [(필독) Gensim](https://radimrehurek.com/gensim/models/word2vec.html)
>
> [Visualizing Word Vectors with t-SNE](https://www.kaggle.com/jeffd23/visualizing-word-vectors-with-t-sne)
>
> 







## [자연어 처리 기법을 이용한 머신러닝 방법](http://hero4earth.com/blog/learning/2018/01/17/NLP_Basics_01/)

처음 자연어 처리를 접했을 때 흐름이 잘 이해가 되지 않았다. word2vec에서 벡터화 단계에서부터 신경망을 사용하고 단어간의 유사도 분석이 가능했다. 그래서 분류/예측 등을 위한 학습 단계로 넘어가는 것이 혼란스러웠다. 간단히 아래의 단계로 진행된다.

1. Word Embedding: 벡터화
2. 학습
3. 예측

결국, 어떤 방식으로 Word Embedding을 하느냐가 가장 중요한 관건이다. 벡터화된 데이터가 자연어의 어떤 의미를 담고 있는지가 결정되기 때문이다. 이후 학습 단계에서 CNN, RNN 등의 기법을 활용하여 성능을 높이게 된다.





# 모델링

[Word2Vec 과 Logistic Regression 을 이용한 (Semi-supervised) Named Entity Recognition](https://lovit.github.io/nlp/2019/02/16/logistic_w2v_ner/)



[정형데이터 대회는 AutoML에 때려박고(?) 시작하자!](https://dacon.io/codeshare/1701)



# 토픽 모델링

## LDA 알아보기

[딥 러닝을 이용한 자연어 처리 입문](https://wikidocs.net/book/2155)

- [자연어처리(NLP) 8일차 (LDA)](https://medium.com/@omicro03/자연어처리-nlp-8일차-lda-f571b4da9d04)



# ToDo

감성사전 적용해서 감성 점수 적용해보기

- 트럼프/바이든 트윗에 적용해서 감성이 어떤지 알아보기 (그의 정신상태 심리상태를 분석할수 있어보인다.)
- 사람들의 감성 to Trump/Biden

