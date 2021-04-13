package main

import "fmt"

func trap(height []int) int {
	ans, left, right := 0, 0, 0

	for index, num := range height {
		if index == 0 {
			continue
		}
		if num < height[left] {
			ans += height[left] - 1
		} else {
			right = index
		}
	}

	if left != right {
		subHeight := make([]int, right - left + 1)
		index := right - left
		for i := left; i <= right; i++ {
			subHeight[index] = height[i]
			index -= 1
		}
		ans += trap(subHeight)
	}

	return ans
}

func cal(height []int, left int, right int) int {
	fmt.Println(height, left, right)
	ans := 0
	for i := left + 1; i < right; i++ {
		if height[i] >= height[left] {
			continue
		}
		ans += height[left] - height[i]
	}
	return ans
}

func main() {
	fmt.Println(trap([]int{0,1,0,2,1,0,1,3,2,1,2,1}))
}