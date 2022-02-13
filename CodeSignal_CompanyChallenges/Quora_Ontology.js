ontology = (treeRepr, questions, queries) => {
  var tree = {}, depth = 0, pred = [], res = []

  // build tree
  treeRepr.split(" ").map(word => {
    if (word == '(') {
      depth++
    } else if (word == ')') {
      depth--
    } else {
      tree[word] = [word]
      pred[depth] = word
      for (let i = 0; i < depth; ++i) {
        tree[pred[i]].push(word);
      }
    }
  })

  // reformat questions, split to title and question
  for (var i in questions)
    questions[i] = questions[i].split(": ")

  // Query processing
  for (var i in queries) {
    // split to title and question prefix
    var firstSpace = queries[i].indexOf(" "),
      section    = queries[i].slice(0, firstSpace),
      question   = queries[i].slice(firstSpace + 1),
      match = 0

    if (tree[section]) {
      for (var j in questions) {
        if (tree[section].includes(questions[j][0])) {
          if (question == questions[j][1].slice(0, question.length))
            match++
        }
      }
    }
    res[i] = match
  }
  return res
}

console.log(ontology("Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )",["Reptiles: Why are many reptiles green?","Birds: How do birds fly?","Eagles: How endangered are eagles?","Pigeons: Where in the world are pigeons most densely populated?","Eagles: Where do most eagles live?"], ["Eagles How en","Birds Where","Reptiles Why do","Animals Wh"]))
//[1,2,0,3]
console.log(ontology("A ( B ( C D E ) F ( G ( H I J ) ) )", ["A: ABC?", "B: A?", "C: A B C?", "D: ?", "E: Where is it?", "F: How are you?", "G: You you you?", "H: You are not?", "I: Where do you live?", "J: Where did he live?"], ["A A B C?", "A A", "G You ", "E W", "B W", "B Whe", "A T", "A t", "C C", "C CO", "G W"]))
//[1, 3, 2, 1, 1, 1, 0, 0, 0, 0, 2]
console.log(ontology("A", ["A: WTF?", "A: Oh, really?", "A: Man, how did you do it?", "A: Right?"], ["A W", "A R", "A R", "A W", "A Oh", "A Man"]))
//[1, 1, 1, 1, 1, 1]