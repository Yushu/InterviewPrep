function estimatedTimeDuration(parent, n, t, selectedEdge, relatedNode) {
    let eta = 0, times = []
    
    relatedNode = relatedNode.slice()
    relatedNode.push(parent)
    
    if(selectedEdge[parent]) {
        selectedEdge[parent].forEach(function(i) {
            if(relatedNode.indexOf(i) < 0) {
                times.push(estimatedTimeDuration(i, n, t, selectedEdge, relatedNode))
            }
        })
    }
    
    if(times.length > 0) {
        eta = times.reduce(function(acc, val) {
            return acc + val
        }) / times.length
    }
    eta += t[parent]
    return eta
}

function solution(n, t, edges) {
    let minReadingPath = Number.MAX_VALUE,
        questionNum = -1,
        length = t.length,
        temp,
        selectedEdge = {}
    
    edges.forEach(function(edge) {
        selectedEdge[edge[0]] = selectedEdge[edge[0]] || []
        selectedEdge[edge[0]].push(edge[1])

        selectedEdge[edge[1]] = selectedEdge[edge[1]] || []
        selectedEdge[edge[1]].push(edge[0])
    })
    
    for(var i = 0; i<length; ++i) {
        temp = estimatedTimeDuration(i, n, t, selectedEdge, [])
        if(temp < minReadingPath) {
            minReadingPath = temp
            questionNum = i
        }
    }
    return questionNum
}