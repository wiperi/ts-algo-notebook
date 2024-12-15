let count = 0;

function sumMaker(length: number) {
  let nums:number[] = [];
  
  const sum = (...args: number[]): any => {
    nums.push(...args);
    if (nums.length >= length) {
      const res = nums.slice(0, length).reduce((p, c) => p + c, 0);
      nums = [];
      return res;
    } else {
      return sum;
    }
  }

  return sum;
}

function typeCheckerGenerator(type: string) {
  return (val: any) => {
    return typeof val === type;
  }
}


// test
const sum = sumMaker(3);

console.log(sum(2)(2))

const numCheck = typeCheckerGenerator('number');
console.log(numCheck('234'));


function race(promises: unknown[]) {
  // returned promise will be resolved based on the first resolved given promises
  return new Promise((resolve, reject) => {
    promises.forEach(p => Promise.resolve(p).then(resolve, reject));
  })
}
function all(promises: unknown[]) {
  // fulfieed when all given promises fulfieed, if any rejected, then rejected
  return new Promise((resolve, reject) => {

    const res: any = [];
    let count = 0;
    promises.forEach((p, i) => Promise.resolve(p).then(
      val => {
        res[i] = val;
        count++;
        if (count === promises.length) resolve(res);
      },
      reject
    ))
  })
}

const p1 = new Promise((r, rej) => {
  setTimeout(() => {
    r(99);
  }, 1000);
})
const p2 = new Promise((r, rej) => {
  setTimeout(() => {
    r(99);
  }, 2000);
})
const p3 = new Promise((r, rej) => {
  setTimeout(() => {
    r(99);
  }, 3000);
})
all([p1,p2,p3, 66]).then(
  res => console.log(res),
  err => console.log(err)
)

