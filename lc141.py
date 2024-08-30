"""効率的な方法が特に思いつかなかったので愚直にやろうと思った。また、ListNodeの扱い方がよくわからなかったのでpythonのリストを用いた。一見良さそうなコードが書けたが、Nodeの中に同じ数字が入っているとダメであることに気づかずそこでsubmitも止まってしまった。(15分)"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head_list = []
        while head:
            if head.val in head_list:
                return True
            head_list.append(head.val)
            head = head.next

        return False

"""step2をやった。step1で私が書いたコードと非常に似ていると感じた。違いはset()を使用していること、headをそのまま使用しないで他の変数に置いているというところか。後の違いは私のコードはvalで比較をしているのに対して解答はノードで比較している点だ。この場合はvalとnextの両方が一致しているかみているということなのだろうか。

別解のフロイドの循環検出アルゴリズムは、今の段階で理解できていない。なんで、循環している時はfast.next.nextとslow.nextが同じになるという発送になるのだろうか"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_node = set()
        current_node = head

        while current_node:
            if current_node in visited_node:
                return True
            visited_node.add(current_node)
            current_node = current_node.next

        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

