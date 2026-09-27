import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        lst = [(-a,'a'), (-b,'b'), (-c,'c')]
        heap = [(val,char) for val,char in lst if val < 0]
        heapq.heapify(heap)
        result = ""
        while heap:
            val, char = heapq.heappop(heap)
            if result[-2:] == 2 * char:
                try:
                    new_val, new_char = heapq.heappop(heap)
                    result += new_char
                    new_val += 1
                    if new_val < 0:
                        heapq.heappush(heap, (new_val,new_char))
                except:
                    break
            else:
                result += char
                val += 1
            if val < 0:
                heapq.heappush(heap, (val,char))
        return result


        
        

        