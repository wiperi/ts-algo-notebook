enum S {
  PENDING = 'pending',
  FULFILLED = 'fulfilled',
  REJECTED = 'rejected',
}

function runAsync(func: any) {
  if (typeof queueMicrotask === 'function') {
    return queueMicrotask(func);
  } else {
    return setTimeout(func, 0);
  }
}

class MyPromise {
  state: S = S.PENDING;
  value: any;

  private callbacks: {
    onFulfilled: (value: any) => void;
    onRejected: (reason: any) => void;
  }[] = [];

  constructor(func: (resolve: any, reject: any) => void) {
    const resolve = (value: any) => {
      if (this.state === S.PENDING) {
        this.state = S.FULFILLED;
        this.value = value;

        this.callbacks.forEach(({ onFulfilled }) => {
          onFulfilled(value);
        });
      }
    };

    const reject = (reason: any) => {
      if (this.state === S.PENDING) {
        this.state = S.REJECTED;
        this.value = reason;
        this.callbacks.forEach(({ onRejected }) => {
          onRejected(reason);
        });
      }
    };
    func(resolve, reject);
  }

  then(onFulfilled?: (value: any) => any, onRejected?: (reason: any) => any) {
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : val => val;
    onRejected = typeof onRejected === 'function' ? onRejected : val => { throw val };

    let res;
    const newPromise = new MyPromise((resolve, reject) => {
      if (this.state === S.FULFILLED) {
        runAsync(() => {
          try {
            res = onFulfilled(this.value);
            console.log('res', res);
            console.log('newPromise', newPromise);
            if (res === newPromise) {
              console.error('Chaining cycle detected');
              throw new TypeError('Chaining cycle detected');
            }
            // if res is a MyPromise, then get the value of the MyPromise
            if (res instanceof MyPromise) {
              res.then(resolve, reject);
            } else {
              resolve(res);
            }
          } catch (error) {
            reject(error);
          }
        });
      } else if (this.state === S.REJECTED) {
        runAsync(() => {
          try {
            res = onRejected(this.value);
            if (res instanceof MyPromise) {
              res.then(resolve, reject);
            } else {
              reject(res);
            }
          } catch (error) {
            reject(error);
          }
        });
      } else if (this.state === S.PENDING) {
        this.callbacks.push({ onFulfilled, onRejected });
      }
    });

    return newPromise;
  }

  catch(onRejected: (reason: any) => void) {
    if (this.state === S.REJECTED && onRejected) {
      onRejected(this.value);
    }
  }

  finally(onFinally: () => void) {}
}

// test
const p = new MyPromise((resolve, reject) => {
  resolve('hello');
});
const p2 = p.then(val => {
  console.log('p1val', val);
  // throw 'error';
  return p2;
})

p2.then(
  val => {
    console.log('p2val',val);
  },
  err => {
    console.log('p2err', err);
  }
);
