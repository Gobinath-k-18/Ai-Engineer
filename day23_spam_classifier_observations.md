# Day 23 — Naive Bayes Spam Classifier

## Objective
Build a simple spam classifier using TF-IDF and Naive Bayes.

## Concepts learned
- Conditional probability and Bayes' theorem
- Naive Bayes classification
- TF-IDF text vectorization
- Training and testing data
- Accuracy, precision, recall, and F1-score

## Implementation
- Created a dataset of 16 text messages: 8 spam and 8 ham.
- Split the dataset into 12 training messages and 4 test messages.
- Used `TfidfVectorizer` to convert text into numerical features.
- Trained a `MultinomialNB` classifier.
- Evaluated predictions using accuracy and a classification report.
- Tested the model on four new messages.

## Results
- Training messages: 12
- Testing messages: 4
- TF-IDF feature count: 50
- Correct test predictions: 4 out of 4
- Test accuracy: 100%

## Limitations
The dataset is very small and contains simple examples. The 100% test accuracy does not demonstrate reliable real-world performance. A larger, more diverse dataset is needed.

## Conclusion
Built an end-to-end text classification pipeline using TF-IDF and Naive Bayes. Learned how to transform text, train a classifier, evaluate predictions, and classify new messages.