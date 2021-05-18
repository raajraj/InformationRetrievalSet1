# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Raajitha Rajkumar 862015848
## Team member 2 - Russell Brown 862024798

## DESIGN

##### For this assignment, we had to create an inverted index that maps documents and terms together from the data provided. For our design, we used python and we put mainly everything in parsing.py and a small command-line interface in read_index.py. In parsing.py, we first go through every single file, every document, and every word in the text. The word is made into lower case and stripped of punctuation except for periods in between letters and numbers. In python, we used sets so that way terms cannot repeat and we also check for stop words. This is placed into a token data structure that is a part of a bigger set. The documents are placed into a document data structure as well. As we traverse, we assign document IDs and term IDs and the number of total terms and distinct terms. Once the entire data is traversed through, we have our inverted index with terms and ID's. 

##### When read_index.py is compiled, the file takes in arguments. Depending on the arguments, it will make a call to parsing.py. So if the argument is asking for a term, then read_index.py will grab the term from the command line and feed into parsing.py. The function called in parsing.py will then find the posting list for the term and record the positions and frequencies that will then output the statistics for it. This is the same for a document or for both. 

## HOW TO COMPILE

##### To run this assignment is simple, but can only be done a specific way. First, go to the directory with the given files. To look up a term, it must be done in this specific format...

```python
$ python3 read_index.py --term [term]
```

##### To look up a document, it must be done in this specific format...

```python
$ python3 read_index.py --doc [doc]
```
##### To look up both, it must be done in this specific format...

```python
$ python3 read_index.py --term [term] --doc [doc]
```
##### Anything that is not in that format will result in an error. A term or document that does not exist will also result in an error. Here are some examples of commands you can put in. 

```python
$python3 read_index.py --term important --doc AP890101-0058

output:

Inverted list for term: important
In document: AP890101-0058
TERMID: 1223
DOCID: 10627
Term frequency in document: 1
Positions: (96,)
```
```python
$ python3 read_index.py --term important 

ouput:

Listing for term: important
Term ID: 1223
Number of documents containing term: 19061
```
