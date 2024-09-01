"""step1 
141と似たような問題、違いは答えの出力が循環が始まる位置を求められていること。
以下のように解こうと思う。
set()で置いてwhile文を用いて循環しているノードを探し出す。
これだと位置を返すのが難しいな。
dict形式で位置とノードを格納すればできるかも。

インデックスとなるposをkeyとして、nodeをvalueに格納すれば、node.nextをしてdictの中に入っているかを確認すればよい。

nullって書いてあるけどpythonだとNoneだよな?
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node = {}
        node = head
        pos = 0

        while node:
            if node in visited_node.values():
                return node
            visited_node[pos] = node
            pos += 1
            node = node.next

        return None

"""step2
141のコードレビューで指摘された、最初にアルゴリズムを言語化するというのはできたが、時間計算量と空間計算量を概算するという過程を忘れていたので、次回では忘れずにやりたい。
解答を見る感じだと141みたいにフロイドの循環アルゴリズムを使う方法があるっぽい。だけど理由がわからない。

https://github.com/h1rosaka/arai60/pull/4#discussion_r1722542513　プライベートメソッドだとアンダースコアをつけるのが普通なんですね。

というか、141ではset()でやって、しかも最初の方針でもset()を使うようにと書いているのになぜか今回のケースだとできなくねと判断してdict{}でやってしまっている。他のデータ構造でも代用できたと、ポジティブに捉えることができるが計算も遅いし、実装としてはあまりよろしくない。
あ、これは問題を読み間違えていてnodeを返すのではなく位置を返すと勘違いしていることから起きたことですね。結局テストケースを試してみて位置を返すのではなくnodeを返すんじゃんと気づき、その場でdictをささっと修正して提出したのが原因なようです。落ち着きましょう。

dictとset()で解いた場合、それぞれで比較してみましたが速度の違いが断然違いますね。なんでかを調べます。

このステップでは、set()に直した場合でやった。もう一つの別解としてフロイドの循環法を使っても解いてみた。多くの解答では2回目にポインタを動かす操作(コードで言うと2回目のwhile文)をするときにheadを動かしていたが、headを動かすことは可読性の観点から抵抗があったのでslowをもう一度初期化して解いた。コードの行数を減らすと言う意味では、初期化をせずにheadを使うべきだがそれを言ってしまうとfast = slow = headだったりそもそも最初に2変数を定義する意味も薄れてしまうなと感じたので、可読性を意識して初期化をした。
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node = set()
        node = head
        while node:
            if node in visited_node:
                return node
            visited_node.add(node)
            node = node.next

        return None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast

        return None

"""step3
両方の解放とも1分で解答
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_node = set()
        node = head

        while node:
            if node in visited_node:
                return node
            visited_node.add(node)
            node = node.next

        return None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                slow = head
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next

                return fast

        return None
"""
