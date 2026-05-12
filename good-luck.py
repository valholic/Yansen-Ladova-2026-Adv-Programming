t = int(input())
for i in range(1, t + 1):
    webpages = []
    max_relevance = -1
    
    for _ in range(10):
        url, relevance = input().split()
        relevance = int(relevance)
        
        webpages.append((url, relevance))
        if relevance > max_relevance:
            max_relevance = relevance
    
    print(f"Case #{i}:")
    
    for url, relevance in webpages:
        if relevance == max_relevance:
            print(url)