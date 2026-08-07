class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_words = len(words)

        need = {}
        for word in words:
            if word in need:
                need[word] += 1
            else:
                need[word] = 1

        result = []
        for offset in range(word_len):
            left = offset 
            current = {}
            count = 0 

            for right in range(offset, len(s) - word_len + 1, word_len):
                right_word = s[right:right + word_len]
                
                if right_word in need:
                    if right_word in current:
                        current[right_word] += 1
                    else:
                        current[right_word] = 1
                    
                    count += 1

                    while current[right_word] > need[right_word]:
                        left_word = s[left:left + word_len]

                        current[left_word] -= 1
                        if current[left_word] ==  0:
                            del current[left_word]

                        left += word_len
                        count -= 1

                    if count == total_words:
                        result.append(left)

                        left_word = s[left:left + word_len]

                        current[left_word] -= 1
                        if current[left_word] ==  0:
                            del current[left_word]
                        left += word_len
                        count -= 1
                else:
                    current = {}
                    count = 0
                    left = right + word_len
        return result                      
