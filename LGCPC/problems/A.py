"""
진우는 정수론 기말고사 시험에서 사용할 계산기를 구매했다. 계산기는 법 $P$에 대해 음이 아닌 정수 간의 덧셈과 곱셈, 그리고 괄호를 이용한 연산의 우선순위 지정을 지원한다. 즉, 계산기는 아래 BNF 표기법에서 <expr>에 해당하는 형태의 수식의 값을 $P$로 나눈 나머지를 계산할 수 있다.

<expr> ::= <term> | <expr> + <term>
<term> ::= <factor> | <term> * <factor>
<factor> ::= <number> | ( <expr> )
<number> ::= <digit> | <number> <digit>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
일반적으로 계산기는 덧셈보다 곱셈을 먼저, 괄호 밖에 있는 연산보다 괄호 안에 있는 연산을 먼저 계산하고, 우선 순위가 동등하다면 왼쪽에 있는 연산부터 계산한다. 하지만 이 계산기는 고장나서 덧셈과 곱셈의 우선 순위를 동등하게 취급하며, 우선 순위가 동등한 연산은 임의 순서대로 계산한다. 즉, (2+2*2)+3은 괄호 안에 있는 덧셈을 곱셈보다 먼저 계산해서 (4*2)+3 = 11로 계산할 수도 있고, 곱셈을 덧셈보다 먼저 계산해서 (2+4)+3 = 9로 계산할 수도 있다.

계산기가 고장났다는 사실을 시험 10분 전에 깨달은 진우는 급한대로 여는 괄호(‘(’)와 닫는 괄호(‘)’)를 적당히 추가해서 고장난 계산기에서도 항상 의도한 대로 계산되도록 수식을 변환해서 입력하려고 한다. 진우가 원래 계산하고자 했던 수식 $S$가 주어지면, 고장난 계산기에서 항상 진우가 의도한 결과를 출력하도록 여는 괄호와 닫는 괄호를 적당히 삽입해서 수식을 변환하는 프로그램을 작성하라.

입력
첫 번째 줄에 수식의 길이 $N$와 법 $P$가 공백을 사이에 두고 주어진다.

두 번째 줄에 진우가 원래 계산하려고 했던 수식 $S$가 주어진다.

출력
첫 번째 줄에 변환된 수식 $T$의 길이 $M$을 출력한다.

두 번째 줄에 변환된 수식 $T$를 출력한다.

제한
$1 <= N <= 50$ 
$2\le P\le 20$ 
$1\le M\le 100$ 
$S,T$는 숫자와 ‘+’, ‘*’, ‘(’, ‘)’로 구성된 문자열이다.
$S$는 본문의 BNF 표기법에서 <expr>에 해당하는 형태의 수식이다.
$T$는 $S$에 여는 괄호와 닫는 괄호만 삽입한 문자열이어야 한다.
서브태스크
번호	배점	제한
1	43	
$S$는 숫자와 ‘+’, ‘*’로 구성된 문자열이다.

2	57	
추가 제약 조건 없음.

예제 입력 1 
9 3
(2+2*2)+3
예제 출력 1 
11
(2+(2*2))+3
예제 입력 2 
9 2
(2+2*2)+3
예제 출력 2 
9
(2+2*2)+3
"""

import sys

input = sys.stdin.readline

N, P = map(int, input().rstrip("\n").split())

line = input().rstrip("\n")
queue = []


def helper():
  if len(queue) == 0:
    return
  tmp = queue.pop()
  queue.append('(')
  queue.append(tmp)
  queue.append('*')


for i in range(len(line)):
  if line[i] == '*':
    helper()
    queue.append(line[i + 1])
    queue.append(')')