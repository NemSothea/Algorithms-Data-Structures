import UIKit

/*
 * Complete the 'simpleArraySum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY ar as parameter.
 -> https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
 */

func simpleArraySum(ar: [Int]) -> Int {
    // Write your code here
   return ar.reduce(0, +)
}


/*
 * Complete the 'compareTriplets' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

func compareTriplets(a: [Int], b: [Int]) -> [Int] {
    var scoreA : Int = 0
    var scoreB : Int = 0
    
    for score in 0..<a.count {
        if a[score] > b[score] {
            scoreA += 1
        }else if a[score] < b[score] {
            scoreB += 1
        }
    }
    return [scoreA,scoreB]
}

print(compareTriplets(a: [1,2,3], b: [3,2,1]))
