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

    def add_document(self, doc_name, list_of_words):
        # Input: doc_name = "foo", list_of_words = ["a", "b", "c", "d", "e", "f", "g", "h"]
        # return: None
        # change the documents obj, add new document with its normalized terms frequency       
        # doc_name is the document name
        #list_of_words is the tokenized document, in this example, this document is "a b c d ..."
        
        # create a dict to store the word frequency
        doc_dict = {}
        # iterate word through list
        for w in list_of_words:
            
            # get the count of key w, if none, set to 0, add increment of 1
            doc_dict[w] = doc_dict.get(w, 0.) + 1.0
            
            # update corpus dict count
            # corpus_dict records the overall word and word frequency statistics.
            self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0
            
            

        # normalizing the dictionary
        # get total numbers of words
        length = float(len(list_of_words))
        
        # go into this document, check the word frequencies and normalize it.
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] / length

        # add the normalized document to the corpus
        # documents is a list, add doc_name and doc frequency to the documents.
        # for each documents
        # documents = [[document1, {word1: freq1}], [document2, {word1:freq1, word2:freq2}], [document3, {worda: freqa}]]
        self.documents.append([doc_name, doc_dict])

    def similarities(self, list_of_words):
        """Returns a list of all the [doc_name, similarity_score] pairs relative to a list of words.
        Input: list_of_words like ["a", "b", "c"]
        Output: document name with similarity score [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]
        """

        # building the query dictionary
        # querys word freqency {word: freq}
        query_dict = {}
        
        for w in list_of_words:
            query_dict[w] = query_dict.get(w, 0.0) + 1.0

        # normalizing the query 
        length = float(len(list_of_words))
        
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
                    
                    # query_dict[k] / self.corpus_dict[k]: 词在文章中出现的次数/该词在语料库中出现的次数
                    score += (query_dict[k] / self.corpus_dict[k]) + (doc_dict[k] / self.corpus_dict[k])
                    # [['foo', 0.6875], ['bar', 0.75], ['baz', 0.0]]  + (doc_dict[k] / self.corpus_dict[k])
                    # [['foo', 3.5], ['bar', 3.5], ['baz', 0.0]] + 1
                    
                # else, ignore it, cannot deal with out of vocabulary problem.
            sims.append([doc[0], score])

        return sims

table = TfIdf()
table.add_document("foo", ["a", "b", "c", "d", "e", "f", "g", "h"])
table.add_document("bar", ["a", "b", "c", "i", "j", "k"])
table.add_document("baz", ["k", "l", "m", "n"])


print table.similarities(["a", "b", "c"])