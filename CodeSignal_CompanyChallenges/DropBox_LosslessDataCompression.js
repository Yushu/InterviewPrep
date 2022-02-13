function losslessDataCompression(str, width) {
  var res = ""
  for (let i = 0; i < str.length; ++i) {
    let m = 0, s = 0
    for (let j = Math.max(i - width, 0); j + m < i; ++j) {
      let k = 0
      while (j + k < i && str[j + k] === str[i + k])
        ++k
        if (k > m) {
          m = k
          s = j
          }
      }
      m > 0 ? (res += `(${s},${m})`, i += m - 1) : res += str[i]
    }
    return res
}

console.log(losslessDataCompression("aaaaaaaaaaaaaaaaaaaaaaaaaaaa",12))
//Expected o/p: "a(0,1)(0,2)(0,4)(0,8)(4,12)"

console.log(losslessDataCompression("abacabadabacaba",7))
//Expected o/p: "ab(0,1)c(0,3)d(4,3)c(8,3)"