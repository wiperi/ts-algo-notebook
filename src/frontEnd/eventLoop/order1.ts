const first = () =>
  new Promise((resovle, reject) => {

    console.log(1);
    const p = new Promise((resovle, reject) => {

      console.log(2);
      setTimeout(() => {

        console.log(3);
        resovle(4);
      }, 0);

      resovle(5);
    });

    resovle(6);

    p.then(arg => {
      console.log(arg);
    });
  });

first().then(arg => {
  console.log(arg);
});

console.log(7);

// 1
// 2
// macro: 3
// macro: p.r(4)
// p.r(5)
// fist.r(6)
// micro: p.then(5)
// micro: first.then(6)
// 7

// 1 2 7 5 6 3
