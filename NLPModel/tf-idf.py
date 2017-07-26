import math

class TfIdf:
    """
    TF-IDF = TF * IDF
    TF = count of words / length of total words
    IDF = log( corpus documents count / (the count of documents that contain this word + 1) )
    """
    
    def __init__(self):
        self.weighted = False
        self.documents = []
        self.corpus_dict = {}
        self.wordPool = {} # stores IDF value
        self.corpus = {}
        self.tfs = {}

    def add_document(self, doc_name, list_of_words):
        # Input: doc_name = "foo", list_of_words = ["a", "b", "c", "d", "e", "f", "g", "h"]
        # return: None
        # change the documents obj, add new document with its normalized terms frequency       
        # doc_name is the document name
        #list_of_words is the tokenized document, in this example, this document is "a b c d ..."
        
        # create a dict to store the word frequency
        doc_dict = {}
        self.corpus[doc_name] = list_of_words
        # iterate word through list
        for term in list_of_words:
            
            # get the count of key w, if none, set to 0, add increment of 1
            doc_dict[term] = doc_dict.get(term, 0.) + 1.0
            
            # update corpus dict count
            # corpus_dict records the overall word and word frequency statistics.
            self.corpus_dict[term] = self.corpus_dict.get(term, 0.0) + 1.0
            
            

        # normalizing the dictionary
        # get total numbers of words
        length = float(len(list_of_words))
        
        # go into this document, check the word frequencies and normalize it.
        for term in doc_dict:
            # doc_dict saves term frequency TF
            doc_dict[term] = doc_dict[term] / length

        # add the normalized document to the corpus
        # documents is a list, add doc_name and doc frequency to the documents.
        # for each documents
        # documents = [[document1, {word1: TF1}], [document2, {word1:TF2, word2:TF3}], [document3, {worda: TFs}]]
        self.documents.append([doc_name, doc_dict])
        self.tfs[doc_name] = doc_dict
        
    def tfidf2(self):
        # idf = log(1 + total documents number / document number that contains the word)
        documentNumber = len(self.documents)
        print 'before'
        print self.documents
        for document in self.documents:
            words = set(document[1].keys())
            for word in words:
                self.wordPool[word] = self.wordPool.get(word, 0.) + 1.0
        
        for word in self.wordPool:
            self.wordPool[word] = math.log(documentNumber/self.wordPool[word]+1, 2)
            
        for document in self.documents:
            for word in document[1]:
                document[1][word] = document[1][word] * self.wordPool[word]
        print 'after'
        print self.documents

    def cosine_similarity(self,v1,v2):
        "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
        print "v1, v2"
        print v1, v2
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        return sumxy/math.sqrt(sumxx*sumyy)

        
    def cosine_similarity2(self, v1, v2):
        dotProduct = sum(a*b for a, b in zip(v1, v2))
        magnitude = math.sqrt(sum(a*a for a in v1)) * math.sqrt(sum(b*b for b in v2))
        if not magnitude:
            return 0
        return dotProduct / magnitude
    
    def calculate(self, query_document):
        query_dict = {}
        for word in query_document:
            query_dict[word] = query_dict.get(word, 0.0) + 1.0

        # normalizing the query 
        length = float(len(query_document))
        
        # get word: freq pair from query dictionary
        for k in query_dict:
            # TF value ready
            if k in self.wordPool:
                query_dict[k] = query_dict[k] / length * self.wordPool[k]
        queryVector = [query_dict[word]*self.wordPool[word] for word in query_document]
        
        print "queryVector"
        print queryVector
        
        for doc_name in self.corpus:
            # document = {doc_name: [word1, word2 ...]}
            v1 = self.corpus[doc_name]
            v1 = [self.tfs[doc_name][word] * self.wordPool[word] for word in v1]
            cs2 = self.cosine_similarity2(v1, queryVector)
            print "TFIDF weighted cosine similarity"
            print cs2

        
    def similarities(self, query_document):
        """Returns a list of all the [doc_name, similarity_score] pairs relative to a list of words.
        Input: list_of_words like ["a", "b", "c"]
        Output: document name with similarity score [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]
        """

        # building the query dictionary
        # querys word freqency {word: freq}
        query_dict = {}
        
        for word in query_document:
            query_dict[word] = query_dict.get(word, 0.0) + 1.0

        # normalizing the query 
        length = float(len(query_document))
        
        # get word: freq pair from query dictionary
        for k in query_dict:
            # normalize query word frequency
            query_dict[k] = query_dict[k] / length

        # computing the list of similarities
        sims = []
        
        # get document from documents, each document contains [doc_name, {word: frequency}]
        for doc in self.documents:
            score = 0.0
            # doc[1] is the word frequency dictionary in corpus {word: freq}
            doc_dict = doc[1]
            
            # get word:freq from query dictionary
            for k in query_dict:
                # if the query word in corpus
                if k in doc_dict:
                    
                    print query_dict[k], doc_dict[k], self.corpus_dict[k]
                    
                    # query_dict[k] / self.corpus_dict[k]
                    score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
                    # [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]  + (doc_dict[k] / self.corpus_dict[k])
                    # [['foo', 3.5], ['bar', 3.5], ['baz', 0.0]] + 1
                    
                # else, ignore it, cannot deal with out of vocabulary problem.
                
            # Fixed TF-IDF score compute
            # How could I compute the TF-IDF score properly? Is it just a score for one word? What if the input is a sentence?
            # 07/23
            sims.append([doc[0], score])

        return sims

table = TfIdf()
table.add_document("doc1", ["a", "b", "c", "d", "e", "f", "g", "h"])
table.add_document("doc2", ["a", "b", "c", "i", "j", "k"])
table.add_document("doc3", ["a", "k", "l", "m", "n"])

table.tfidf2()

doc4 = ["a", "b", "c"]
print "original"
print table.similarities(doc4)
print "tfidf cosine"
print table.calculate(doc4)