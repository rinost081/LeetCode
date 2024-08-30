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
