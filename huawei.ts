function problem(k: number, s: string) {

  let i = 0;
  let winLen = 0;
  while (s[i++] !== '-') continue;

  let up = [], lo = []

  while (1) {
    if (i === s.length) break;

    if ('a' <= s[i] && s[i] <= 'Z') {
      if (s[i] <= 'z') {
        lo.push(i);
      } else {
        up.push(i);
      }
    } else if (s[i] === '-') {
      s = s.substring(0, i) + s.substring(i + 1);
    }

    i++;
    winLen++;

    if (winLen === k || i === s.length) {
      s = s.substring(0, i) + '-' + s.substring(i);
      i++;
      console.log(s)
      winLen = 0;
    }
  }

  console.log(s)
}

problem(3, 'aAa-ZAbA-ccc')