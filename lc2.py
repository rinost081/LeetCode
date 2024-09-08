"""step1
まずは繰り上がりがない単純な場合を考えてみる。
各ノードを参照して足すだけ
l1をreturnすることを考えてdummyを作成
桁が合わない場合のためにパディングをする、ただし効率的ではなさそう.
whileをl1 and l2ではなくl1 or l2にすればよい。ただしこの場合Noneを参照してエラーを起こしそう→起こしたのでそれに対するif分が必要
桁が合わない場合のケースが解けなかった。時間をかければ無理やり解けそうだが、20分を経過したのでやめる。
できなかったことは、l1とl2のどちらかが先にNoneに入るのでそれを阻止して足し算を続けること
解いた時に思ったのはflagをboolにするのではなく0か1を入れて常に足すというコードも書けるのではと思った。
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = l1
        flag = False


        while l1 and l2:
                if flag:
                    l1.val = l1.val + l2.val + 1
                else:
                    l1.val = l1.val + l2.val

                if l1.val > 9:
                    l1.val = l1.val % 10
                    flag = True
                else:
                    flag = False

                l1 = l1.next
                l2 = l2.next
                
        if flag:
            l1.val = 1

        return answer
"""step2
これまでみたいに長々と書かずに解けるものなのだと思ってstep1は途中で辞めたんですけど、別の関数を作ったり結構長めなコードを書いている人を見たので変な先入観は捨てます、、、
step1でやりたかった処理は以下の通り
時間計算量は0(n)
空間計算量はO(n) 両者ともl1とl2で長さが大きい方をnとしている
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        answer_head = answer
        carry = 0

        while l1 or l2:
            answer.next = ListNode()
            answer = answer.next

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            answer.val = l1_val + l2_val + carry

            if answer.val > 9:
                answer.val = answer.val % 10
                carry = 1
            else:
                carry = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            answer.next = ListNode(1)

        return answer_head.next
"""
step3
2分50秒
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(-1)
        answer_head = answer
        carry = 0

        while l1 or l2:
            answer.next = ListNode()
            answer = answer.next

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            answer.val = l1_val + l2_val + carry

            if answer.val > 9:
                answer.val = answer.val % 10
                carry = 1
            else:
                carry = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            answer.next = ListNode(1)

        return answer_head.next
