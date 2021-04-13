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
// 👍 2084 👎 0
package main

//leetcode submit region begin(Prohibit modification and deletion)
func trap(height []int) int {
	deque := make(chan int)
	defer close(deque)

	ans := 0

	first, last := -1, -1
	for _, num := range height {
		if num == 0 && len(deque) == 0 {
			continue
		}
		if num != 0 && len(deque) == 0 {
			first = num
			deque <- num
			continue
		}
		if first != -1 && last == -1 {
			if num <= first {
				deque <- num
				continue
			} else {
				last = num
				deque <- num
			}
		}
		if last != -1 {
			if num < last {
				 ans += calcute(deque)
				 deque <- last
				 first = last
				 last = -1
			} else {
				last = num
				deque <- num
			}
		}
	}

	if len(deque) > 1 {
		subHeight := make([]int, len(deque))
		index := len(deque) - 1
		for len(deque) != 0 {
			subHeight[index] = <- deque
		}
		ans += trap(subHeight)
	}
	return ans
}

func calcute(deque chan int) int {
	first := <- deque
	ans := 0
	for len(deque) != 0 {
		num := <- deque
		ans += first - num
	}
	return ans
}
//leetcode submit region end(Prohibit modification and deletion)
