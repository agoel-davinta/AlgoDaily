package main

import (
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// depth first search O(n)
// This a not a good way to do dfs cos it is nested
func closestValue0(root *TreeNode, target float64) int {
	closest := root.Val
	var dfs func(cur *TreeNode)
	dfs = func(cur *TreeNode) {
		diff := math.Abs(target - float64(closest))
		cur_diff := math.Abs(target - float64(cur.Val))
		if cur_diff < diff {
			closest = cur.Val
		}
		if cur.Left != nil {
			dfs(cur.Left)
		}
		if cur.Right != nil {
			dfs(cur.Right)
		}
	}

	dfs(root)

	return closest
}

// recursion with return value
func closestValue(root *TreeNode, target float64) int {
	cur_diff := math.Abs(target - float64(root.Val))
	left := math.MaxInt64
	right := math.MaxInt64
	if root.Left != nil {
		left = closestValue(root.Left, target)
	}
	left_diff := math.Abs(target - float64(left))
	if root.Right != nil {
		right = closestValue(root.Right, target)
	}
	right_diff := math.Abs(target - float64(right))
	if cur_diff < left_diff && cur_diff < right_diff {
		return root.Val
	} else if left_diff < cur_diff && left_diff < right_diff {
		return left
	} else if right_diff < cur_diff && right_diff < left_diff {
		return right
	}
	return root.Val
}

func main() {
}
