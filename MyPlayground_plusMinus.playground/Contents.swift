import Foundation

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

func plusMinus(arr: [Int]) -> Void {
    // Write your code here
    let n = arr.count
    var positive    = arr.filter {$0 > 0}.count
    var nagative    = arr.filter {$0 < 0}.count
    var zero        = arr.filter {$0 == 0}.count
    
   
    let proportionPositive = Double(positive) / Double(n)
    let proportionNagative = Double(nagative) / Double(n)
    let proportionZero = Double(zero) / Double(n)
    
    print(proportionPositive)
    print(proportionNagative)
    print(proportionZero)

}


print(plusMinus(arr: [-4, 3, -9, 0, 4, 1]))
