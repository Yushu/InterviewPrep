function salesLeadsScore(names, time, netValues, isOnVacation) {

  return names.map((name,i) => [name, time[i], netValues[i], isOnVacation[i]]).filter(e => !e[3]).sort(([n1, t1, v1], [n2, t2, v2]) => (t2 * v2 - t1 * v1) || t2 - t1 || (n1 < n2 ? -1 : n1 > n2 ? 1: 0)).map(e => e[0]);
}

const names = ["lead1", "lead2", "lead3", "lead4", "lead5"];
const time = [250, 300, 250, 260, 310];
const netValues = [1000, 800, 1100, 1200, 1000];
const isOnVacation = [true, false, true, false, false];

console.log(salesLeadsScore(names, time, netValues, isOnVacation));