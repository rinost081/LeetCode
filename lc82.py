"""step1
基本は83と同じ。
83と同じ方針でやるなら時間計算量はO(n)かな。
方針としては、node.nextを付け替える操作を繰り返すだけ。

やりたいことは、
1. 現在の値と次の値が同じかを比較
2. a. 同じ場合はwhile文を使って、その次の値も同じかを繰り返し比較
   b. 違う場合は次のnodeに進み1に戻る。
3. a. 繰り返して比較するため現在のnodeと連続する最後のnodeを特定
4. a. 現在の一つ前のnode→最後のnodeの次へと付け替える

これを繰り返す。
しかしprevが存在しないため1は現在の値と次の値ではなく、次の値と次の次の値を比較する。2以降もこれに対応するようにずらす。
テストケース２みたいにheadを消さなければならないときはどうするんだ。最初の処理で時間を費やしたので２個目のwhile分は無限ループに入っている。
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        end_node = head

        while end_node.next:
            if end_node.val == end_node.next.val:
                end_node = end_node.next
            else:
                break

        head.next = end_node.next

        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                end_node = node.next.next
                while end_node.next:
                    if node.next.val == end_node.next:
                        end_node = end_node.next
                node.next = end_node.next
            node = node.next

        return head 

"""step2
解答を見る感じ方針としては、大きく間違えているわけではなさそう。
テストケース2みたいにheadを消さないといけない場合に備えてdummy nodeを作成すれば解決。
@h1rosakaさんのプルリクをかなり参考にしました。 (https://github.com/h1rosaka/arai60/pull/6)
時間計算量は全てのnodeを1度みるためO(n)
空間計算量はdummy nodeを作成したときのO(1)→定数空間
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        node = dummy

        while node:
            if node.next and node.next.next and node.next.val == node.next.next.val:
                while node.next and node.next.next and node.next.val == node.next.next.val:
                    node.next = node.next.next
                node.next = node.next.next
            else:
                node = node.next

        return dummy.next

"""step3
1分30秒, step2と同じ
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        node = dummy

        while node:
            if node.next and node.next.next and node.next.val == node.next.next.val:
                while node.next and node.next.next and node.next.val == node.next.next.val:
                    node.next = node.next.next
                node.next = node.next.next
            else:
                node = node.next

        return dummy.next
