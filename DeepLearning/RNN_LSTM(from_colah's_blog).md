# [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

Posted on August 27, 2015

- 가독성+정확한 이해를위한 (국어+영어) 통합본


## Recurrent Neural Networks

Humans don’t start their thinking from scratch every second. As you read this essay, you understand each word based on your understanding of previous words. You don’t throw everything away and start thinking from scratch again. Your thoughts have persistence.

Traditional neural networks can’t do this, and it seems like a major shortcoming. For example, imagine you want to classify what kind of event is happening at every point in a movie. It’s unclear how a traditional neural network could use its reasoning about previous events in the film to inform later ones.

Recurrent neural networks address this issue. They are networks with loops in them, allowing information to persist.

인간은 매초 처음부터 생각을 시작하지 않습니다. 이 에세이를 읽으면서 이전 단어에 대한 이해를 바탕으로 각 단어를 이해하게됩니다. 모든 것을 버리지 않고 처음부터 다시 생각하기 시작합니다. 당신의 생각에는 끈기가 있습니다.

기존의 신경망은이를 수행 할 수 없으며 큰 단점으로 보입니다. 예를 들어 영화의 모든 지점에서 어떤 종류의 이벤트가 발생하는지 분류하려고한다고 가정 해보십시오. 전통적인 신경망이 영화의 이전 사건에 대한 추론을 사용하여 이후 사건을 알리는 방법은 불분명합니다.

반복 신경망은이 문제를 해결합니다. 루프가있는 네트워크이므로 정보가 지속될 수 있습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-rolled.png)

**Recurrent Neural Networks have loops.**

In the above diagram, a chunk of neural network, A, looks at some input xt and outputs a value ht. A loop allows information to be passed from one step of the network to the next.

These loops make recurrent neural networks seem kind of mysterious. However, if you think a bit more, it turns out that they aren’t all that different than a normal neural network. A recurrent neural network can be thought of as multiple copies of the same network, each passing a message to a successor. Consider what happens if we unroll the loop:

위의 다이어그램에서 신경망 A 청크는 입력 xt를보고 ht 값을 출력합니다. 루프를 사용하면 네트워크의 한 단계에서 다음 단계로 정보를 전달할 수 있습니다.

이러한 루프는 반복되는 신경망을 신비하게 만듭니다. 그러나 조금 더 생각해 보면 일반적인 신경망과 크게 다르지 않다는 것이 밝혀졌습니다. 반복 신경망은 동일한 네트워크의 여러 복사본으로 생각할 수 있으며, 각 복사본은 메시지를 후속 작업에 전달합니다. 루프를 풀면 어떤 일이 발생하는지 고려하십시오:

![An unrolled recurrent neural network.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-unrolled.png)

**An unrolled recurrent neural network.**

This chain-like nature reveals that recurrent neural networks are intimately related to sequences and lists. They’re the natural architecture of neural network to use for such data.

And they certainly are used! In the last few years, there have been incredible success applying RNNs to a variety of problems: speech recognition, language modeling, translation, image captioning… The list goes on. I’ll leave discussion of the amazing feats one can achieve with RNNs to Andrej Karpathy’s excellent blog post, [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). But they really are pretty amazing.

Essential to these successes is the use of “LSTMs,” a very special kind of recurrent neural network which works, for many tasks, much much better than the standard version. Almost all exciting results based on recurrent neural networks are achieved with them. It’s these LSTMs that this essay will explore.

이 체인과 유사한 특성은 반복되는 신경망이 시퀀스 및 목록과 밀접하게 관련되어 있음을 보여줍니다. 이러한 데이터에 사용할 수있는 신경망의 자연스러운 아키텍처입니다.

그리고 그들은 확실히 사용됩니다! 지난 몇 년 동안 음성 인식, 언어 모델링, 번역, 이미지 캡션 등 다양한 문제에 RNN을 적용하여 놀라운 성공을 거두었습니다. 목록은 계속됩니다. RNN으로 달성 할 수있는 놀라운 업적에 대한 논의는 Andrej Karpathy의 훌륭한 블로그 게시물 인 The Unreasonable Effectiveness of Recurrent Neural Networks에 남겨 두겠습니다. 하지만 정말 놀랍습니다.

이러한 성공에 필수적인 것은 많은 작업에 대해 표준 버전보다 훨씬 더 잘 작동하는 매우 특별한 종류의 반복 신경망 인 "LSTM"을 사용하는 것입니다. 반복적 인 신경망을 기반으로 한 거의 모든 흥미로운 결과를 얻을 수 있습니다. 이 에세이에서 살펴볼 것은 바로이 LSTM입니다.

## The Problem of Long-Term Dependencies

One of the appeals of RNNs is the idea that they might be able to connect previous information to the present task, such as using previous video frames might inform the understanding of the present frame. If RNNs could do this, they’d be extremely useful. But can they? It depends.

Sometimes, we only need to look at recent information to perform the present task. For example, consider a language model trying to predict the next word based on the previous ones. If we are trying to predict the last word in “the clouds are in the _sky_,” we don’t need any further context – it’s pretty obvious the next word is going to be sky. In such cases, where the gap between the relevant information and the place that it’s needed is small, RNNs can learn to use the past information.

RNN의 매력 중 하나는 이전 비디오 프레임을 사용하여 현재 프레임에 대한 이해를 알릴 수있는 것과 같이 이전 정보를 현재 작업에 연결할 수 있다는 아이디어입니다. RNN이이 작업을 수행 할 수 있다면 매우 유용 할 것입니다. 그러나 그들은 할 수 있습니까? 때에 따라 다르지.

때로는 현재 작업을 수행하기 위해 최근 정보 만 보면됩니다. 예를 들어, 이전 단어를 기반으로 다음 단어를 예측하려는 언어 모델을 고려하십시오. "구름이 하늘에 있습니다"의 마지막 단어를 예측하려는 경우 추가 컨텍스트가 필요하지 않습니다. 다음 단어가 하늘이 될 것이 분명합니다. 관련 정보와 필요한 장소 사이의 간격이 작은 이러한 경우 RNN은 과거 정보를 사용하는 방법을 배울 수 있습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-shorttermdepdencies.png)

But there are also cases where we need more context. Consider trying to predict the last word in the text “I grew up in France… I speak fluent _French_.” Recent information suggests that the next word is probably the name of a language, but if we want to narrow down which language, we need the context of France, from further back. It’s entirely possible for the gap between the relevant information and the point where it is needed to become very large.

Unfortunately, as that gap grows, RNNs become unable to learn to connect the information.

하지만 더 많은 맥락이 필요한 경우도 있습니다. "나는 프랑스에서 자랐습니다… 나는 프랑스어를 유창하게 구사합니다."라는 텍스트의 마지막 단어를 예측해보십시오. 최근 정보에 따르면 다음 단어는 아마도 언어의 이름 일 것입니다. 그러나 우리가 어떤 언어를 좁히고 싶다면 더 뒤로 프랑스의 맥락이 필요합니다. 관련 정보와 정보가 매우 커져야하는 지점 사이의 격차는 전적으로 가능합니다.

불행히도 그 격차가 커짐에 따라 RNN은 정보를 연결하는 방법을 배울 수 없게됩니다.

![Neural networks struggle with long term dependencies.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/RNN-longtermdependencies.png)

In theory, RNNs are absolutely capable of handling such “long-term dependencies.” A human could carefully pick parameters for them to solve toy problems of this form. Sadly, in practice, RNNs don’t seem to be able to learn them. The problem was explored in depth by [Hochreiter (1991) [German]](http://people.idsia.ch/~juergen/SeppHochreiter1991ThesisAdvisorSchmidhuber.pdf) and [Bengio, et al. (1994)](http://www-dsi.ing.unifi.it/~paolo/ps/tnn-94-gradient.pdf), who found some pretty fundamental reasons why it might be difficult.

Thankfully, LSTMs don’t have this problem!

이론적으로 RNN은 이러한 "장기 종속성"을 절대적으로 처리 할 수 있습니다. 인간은 이러한 형태의 장난감 문제를 해결하기 위해 매개 변수를 신중하게 선택할 수 있습니다. 안타깝게도 실제로 RNN은이를 배울 수없는 것 같습니다. 이 문제는 Hochreiter (1991) [독일어]와 Bengio, et al. (1994), 그는 그것이 어려울 수있는 꽤 근본적인 이유를 발견했습니다.

고맙게도 LSTM에는이 문제가 없습니다!

## LSTM Networks

Long Short Term Memory networks – usually just called “LSTMs” – are a special kind of RNN, capable of learning long-term dependencies. They were introduced by [Hochreiter & Schmidhuber (1997)](http://www.bioinf.jku.at/publications/older/2604.pdf), and were refined and popularized by many people in following work.[1](https://colah.github.io/posts/2015-08-Understanding-LSTMs/#fn1) They work tremendously well on a large variety of problems, and are now widely used.

일반적으로 "LSTM"이라고하는 장단기 기억 네트워크는 장기 종속성을 학습 할 수있는 특별한 종류의 RNN입니다. Hochreiter & Schmidhuber (1997)에 의해 소개되었으며 다음 작업에서 많은 사람들에게 세련되고 대중화되었습니다.

LSTMs are explicitly designed to avoid the long-term dependency problem. Remembering information for long periods of time is practically their default behavior, not something they struggle to learn!

LSTM은 장기적인 종속성 문제를 피하기 위해 명시 적으로 설계되었습니다. 오랜 기간 동안 정보를 기억하는 것은 배우기 힘든 것이 아니라 사실상 기본 행동입니다!

All recurrent neural networks have the form of a chain of repeating modules of neural network. In standard RNNs, this repeating module will have a very simple structure, such as a single tanh layer.

모든 반복 신경망은 신경망의 반복 모듈 체인 형태를 갖습니다. 표준 RNN에서이 반복 모듈은 단일 tanh 레이어와 같은 매우 간단한 구조를 갖습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-SimpleRNN.png)

**The repeating module in a standard RNN contains a single layer.**

LSTMs also have this chain like structure, but the repeating module has a different structure. Instead of having a single neural network layer, there are four, interacting in a very special way.

LSTM도 이러한 체인 구조를 가지고 있지만 반복 모듈은 다른 구조를 가지고 있습니다. 하나의 신경망 계층을 갖는 대신 매우 특별한 방식으로 상호 작용하는 4 개의 계층이 있습니다.

![A LSTM neural network.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png)

**The repeating module in an LSTM contains four interacting layers.**

Don’t worry about the details of what’s going on. We’ll walk through the LSTM diagram step by step later. For now, let’s just try to get comfortable with the notation we’ll be using.

자세한 내용은 걱정하지 마세요. 나중에 LSTM 다이어그램을 단계별로 살펴 보겠습니다. 지금은 우리가 사용할 표기법에 익숙해 지도록하겠습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM2-notation.png)

In the above diagram, each line carries an entire vector, from the output of one node to the inputs of others. The pink circles represent pointwise operations, like vector addition, while the yellow boxes are learned neural network layers. Lines merging denote concatenation, while a line forking denote its content being copied and the copies going to different locations. 

위의 다이어그램에서 각 라인은 한 노드의 출력에서 다른 노드의 입력까지 전체 벡터를 전달합니다. 분홍색 원은 벡터 추가와 같은 점 단위 연산을 나타내고 노란색 상자는 학습 된 신경망 계층입니다. 병합하는 줄은 연결을 나타내는 반면 줄 분기는 복사되는 내용과 다른 위치로 이동하는 복사본을 나타냅니다.

## The Core Idea Behind LSTMs

The key to LSTMs is the cell state, the horizontal line running through the top of the diagram.

The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It’s very easy for information to just flow along it unchanged.

LSTM의 핵심은 다이어그램 상단을 가로 지르는 수평선 인 셀 상태입니다.

세포 상태는 일종의 컨베이어 벨트와 같습니다. 그것은 단지 약간의 선형 상호 작용으로 전체 체인을 따라 똑바로 실행됩니다. 정보가 그대로 그대로 전달되는 것은 매우 쉽습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-C-line.png)

The LSTM does have the ability to remove or add information to the cell state, carefully regulated by structures called gates.

Gates are a way to optionally let information through. They are composed out of a sigmoid neural net layer and a pointwise multiplication operation.

LSTM은 게이트라고하는 구조에 의해 신중하게 조절되는 셀 상태에 정보를 제거하거나 추가 할 수있는 기능이 있습니다.

게이트는 선택적으로 정보를 전달하는 방법입니다. 시그 모이 드 신경망 계층과 점적 곱셈 연산으로 구성됩니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-gate.png)

The sigmoid layer outputs numbers between zero and one, describing how much of each component should be let through. A value of zero means “let nothing through,” while a value of one means “let everything through!”

An LSTM has three of these gates, to protect and control the cell state.

시그 모이 드 레이어는 0과 1 사이의 숫자를 출력하여 각 구성 요소를 얼마나 통과해야하는지 설명합니다. 값이 0이면 "아무것도 통과하지 못함"을 의미하고 값 1은 "모든 것을 통과 시키십시오!"를 의미합니다.

LSTM에는 셀 상태를 보호하고 제어하기 위해 세 개의 게이트가 있습니다.

## Step-by-Step LSTM Walk Through

The first step in our LSTM is to decide what information we’re going to throw away from the cell state. This decision is made by a sigmoid layer called the “forget gate layer.” It looks at ht−1and xt, and outputs a number between 0 and 1 for each number in the cell state Ct−1. A 1represents “completely keep this” while a 0 represents “completely get rid of this.”

Let’s go back to our example of a language model trying to predict the next word based on all the previous ones. In such a problem, the cell state might include the gender of the present subject, so that the correct pronouns can be used. When we see a new subject, we want to forget the gender of the old subject.

LSTM의 첫 번째 단계는 셀 상태에서 버릴 정보를 결정하는 것입니다. 이 결정은 "포겟 게이트 레이어"라고하는 시그 모이 드 레이어에 의해 이루어집니다. ht-1과 xt를보고 셀 상태 Ct-1의 각 숫자에 대해 0에서 1 사이의 숫자를 출력합니다. 1은 "완전히 유지"를 나타내고 0은 "완전히 제거"를 나타냅니다.

이전의 모든 단어를 기반으로 다음 단어를 예측하려는 언어 모델의 예로 돌아가 보겠습니다. 이러한 문제에서 셀 상태는 현재 주제의 성별을 포함 할 수 있으므로 올바른 대명사를 사용할 수 있습니다. 새로운 주제를 볼 때 우리는 이전 주제의 성별을 잊고 싶습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-focus-f.png)

The next step is to decide what new information we’re going to store in the cell state. This has two parts. First, a sigmoid layer called the “input gate layer” decides which values we’ll update. Next, a tanh layer creates a vector of new candidate values, C̃ t, that could be added to the state. In the next step, we’ll combine these two to create an update to the state.

In the example of our language model, we’d want to add the gender of the new subject to the cell state, to replace the old one we’re forgetting.

다음 단계는 셀 상태에 저장할 새로운 정보를 결정하는 것입니다. 이것은 두 부분으로 구성됩니다. 먼저 "입력 게이트 레이어"라고하는 시그 모이 드 레이어가 업데이트 할 값을 결정합니다. 다음으로 tanh 레이어는 상태에 추가 할 수있는 새로운 후보 값  C̃ t의 벡터를 생성합니다. 다음 단계에서는이 두 가지를 결합하여 상태에 대한 업데이트를 만듭니다.

언어 모델의 예에서는 새 주제의 성별을 셀 상태에 추가하여 잊어 버린 이전 주제를 대체하려고합니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-focus-i.png)

It’s now time to update the old cell state, Ct−1, into the new cell state Ct. The previous steps already decided what to do, we just need to actually do it.

We multiply the old state by ft, forgetting the things we decided to forget earlier. Then we add it∗C̃ t. This is the new candidate values, scaled by how much we decided to update each state value.

In the case of the language model, this is where we’d actually drop the information about the old subject’s gender and add the new information, as we decided in the previous steps.

이제 이전 셀 상태 Ct-1을 새 셀 상태 Ct로 업데이트 할 때입니다. 이전 단계는 이미 무엇을 해야할지 결정 했으므로 실제로 수행하면됩니다.

우리는 이전에 잊기로 결정한 것을 잊고 이전 상태에 ft를 곱합니다. 그런 다음 그것을 추가합니다 ∗C̃ t. 이것은 우리가 각 상태 값을 업데이트하기로 결정한 정도에 따라 조정 된 새로운 후보 값입니다.

언어 모델의 경우 이전 단계에서 결정한대로 실제로 이전 주제의 성별에 대한 정보를 삭제하고 새 정보를 추가하는 곳입니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-focus-C.png)

Finally, we need to decide what we’re going to output. This output will be based on our cell state, but will be a filtered version. First, we run a sigmoid layer which decides what parts of the cell state we’re going to output. Then, we put the cell state through tanh (to push the values to be between −1 and 1) and multiply it by the output of the sigmoid gate, so that we only output the parts we decided to.

For the language model example, since it just saw a subject, it might want to output information relevant to a verb, in case that’s what is coming next. For example, it might output whether the subject is singular or plural, so that we know what form a verb should be conjugated into if that’s what follows next.

마지막으로 출력 할 내용을 결정해야합니다. 이 출력은 셀 상태를 기반으로하지만 필터링 된 버전입니다. 먼저 셀 상태에서 출력 할 부분을 결정하는 시그 모이 드 레이어를 실행합니다. 그런 다음 tanh를 통해 셀 상태를 입력하고 (값을 -1과 1 사이로 밀어 냄) 시그 모이 드 게이트의 출력을 곱하여 결정한 부분 만 출력하도록합니다.

언어 모델 예의 경우 주제를 방금 보았 기 때문에 동사와 관련된 정보를 출력하고 싶을 수 있습니다. 예를 들어, 주어가 단수인지 복수인지를 출력 할 수 있으므로 다음에 따라 오는 경우 동사의 형태가 어떤 형태로 활용되어야하는지 알 수 있습니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-focus-o.png)

## Variants on Long Short Term Memory

What I’ve described so far is a pretty normal LSTM. But not all LSTMs are the same as the above. In fact, it seems like almost every paper involving LSTMs uses a slightly different version. The differences are minor, but it’s worth mentioning some of them.

One popular LSTM variant, introduced by [Gers & Schmidhuber (2000)](ftp://ftp.idsia.ch/pub/juergen/TimeCount-IJCNN2000.pdf), is adding “peephole connections.” This means that we let the gate layers look at the cell state.

지금까지 설명한 것은 매우 일반적인 LSTM입니다. 그러나 모든 LSTM이 위와 동일하지는 않습니다. 사실 LSTM과 관련된 거의 모든 논문이 약간 다른 버전을 사용하는 것 같습니다. 차이는 사소하지만 몇 가지를 언급 할 가치가 있습니다.

Gers & Schmidhuber (2000)가 도입 한 인기있는 LSTM 변형 중 하나는 "peephole connections"을 추가하는 것입니다. 이것은 게이트 레이어가 셀 상태를 보게 함을 의미합니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-var-peepholes.png)

The above diagram adds peepholes to all the gates, but many papers will give some peepholes and not others.

Another variation is to use coupled forget and input gates. Instead of separately deciding what to forget and what we should add new information to, we make those decisions together. We only forget when we’re going to input something in its place. We only input new values to the state when we forget something older.

위의 다이어그램은 모든 게이트에 틈새를 추가하지만 많은 종이는 일부 틈새를 제공하고 나머지는 제공하지 않습니다.

또 다른 변형은 결합 된 잊어 버림 및 입력 게이트를 사용하는 것입니다. 무엇을 잊고 무엇에 새로운 정보를 추가해야하는지 별도로 결정하는 대신, 우리는 이러한 결정을 함께 내립니다. 그 자리에 무언가를 입력 할 때만 잊어 버립니다. 우리는 오래된 것을 잊었을 때만 새로운 값을 상태에 입력합니다.

![](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-var-tied.png)

A slightly more dramatic variation on the LSTM is the Gated Recurrent Unit, or GRU, introduced by [Cho, et al. (2014)](http://arxiv.org/pdf/1406.1078v3.pdf). It combines the forget and input gates into a single “update gate.” It also merges the cell state and hidden state, and makes some other changes. The resulting model is simpler than standard LSTM models, and has been growing increasingly popular.

LSTM에서 약간 더 극적인 변형은 Cho 등이 소개 한 Gated Recurrent Unit 또는 GRU입니다. (2014). 잊어 버림 및 입력 게이트를 단일 "업데이트 게이트"로 결합합니다. 또한 셀 상태와 숨겨진 상태를 병합하고 다른 변경을 수행합니다. 결과 모델은 표준 LSTM 모델보다 간단하며 점점 인기를 얻고 있습니다.

![A gated recurrent unit neural network.](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-var-GRU.png)

These are only a few of the most notable LSTM variants. There are lots of others, like Depth Gated RNNs by [Yao, et al. (2015)](http://arxiv.org/pdf/1508.03790v2.pdf). There’s also some completely different approach to tackling long-term dependencies, like Clockwork RNNs by [Koutnik, et al. (2014)](http://arxiv.org/pdf/1402.3511v1.pdf).

Which of these variants is best? Do the differences matter? [Greff, et al. (2015)](http://arxiv.org/pdf/1503.04069.pdf) do a nice comparison of popular variants, finding that they’re all about the same. [Jozefowicz, et al. (2015)](http://jmlr.org/proceedings/papers/v37/jozefowicz15.pdf)tested more than ten thousand RNN architectures, finding some that worked better than LSTMs on certain tasks.

이들은 가장 주목할만한 LSTM 변형 중 일부에 불과합니다. Yao 등의 Depth Gated RNN과 같은 많은 다른 것들이 있습니다. (2015). 또한 Koutnik 등의 Clockwork RNN과 같이 장기 종속성을 해결하는 완전히 다른 접근 방식이 있습니다. (2014).

다음 중 가장 좋은 변형은 무엇입니까? 차이점이 중요합니까? Greff, et al. (2015)는 인기있는 변종을 멋지게 비교하여 모두 거의 동일하다는 것을 확인했습니다. Jozefowicz, et al. (2015)는 10,000 개 이상의 RNN 아키텍처를 테스트하여 특정 작업에서 LSTM보다 더 잘 작동하는 일부를 찾았습니다.

## Conclusion

Earlier, I mentioned the remarkable results people are achieving with RNNs. Essentially all of these are achieved using LSTMs. They really work a lot better for most tasks!

앞서 사람들이 RNN을 통해 달성 한 놀라운 결과에 대해 언급했습니다. 기본적으로이 모든 것은 LSTM을 사용하여 달성됩니다. 대부분의 작업에서 실제로 훨씬 더 잘 작동합니다!

Written down as a set of equations, LSTMs look pretty intimidating. Hopefully, walking through them step by step in this essay has made them a bit more approachable.

일련의 방정식으로 작성된 LSTM은 꽤 위협적인 것처럼 보입니다. 바라건대,이 에세이에서 단계별로 그들을 훑어 보면서 좀 더 접근하기 쉽게 만들었습니다.

LSTMs were a big step in what we can accomplish with RNNs. It’s natural to wonder: is there another big step? A common opinion among researchers is: “Yes! There is a next step and it’s attention!” The idea is to let every step of an RNN pick information to look at from some larger collection of information. For example, if you are using an RNN to create a caption describing an image, it might pick a part of the image to look at for every word it outputs. In fact, [Xu, _et al._(2015)](http://arxiv.org/pdf/1502.03044v2.pdf) do exactly this – it might be a fun starting point if you want to explore attention! There’s been a number of really exciting results using attention, and it seems like a lot more are around the corner…

LSTM은 우리가 RNN으로 달성 할 수있는 중요한 단계였습니다. 의아해하는 것은 자연스러운 일입니다. 또 다른 큰 단계가 있습니까? 연구자들의 공통된 의견은“예! 다음 단계가 있습니다. 주목입니다!” 아이디어는 RNN의 모든 단계에서 더 큰 정보 모음에서 볼 정보를 선택하도록하는 것입니다. 예를 들어, RNN을 사용하여 이미지를 설명하는 캡션을 만드는 경우 이미지의 일부를 선택하여 출력하는 모든 단어를 볼 수 있습니다. 사실 Xu, et al. (2015)은 정확히 이것을합니다.주의를 끌고 싶다면 재미있는 시작점이 될 것입니다! 관심을 사용하여 정말 흥미 진진한 결과가 많이 나왔고 앞으로 더 많은 결과가 나올 것 같습니다.

Attention isn’t the only exciting thread in RNN research. For example, Grid LSTMs by [Kalchbrenner, _et al._ (2015)](http://arxiv.org/pdf/1507.01526v1.pdf) seem extremely promising. Work using RNNs in generative models – such as [Gregor, _et al._ (2015)](http://arxiv.org/pdf/1502.04623.pdf), [Chung, _et al._ (2015)](http://arxiv.org/pdf/1506.02216v3.pdf), or [Bayer & Osendorfer (2015)](http://arxiv.org/pdf/1411.7610v3.pdf) – also seems very interesting. The last few years have been an exciting time for recurrent neural networks, and the coming ones promise to only be more so!

Attention은 RNN 연구에서 유일하게 흥미로운 주제가 아닙니다. 예를 들어, Kalchbrenner 등의 Grid LSTM. (2015)는 매우 유망 해 보입니다. Gregor 등의 생성 모델에서 RNN을 사용하여 작업합니다. (2015), Chung, et al. (2015) 또는 Bayer & Osendorfer (2015) – 또한 매우 흥미로워 보입니다. 지난 몇 년은 반복되는 신경망에 흥미 진진한시기였으며 앞으로 나올 것들은 더 많은 것을 약속합니다!

## Acknowledgments

I’m grateful to a number of people for helping me better understand LSTMs, commenting on the visualizations, and providing feedback on this post.

I’m very grateful to my colleagues at Google for their helpful feedback, especially [Oriol Vinyals](http://research.google.com/pubs/OriolVinyals.html), [Greg Corrado](http://research.google.com/pubs/GregCorrado.html), [Jon Shlens](http://research.google.com/pubs/JonathonShlens.html), [Luke Vilnis](http://people.cs.umass.edu/~luke/), and [Ilya Sutskever](http://www.cs.toronto.edu/~ilya/). I’m also thankful to many other friends and colleagues for taking the time to help me, including [Dario Amodei](https://www.linkedin.com/pub/dario-amodei/4/493/393), and [Jacob Steinhardt](http://cs.stanford.edu/~jsteinhardt/). I’m especially thankful to [Kyunghyun Cho](http://www.kyunghyuncho.me/) for extremely thoughtful correspondence about my diagrams.

Before this post, I practiced explaining LSTMs during two seminar series I taught on neural networks. Thanks to everyone who participated in those for their patience with me, and for their feedback.

* * *

  1. In addition to the original authors, a lot of people contributed to the modern LSTM. A non-comprehensive list is: Felix Gers, Fred Cummins, Santiago Fernandez, Justin Bayer, Daan Wierstra, Julian Togelius, Faustino Gomez, Matteo Gagliolo, and [Alex Graves](https://scholar.google.com/citations?user=DaFHynwAAAAJ&hl=en).[↩](https://colah.github.io/posts/2015-08-Understanding-LSTMs/#fnref1)

* * *

#### More Posts

[

![](https://colah.github.io/images/post-covers/attention.png)

### Attention and Augmented Recurrent Neural Networks

#### _On Distill_

](http://distill.pub/2016/augmented-rnns/)[

![](https://colah.github.io/posts/2014-07-Conv-Nets-Modular/img/fig.png)

### Conv Nets

#### A Modular Perspective

](https://colah.github.io/posts/2014-07-Conv-Nets-Modular/)[

![](https://colah.github.io/images/post-covers/topology.png)

### Neural Networks, Manifolds, and Topology

](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)[

![](https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/img/Mikolov-GenderVecs.png)

### Deep Learning, NLP, and Representations

](https://colah.github.io/posts/2014-07-NLP-RNNs-Representations/)

  