"""test1
case1とcase2は小さい順に並んでいるケースだけど、問題文に返り値のリストはソートされてないといけないと言うことは、適当に数字が格納されているケースまで想定しなければならないってことだよね。
データ構造を考えたけど、set()でやれば終わりじゃ無いか?
set()でやったときの計算量を概算したいけどどうやって削除しているのかを理解してないので答えられない。step2で調べます。
これは削除じゃなくて前から見て行ってあったら追加しない、なかったら追加と言う方法になるのか。ただその場合は、結局全部見ることになるので時間計算量はO(n)になりそう?

[1, 2]がListNodeの型じゃ無いって言われた。その通りだけどどう解こう。これは変数=ListNode()をすれば良いね。

結局30分を経過したので解けなかったが、最終的な方針としては以下のようにやった。
1. while文でリストに重複していないものを格納してからsorted()で整列。
2. ListNodeオブジェクトを生成し1で作成したリストをもとに格納していく。ここでは.valに1で作成したリストの要素を格納。nextには次の要素を格納していく。

ここで詰まったことは、主に二つ。一つ目は、与えられた数字の最後のみが格納されているListNodeオブジェクトが生成されてしまう。これはnextの扱い方がよくわからなかったため。二つ目は、以下のエラー文の通り。

AttributeError: 'int' object has no attribute 'val'
    ^^^^^^^^^^^^^^^^^^^^
non_overlap_node.val = non_overlap_node_list[i]

なんでこうなるのかよくわからん。

変数名に関しては、長くなっていることは理解した上でnon_overlap_nodeを最初につけている。
ただし、これが可読性のある変数名であるかは客観的に判断しかねるのでコードレビューをされる方には、ぜひ意見をお伺いしたい。
30分
"""
non_overlap_node_list = list()
        node = head
        
        while node:
            if node.val not in non_overlap_node_list:
                non_overlap_node_list.append(node.val)

            node = node.next
        
        non_overlap_node_length = len(non_overlap_node_list)
        non_overlap_node_list = sorted(non_overlap_node_list)
        non_overlap_node = ListNode()
        
        for i in range(non_overlap_node_length):
            non_overlap_node.val = non_overlap_node_list[i]

            if i == non_overlap_node_length-1:
                non_over_lap_node.next = None
            else:
                non_overlap_node.next = non_overlap_node_list[i+1] 

            non_overlap_node = non_overlap_node.next

        return non_overlap_node

"""step2
なんかそもそもListNode、連結リストの概念を間違えて理解していたっぽいのでstep1は的外れな解答をしていることがわかった。
あとは142でもそうだったけど問題文が読めていなさすぎる、、、sorted listが与えられているからソートしているかを判別するかとかは今回の問題だとどうでも良い。
仕組みを理解すればどうってことない問題だった(1分30秒)。一つ気になるのはnode_valという変数だけど、これは読みやすいのか? node_valとnode.valで混同しそう。https://discord.com/channels/1084280443945353267/1225849404037009609/1234206158630289450 にcurrentを変数名につけるときのことについて書いてあるんだけど(前回指摘された)何か最適なのはあるのだろうか。
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = head
        node_val = head.val

        while node and node.next:
            if node.next.val == node_val:
                node.next = node.next.next
            else:
                node = node.next
                node_val = node.val

        return head

"""step3
1分30分
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        node = head
        node_val = node.val

        while node and node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
                node_val = node.val

        return head
