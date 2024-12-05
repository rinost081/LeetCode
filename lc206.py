"""step1
単純にポインタの付け替えをすれば良さそう。
手がつけられなかった。わからなかった点としては、どうやって最後の要素(tail)にアクセスするのかと、そこから逆向きに動かす操作方法がわからなかった。解答を見てなんとなくの理解をした(手を動かして実際に操作することまでわかったが、感覚的に掴めていない)。
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp

        return node

"""step2
Discordを遡ってみて、参考にしたPRを以下に記します。
https://github.com/ichika0615/arai60/pull/6#discussion_r1864910519
https://github.com/katataku/leetcode/pull/7#discussion_r1860201328
https://github.com/konnysh/arai60/pull/7#discussion_r1845699956
https://github.com/tarinaihitori/leetcode/pull/6#issuecomment-2439783292



この問題の解き方は以下の方法がありそう
1. スタックで繋ぎ変え
class Solution:
    def reverseList(self, head: [Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        while current:
            stack.append(current)
            curent = current.next

        if not stack:
            return None
        reversed_head = stack.pop()
        current = reversed_head

        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None
        
        return reversed_head
時間計算量: O(n), 空間計算量: O(n)
愚直なやり方、

2. スタックなしで繋ぎ変え
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_node = None
        current = head

        while current:
            next_node = current.next
            current.next = reversed_node
            reversed_node = current
            current = next_nodd

        return reversed_node

時間計算量: O(n), 空間計算量: O(n)
step1の変数を変えた改良版、headは動かさないようにしている。また、reversed_nodeと変数名をつけることで逆側からのという問題の文脈を付け加えた。

3. 再帰

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return new_head


4. 逆向きの再帰

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverse_linked_list(head, previous):
            if head is None:
                return previous
            temp = head.next
            head.next = previous
            return _reverse_linked_list(temp, head)

        retrun _reverse_linked_list(head, None)

個人的には3.の再帰よりもこちらの方が2番のやり方に近いと感じていて、分かりやすい。


 再帰で解く時は、recursionErrorと呼ばれるエラーが発生する可能性があるので常にそれを意識する　
"""

"""step3

1分30秒
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        reverse_node = None

        while current:
            next_node = current.next
            current.next = reverse_node
            reverse_node = current
            current = next_node

        return reverse_node

4分
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverse_linked_list(head, previous):
            if head is None:
                return previous
            next_node = head.next
            head.next = previous
            return _reverse_linked_list(next_node, head)

        return _reverse_linked_list(head, None)
"""
