//给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
//
// 
//
// 示例 1： 
//
// 
//
// 
//输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
//输出：6
//解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
// 
//
// 示例 2： 
//
// 
//输入：height = [4,2,0,3,2,5]
//输出：9
// 
//
// 
//
// 提示： 
//
// 
// n == height.length 
// 0 <= n <= 3 * 104 
// 0 <= height[i] <= 105 
// 
// Related Topics 栈 数组 双指针 动态规划 
// 👍 2122 👎 0


import java.util.Deque;
import java.util.LinkedList;

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int trap(int[] height) {
        int ans = 0;
        Deque<Integer> deque = new LinkedList<>();
        for (int i = 0; i < height.length; i++) {
            if (deque.isEmpty() && height[i] == 0) {
                continue;
            }
            if (height[i] < deque.getLast()) {
                ans += cal(deque);
                deque.add(height[i]);
                continue;
            }
            deque.add(height[i]);
        }
        return ans;
    }

    private int cal(Deque<Integer> deque) {
        int amount = 0;
        int head = deque.pollFirst();
        deque.pollLast();
        while (!deque.isEmpty()) {
            amount += head - deque.pollFirst();
        }
        return amount;
    }
}
//leetcode submit region end(Prohibit modification and deletion)
