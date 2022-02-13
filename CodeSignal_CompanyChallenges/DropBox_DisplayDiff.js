function displayDiff(oldVersion, newVersion) {
  dp = []
  f = (f1, f2) => {
    var i = 0, j, diff = "",temp, ret
    if (!dp[f1 + " " + f2]) {
      while (f1[i] && f1[i] === f2[i]) {
        diff += f1[i]
        i++
      }
      ret = []
      for (j = i; j++ < f1.length; ) {
        temp = f(f1.slice(j), f2.slice(i))
        ret.push([diff + '\200' + f1.slice(i, j) + '\201' + temp[0], diff + f1.slice(i, j) + temp[1]])
      }
      for (j = i; j++ < f2.length; ) {
        temp = f(f1.slice(i), f2.slice(j))
        ret.push([diff + '\202' + f2.slice(i, j) + '\203' + temp[0], diff + f2.slice(i, j) + temp[1]])
      }

      ret.sort(
        (a, b) => a[1].length < b[1].length ? -1 : a[1].length > b[1].length ? 1 : a[0] < b[0] ? -1 : a[0] > b[0]
      )
      dp[f1 + " " + f2] = ret[0] ? ret[0] : [diff, diff]
    }
    return dp[f1 + " " + f2]
  }
  return f(oldVersion, newVersion)[0].replace(/\200/g, "(").replace(/\201/g, ")").replace(/\202/g, "[").replace(/\203/g, "]")
}

console.log(displayDiff("same_prefix_1233_same_suffix", "same_prefix23123_same_suffix"))
//Expected o/p: "same_prefix(_1)23[12]3_same_suffix"

console.log(displayDiff("ab", "ab"))

console.log(displayDiff("Codesignal", "ab"))

console.log(displayDiff("dasdf", "asdfd"))