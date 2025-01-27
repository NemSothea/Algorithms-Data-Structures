
// Link : https://developer.apple.com/documentation/naturallanguage/creating-a-word-tagger-model
//Creating a word tagger model
//Train a machine learning model to tag individual words in natural language text.
//Overview
//A word tagger is a machine learning model that’s been trained to classify natural language text at the word level.
//
//You train a word tagger by showing it multiple examples of sentences containing words you’ve already tagged — for example, Apple product names like iPad and iPhone.
//
//Import your data
//Start by gathering textual data and importing it into an MLDataTable instance. You can create a data table from JSON and CSV formats.
//
//As an example, consider a JSON file containing sentences with words that you’ve tagged. Each entry contains a pair of keys—tokens and labels:
//
//The value for the tokens key is an array of words and punctuation in an individual sentence.
//
//The value for labels is an array of corresponding labels, or tags, for each of those tokens.
//
//The arrays are the same length, resulting in a one-to-one mapping between each token and its corresponding label.
//
//The JSON snippet below shows three pairs of tokenized sentences with their associated labels.

import CreateML
import SwiftUI

let fileName = "JsonExample"
let fileType = "json"

if let filepath = Bundle.main.path(forResource: fileName, ofType: fileType) {
    do {
        let contents = try String(contentsOfFile: filepath)
        print(contents)
    } catch {
        // contents could not be loaded
    }
} else {
    // example.txt not found!
}
//let data = try MLDataTable(contentsOf: URL(fileURLWithPath:fileType))
//print(data)



