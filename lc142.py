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
