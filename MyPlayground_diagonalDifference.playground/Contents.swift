import Foundation

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

func diagonalDifference(arr: [[Int]]) -> Int {
    // Write your code here
    let n = arr.count
    var primaryDiagonalSum = 0
    var secondDiagonalSum = 0
    for i in 0..<n {
        primaryDiagonalSum += arr[i][i]
        secondDiagonalSum += arr[i][n - 1 - i]
    }
    return abs(primaryDiagonalSum - secondDiagonalSum)
}
let arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
print(diagonalDifference(arr: arr))

/**
 Explanation :
1. n = arr.count: This gives the size of the matrix (number of rows or columns since it's a square matrix).
 
2. Primary Diagonal Sum: We loop over each row i and sum the elements where the row index equals the column index (arr[i][i]).

 3. Secondary Diagonal Sum: We sum the elements where the row index i and column index are n - 1 - i (arr[i][n - 1 - i]).

4. Absolute Difference: Finally, we return the absolute difference between the two sums using abs().
 
 let arr = [
     [11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]
 ]
 
 Explanation of the Example:
 - Primary Diagonal: 11 + 5 + (-12) = 4
 - Secondary Diagonal: 4 + 5 + 10 = 19
 - Absolute Difference: |4 - 19| = 15
 -> This solution efficiently handles the problem in O(n) time complexity, where n is the size of the matrix.
 
*/
