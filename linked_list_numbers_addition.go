/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    var result, currentNode *ListNode
    var carry int
    for l1 != nil || l2 != nil || carry == 1 {
        columnSum := carry
        if l1 != nil {
            columnSum += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            columnSum += l2.Val
            l2 = l2.Next
        }
        var adjusted int
        if columnSum > 9 {
            adjusted = columnSum - 10
            carry = 1
        } else {
            adjusted = columnSum
            carry = 0
        }
        if result == nil {
            currentNode = &ListNode{
                Val : adjusted,
                Next : nil,
            }
            result = currentNode
        } else {
            newNode := &ListNode{
                Val : adjusted,
                Next : nil,
            }
            currentNode.Next = newNode
            currentNode = newNode
        }
    }
    return result
}
