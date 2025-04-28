"""step1

思考ログ
愚直にやるならforループを回すだけ
少し工夫するならtargetより大きい数字を削除
入出力が負のケースを考慮していなかった
"""

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

"""step2
参考にした方のdiscord一覧
- https://github.com/shintaro1993/arai60/pull/15/files?short_path=70b0510#diff-70b05104dc88196abb247b2c62f918005ded7b778d46b818dbf957c243ee211f
- https://github.com/takumihara/leetcode/pull/1/files#diff-0e987cffc3503d02426293fe621110aa1c7f49e3940742ac0e27bd758446c3ea 
- https://github.com/fhiyo/leetcode/pull/14/files?short_path=050f7e8#diff-050f7e8a6e8dcab5ada34b1061c96b59923387f92e6582826703e46c59d73557

- enumerateを使うやり方を紹介している人がいたが、本質的には変わらないなと思ったため実装は割愛する。
- 引き算をして何かをするというのは発送として持っていたが実装に活かせなかった。
- complementという変数名を使っている人が多数いたが、個人的にあまり使わない言葉であまり見たことない単語だと感じた。単なる勉強不足の可能性もあるので様子を見たいと思い別の変数を名付けた。
- dict型の変数に関しても、XX_to_YYという名前にすることが多そうだと感じた、今回だったらvalue_to_index, num_to_indexなどもありだと思った。
- 今回の問題では明示的に、"You may assume that each input would have exactly one solution"とあったので考えなかったが、エラー時の例外についても頭に入れておくのは良いと思った。(https://discord.com/channels/1084280443945353267/1218740927120674977/1223967037588635658)
"""

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            needed_value = target - nums[i]
            if needed_value in seen:
                return [seen[needed_value], i]

            seen[nums[i]] = i 
```

# step 3
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            needed_value = target - nums[i]
            if needed_value in seen:
                return [seen[needed_value], i]

            seen[nums[i]] = i
```
