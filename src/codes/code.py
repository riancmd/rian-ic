import math

# define um template para um código de comprimento n(length)
# e as principais funções da teoria dos códigos
class Code:
    # recebe o comprimento e o elemento identidade
    def __init__(self,length,identity):
        self.length = length
        self.code = []
        self.identity = identity

    # adiciona nova palavra ao código
    def addWord(self,word:Word):
        if word.getLength() != self.length:
            print(f'\nPalavra com comprimento diferente do código.')
            return 
        self.code.append(word)

    # compara todos os elementos e acrescenta num contador para cada elemento diferente
    def hammingDistance(self,w1:'Word',w2:'Word'):
        hammingDistance = 0

        for i in range(self.length):
            if w1.word[i] != w2.word[i]:
                hammingDistance += 1

        return hammingDistance

    # compara todas as distâncias de hamming até encontrar a menor
    # mesmo que minimumWeight
    def minDistance(self):
        minDistance = self.hammingDistance(self.code[0],self.code[0])
        for word1 in self.code:
            for word2 in self.code:
                if self.hammingDistance(word1.code,word2.code) < minDistance:
                    minDistance = self.hammingDistance(word1.code,word2.code)
        
        return minDistance
                
    # calcula o peso de um elemento do código linear
    def weight(self,w1:Word):
        weight = self.hammingDistance(w1.word,self.identity)
        return weight

    # retorna a capacidade do código (quanto se pode corrigir) - error correction code capacity
    def ECCC(self):
        return math.floor((self.minDistance() - 1)/2)
    
    # retorna a capacidade de detecção de erros
    def errorDetectionCapacity(self):
        return self.minDistance() - 1

class Word:
    def __init__(self, length):
        if length >1:
            self.word = [0] * length
        else:
            self.word = [0]

    def getLength(self):
        return len(self.word)