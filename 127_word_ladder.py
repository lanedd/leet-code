from collections import defaultdict, deque
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Solution(object):
    def ladderLength(self, begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: List[str]
        :rtype: int
        """
        word_list.append(begin_word)
        
        # Build Graph
        mutations = defaultdict(set)
        for word in word_list:
            for index in range(len(word)):
                mutated = f"{word[:index]}*{word[index+1:]}"
                mutations[mutated].add(word)
        logger.debug(mutations)
        edges = defaultdict(set)
        for words in mutations.values():
            for word in words:
                edges[word].update(words)
                logger.debug(words)
                logger.debug(edges[word])
        logger.debug(edges)
        for word, words in edges.items():
            words.remove(word)
        edges = {word: words for word, words in edges.items() if len(words) > 0}
        logger.debug("\nEdges built")
        logger.debug(edges)

        # BFS
        queue = deque([(begin_word, 1), ])
        explored = set()
        while len(queue) > 0:
            word, distance = queue.popleft()
            if word in explored:
                continue
            if word == end_word:
                return distance
            if word in edges:
                words = edges[word]
                add_to_queue = [(word, distance + 1) for word in words]
                queue.extend(add_to_queue)
            explored.add(word)
        return 0


print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
