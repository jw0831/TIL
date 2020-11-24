# BERT(Bidirectional Encoder Representation from Transformers)

3가지의 입력 임베딩 (Tokken, Segment, Position 임베딩)의 합으로 구성

단순히 포지션만 갖고 있는 임베딩 형태가 아니라 segment 로 구분 + 토큰을 준다.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FWFCfe%2FbtqBWZ40Gmc%2F6FkuwsAGN9e7Uudmi03k4k%2Fimg.png)

## Token Embeddings

- Word Piece 임베딩 방식 사용
- 자주 등장하면서 가장 긴 길이의 sub-word를 하나의 단위로 생성
  - 자주 등장하는 sub-word는 그 자체 단위가 되고, 자주 등장하지 않는 단어는 sub-word로 쪼개짐
- 기존 워드 임베딩은 OOV문제가 존제 하지만, Word Picec임베딩은 모든 언어에 적용 가능, sub-word 단위로 단어를 분절 하므로 OOV 처리에 효과적이고 정확도 상승효과도 있음

## Sentence Embeddings

- BERT는 두 개의 문장을 문장 구분자 ([SEP])와 함께 결합
- 입력 길이의 제한으로 두 문장은 합쳐서 512 subword 이하로 제한
- 입력의 길이가 길어질수록 학습 시간은 제곱으로 증가하기 때문에 적절한 입력 길이 설정 필요
- 한국어는 보통 평균 20 subword로 구성되고 99%가 60 subword를 넘지 않기 때문에 입력 길이를 두 문장이 합쳐 128로 해도 충분
- 간혹 긴 문장이 있으므로 우선 입력 길이 128로 제한하고 학습한 후, 128보다 긴 입력들을 모아 마지막에 따로 추가 학습하는 방식을 사용

## Position Embedding

- BERT는 저자의 이전 논문인 Transformer 모델을 착용
- Transformer 는 주로 사용하는 CNN, RNN 모델을 사용하지 않고 Self-Attention(입력의 위치를 알지 못함) 모델을 사용
- Self-Attention은 입력의 위치에 대해 고려하지 못하므로 입력 토큰의 위치 정보가 필요
- Transformer 에서는 Sinusoid 함수를 이용한 Positional encoding을 사용하였고, BERT에서는 이를 변형하여 Position encoding을 사용
- Position encoding은 단순하게 Token 순서대로 0,1,2,,...와 같이 순서대로 인코딩

## 임베딩 취합

- BERT 는 위에서 소개한 3가지의 입력 임베딩 (Token, Segment, Position 임베딩)을 **취합**하여 <u>하나의 임베딩</u> 값으로 생성
- 임베딩의 합에 **Layer Normalization** 과 **Dropout**을 적용하여 입력으로 사용

## 언어 모델링 구조(Pre-training BERT)

미리 한번 학습된 BERT를 가지고 다양한 데이터를 Fine-Tuning 을 통해 활용해서, 우리가 원하는 어플리케이션을 모델을 생성할 수있음.

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcEoPYe%2FbtqBW0v9pJo%2FxM7PQl9BL0XAKX9fYuphw1%2Fimg.png)

## 언어 모델링 데이터

- BERT는 총 3.3억 단어(8억 단어의 BookCorpus 데이터와 25억 단어의 Wikipedia 데이터)의 거대한 말뭉치를 이용하여 학습
- 거대한 말뭉치를 MLM, NSP 모델 적용을 위해 스스로 라벨을 만들고 수행하므로 준지도학습(Semi-supervised)이라고 함
- Wikipedia와 BookCorpus를 정제하기 위해 list, table, header를 제거
- 문장의 순서를 고려해야 하므로 문단 단위로 분리하였고 많은 데이터 정제 작업을 수행

### 모델구조

- BERT 모델은 Transformer 를 기반으로 함
- Transformer 모델 구조는 인코더-디코더 모델이며 번역 도메인에서 최고 성능을 기록
- 기존 인코더-디코더 모델들과 다르게 Transformer는 CNN, RNN을 이용하지 않고 Self-attention이라는 개념을 도입
- BERT는 Transformer의 인코더-디코더 중 인코더만 사용하는 모델
- <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbL28Ok%2FbtqznO6UmYw%2Fe0mFyA814Pvj4kltVxKls0%2Fimg.png" style="zoom:50%;" />

## MLM(Masked Language Model)

- 입력 문장에서 임의로 Token을 마스킹(masking), 그 Token을 맞추는 방식인 MLM 학습 진행
- 문장의 빈칸 채우기 문제를 학습
- 생성 모델 계열은 (예를들어 GPT) 입력의 다음 단어를 예측
- MLM은 문장 내 랜덤한 단어를 마스킹 하고 이를 예측
- 입력의 15% 단어를 [MASK]Token으로 바꿔주어 마스킹 (학습률 향상)
- 이때 **80%**는 <u>[MASK]로 바꿔</u>주지만, 나머지 **10%**는 다른 <u>랜덤 단어</u>로, 또 남은 **10%**는 바꾸지 않고 <u>그대로 둠</u>
- 이는 미세 조정 시 올바른 예측을 돕도록 마스킹에 노이즈를 섞음
- <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLMyXN%2Fbtqzl4Ql7sH%2FykzRZNWkc6rcb8ffU5Nrm1%2Fimg.png" style="zoom:80%;" />
- 입력 단어의 15%가 [MASK]로 대체된 입력이 들어가고, MLM은 [MASK]가 어떤 단어인지를 예측
- BERT의 Token 임베딩은 Word Piece 임베딩 방식을 사용하고, Word piece의 단어수는 30522 단어
- 3만 단어 중 [MASK]에 들어갈 단어를 찾는 것이므로 MLM의 출력인 Softmax의 클래스는 3만개
- 다음 그림은 MLM의 학습 과정이다
- ![MLM학습과정](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdTnfQQ%2FbtqBVLfnFBV%2FrK5PCPsz2xX9t7qLEKUiF1%2Fimg.png)

## NSP(Next Sentence Prediction)

- NSP는 두 문장이 주어졌을 때 두 번째 문장이 첫 번째 문장의 바로 다음에 오는 문장인지 여부를 예측하는 방식
- 두 문장 간 관련이 고려되어야 하는 NLI와 QA의 파인튜닝을 위해 두 문장이 연관이 있는지를 맞추도록 학습
- 첫번째 문장과 두 번째 문장은 [SEP]로 구분
- 두 문장이 실제로 연속하는지는 50% 비율로 참인 문장과, 50%의 랜덤하게 추출된 상관 없는 문장으로 구성
- 이 학습을 통해 문맥과 순서를 언어 모델이 학습 가능, 다음에 올 만한 문장인지 아닌지를 학습
- <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmRPzz%2Fbtqzps28Eyd%2F2ak5AHBLlk1jXHnOgGwyMK%2Fimg.png" style="zoom:80%;" />

- 아래 그림은 NSP의 학습 방법. 연속 문장인지, 아닌지(is next | not next)만 판단하면 되므로 Softmax의 출력은 2개이고 3만개의 출력을 같는 MLM에 비해 빠르게 학습된다는 장점이 있다.
- ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbeTrc5%2FbtqBTL8u19d%2FT1020drYaYApQP6TuKPjaK%2Fimg.png)

## 학습된 언어모델 전이학습(Transfer Learning)

- 이렇게 데이터가 큰 모델은 전이학습이 필요하다.
- 실질적으로 성능이 관찰되는 것은 전이학습 이지만, 언어 모델이 제대로 학습되야 전이학습 시 좋은 성능이 나옴
- 기존 알고리즘들은 자연어의 다양한 Task에 각각의 알고리즘을 독립적으로 만들어야 했지만, BERT 개발 이후 많은 자연어처리 연구자들은 언어 모델을 만드는데 더 공을 들이게 됨
- 전이학습 Task의 성능도 훨씬 더 좋아짐
- 전이학습은 라벨이 주어지므로 지도학습(Supervised learning)
- 전이학습은 BERT의 언어 모델의 출력에 추가적인 모델을 쌓아서 사용
- 일반적으로 복잡한 CNN, LSTM, Attention을 **쌓지 않고 간단한 DNN만 쌓아도 성능이 잘 나오며** 별 차이가 없다고 알려짐
- <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdHqgat%2Fbtqzl4CSqNd%2F7q3g5hxTcAENvvcu1wK6KK%2Fimg.png" style="zoom:67%;" />
- BERT를 각 Task에 쓰기위한 예시는 위 그림과 같다. (a)는 문장 쌍 분류 문제로 **두 문장을 하나의 입력**으로 넣고 두 문장간 관계를 구한다. (b)는 **한 문장을 입력**으로 넣고 문장의 종류를 분류하는 문제이다. (c)는 문장이나 문단 내에서 **원하는 정답 위치의 시작과 끝을 구한다**. (d)는 입력 문장 Token들의 **개체명**(Named entity recognigion)을 구하거나 품사(Part-of-speech tagging) 를 구하는 문제이다. 다른 Task들과 다르게 입력의 모든 Token들에 대해 결과를 구한다.

## BERT의 친구들

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbMaiOM%2FbtqznO6UO3m%2FwvMAVAZDLngmplVbkn0gqK%2Fimg.jpg)

- Transformer 와 Bidirectional LM의 개념을 통해서 BERT가 탄생
- BERT로 부터 파생된 모델이 많음

## 한국어 BERT 모델:

https://beomi.github.io/categories/NLP/LanguageModel/BERT/

[Korean BERT pre-trained cased (KoBERT)](https://github.com/SKTBrain/KoBERT)

[한국어 BERT 언어모델 및 음성 학습데이터](http://aiopen.etri.re.kr/service_dataset.php)



# 참고한 사이트

https://ebbnflow.tistory.com/151

https://keep-steady.tistory.com/19

https://github.com/NLP-kr/tensorflow-ml-nlp-tf2