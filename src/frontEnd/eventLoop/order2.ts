async function async1() {

  // 2
  console.log('async1');
  
  // code under await is == .then(...)
  await async2();

  // micro 1 （async2() = Promise{undefined})
  console.log('async1 end');
}

async function async2() {
  // 3
  console.log('async2');
}

// 1
console.log('script start');

setTimeout(() => {
  // macro 1
  console.log('setTimeOut');
}, 0);

async1();

new Promise(resolve => {

  // 4
  console.log('promise');

  resolve(undefined);
}).then(() => {

  // micro 2
  console.log('promise2');
});

// 5
console.log('script end');  
export {}