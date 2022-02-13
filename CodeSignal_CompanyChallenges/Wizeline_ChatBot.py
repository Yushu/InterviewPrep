def solution(conversations, currentConversation):
    nearest_match, max_match, pos = None, -1, -1
    for convo in conversations:
        matching = 0
        distinct = []
        already_seen_word_pos = -1
        for word in currentConversation:
            if word in convo and word not in distinct:
                matching += 1
                distinct.append(word)
                idx = max([i for i,w in enumerate(convo) if w == word])
                if idx > already_seen_word_pos:
                    already_seen_word_pos = idx
        if matching > max_match:
            max_match = matching
            nearest_match = convo
            pos = already_seen_word_pos
    if pos != -1:
        for i in range(pos+1, len(nearest_match)):
            currentConversation.append(nearest_match[i])
    return currentConversation