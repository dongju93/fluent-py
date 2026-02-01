import collections
from random import choice

"""
- collections.namedtuple은 내부적으로 type() 메타클래스를 사용하여 동적으로 클래스를 생성한다.
- 반환되는 Card 클래스는 tuple의 서브클래스이므로 불변(immutable)이며, 인스턴스는 튜플과 동일하게 해시 가능(hashable)하고 메모리 효율적이다.
- 필드명은 _fields 속성으로 접근 가능하며, 인덱스와 속성 두 가지 방식으로 값을 읽을 수 있다.
"""
Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """
    - ranks와 suits는 클래스 변수(class variable)로, 모든 인스턴스가 공유하는 단일 객체이다.
    - 이는 각 인스턴스마다 복사되지 않으며, 인스턴스에서 읽을 때 클래스의 __dict__를 통해 조회된다.
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        """
        - 리스트 컴프리헤션의 루프 순서는 왼쪽(suit)이 외부 루프, 오른쪽(rank)이 내부 루프이다.
        - 따라서 카드 순서는 suit 단위로 묶이며, 각 suit 내에서 rank가 2~A 순으로 나온다.
        - 접두사 _은 외부에서 직접 접근하지 않음을 암시하는 관례이며, __getitem__을 통해 간접적으로만 접근하도록 설계되었다.
        """
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    """
    - __len__을 정의하면 len() 내장함수와 bool() 변환이 작동한다.
    - bool()은 __bool__이 없으면 __len__의 반환값으로 진리값을 판단한다 (0이면 False).
    """

    def __len__(self):
        return len(self._cards)

    """
    - __getitem__은 단순히 인덱스 접근만 제공하는 것이 아니다.
    - Python은 __iter__가 정의되지 않은 경우, __getitem__을 0부터 순차적으로 호출하여 반복(iteration) 프로토콜의 폴백(fallback)으로 사용한다.
    - 이로 인해 for 루프, in 연산자, list() 변환, random.choice() 등이 별도의 구현 없이 자동으로 작동한다.
    - 또한 position에 list의 슬라이스 객체가 전달되면 슬라이싱도 지원된다.
    """

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    # 카드 1장 출력
    beer_card = Card("7", "diamonds")
    print(beer_card)

    # 카드 덱 생성
    deck = FrenchDeck()
    print(len(deck))

    # 덱의 카드 알아내기
    print(deck[0])
    print(deck[-1])

    # 무작위 카드 고르기, choice 사용
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
