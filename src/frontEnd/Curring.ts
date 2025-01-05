let count = 0;

function sumMaker(length: number) {
  let nums: number[] = [];

  const sum = (...args: number[]): any => {
    nums.push(...args);
    if (nums.length >= length) {
      const res = nums.slice(0, length).reduce((p, c) => p + c, 0);
      nums = [];
      return res;
    } else {
      return sum;
    }
  };

  return sum;
}

function typeCheckerGenerator(type: string) {
  return (val: any) => {
    return typeof val === type;
  };
}

if (require.main === module) {
  const sum = sumMaker(3);

  console.log(sum(2)(2));

  const numCheck = typeCheckerGenerator('number');
  console.log(numCheck('hello'));
}

export {}