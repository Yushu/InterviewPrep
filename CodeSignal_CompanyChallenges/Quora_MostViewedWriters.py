from collections import defaultdict
from bisect import bisect
from operator import itemgetter
import itertools

def solution(topicIds, answerIds, views):
    answers_table = dict()
    for topics, answers in zip(topicIds, answerIds):
        for a in answers:
            answers_table[a] = topics
    topics = list(set(itertools.chain(*topicIds)))
    topics.sort()
    topics_table = dict()
    for view in views:
        ans_id = view[0]
        u_id = view[1]
        count = view[2]
        current_topics = answers_table[ans_id]
        for ct in current_topics:
            if ct not in topics_table:
                topics_table[ct] = dict()
            if u_id not in topics_table[ct]:
                topics_table[ct][u_id] = count
            else:
                topics_table[ct][u_id] += count
    output = []
    for top in topics:
        v = topics_table.get(top, {})
        output.append([list(p) for p in sorted(sorted(v.items(), key = lambda x: x[0]), key = lambda x : x[1], reverse=True)])
    return output