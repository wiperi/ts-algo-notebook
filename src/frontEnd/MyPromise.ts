enum S {
  PENDING = 'pending',
  FULFILLED = 'fulfilled',
  REJECTED = 'rejected',
}

function asyncRun(func: () => void) {
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

    try {
      func(resolve, reject);
    } catch (error) {
      reject(error);
    }
  }

  then(onFulfilled?: (value: any) => any, onRejected?: (reason: any) => any) {
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : val => val;
    onRejected =
      typeof onRejected === 'function'
        ? onRejected
        : val => {
            throw val;
          };

    const newPromise = new MyPromise((resolve, reject) => {
      /**
       * Resolve new promise based on the return value of onFulfilled or onRejected
       * @param onSettled onFulfilled or onRejected
       */
      const resolveNewPromise = (onSettled: (value: any) => any) => {
        asyncRun(() => {
          try {
            const res = onSettled(this.value);

            if (res === newPromise) {
              throw new TypeError('Chaining cycle detected');
            } else if (res instanceof MyPromise) {
              // Extract value from the returned Promise and use it to resolve the new Promise.
              // res.then(onFulfilled = resolve, onRejected = reject)
              res.then(resolve, reject);
            } else {
              resolve(res);
            }
          } catch (error) {
            reject(error);
          }
        });
      };

      if (this.state === S.FULFILLED) {
        resolveNewPromise(onFulfilled);
      } else if (this.state === S.REJECTED) {
        resolveNewPromise(onRejected);
      } else if (this.state === S.PENDING) {
        this.callbacks.push({
          onFulfilled: () => resolveNewPromise(onFulfilled),
          onRejected: () => resolveNewPromise(onRejected),
        });
      }
    });

    return newPromise;
  }

  catch(onRejected: (reason: any) => any) {
    return this.then(undefined, onRejected);
  }

  finally(onFinally: () => any) {
    return this.then(onFinally, onFinally);
  }

  static resolve(value: any) {
    if (value instanceof MyPromise) {
      return value;
    }

    return new MyPromise((resolve, reject) => {
      resolve(value);
    });
  }

  static reject(reason: any) {
    return new MyPromise((resolve, reject) => {
      reject(reason);
    });
  }

  static race(promises: unknown[]) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        return reject(new TypeError(`${promises} is not iterable`));
      }

      promises.forEach(p => MyPromise.resolve(p).then(resolve, reject));
    });
  }

  /**
   * Return a promise that is resolved when all of the given promises are resolved.
   * - If any of the promises is rejected, the returned promise is rejected. Reason is the same as the first rejected promise.
   * - If all of the promises are fulfilled, the returned promise is fulfilled with its value being an array of the results of the input promises.
   * - If given an empty array, resolve immediately.
   * @param promises - An array of promises.
   * @returns A promise that resolves to an array of the results of the input promises.
   */
  static all(promises: unknown[]) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        return reject(new TypeError(`${promises} is not iterable`));
      }

      promises.length === 0 && resolve(promises);

      const results: any[] = [];
      let count = 0;

      promises.forEach((p, index) =>
        MyPromise.resolve(p).then(res => {
          results[index] = res;
          count++;
          if (count === promises.length) resolve(results);
        }, reject)
      );
    });
  }

  static allSettled(promises: unknown[]) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        return reject(new TypeError(`${promises} is not iterable`));
      }

      promises.length === 0 && resolve(promises);

      const results: any[] = [];
      let count = 0;

      promises.forEach((p, index) =>
        MyPromise.resolve(p).then(
          val => {
            results[index] = {
              status: S.FULFILLED,
              value: val,
            };
            count++;
            if (count === promises.length) resolve(results);
          },
          err => {
            results[index] = {
              status: S.REJECTED,
              reason: err,
            };
            count++;
            if (count === promises.length) resolve(results);
          }
        )
      );
    });
  }

  static any(promises: unknown[]) {
    return new MyPromise((resolve, reject) => {
      if (!Array.isArray(promises)) {
        return reject(new TypeError(`${promises} is not iterable`));
      }

      if (promises.length === 0) reject(new AggregateError('All promises were rejected'));

      const reasons: any[] = [];
      let count = 0;

      promises.forEach((p, index) =>
        MyPromise.resolve(p).then(resolve, err => {
          reasons[index] = err;
          count++;
          if (count === promises.length) reject(new AggregateError(reasons));
        })
      );
    });
  }
}

module.exports = {
  deferred() {
    const res = {} as any;
    res.promise = new MyPromise((resolve, reject) => {
      res.resolve = resolve;
      res.reject = reject;
    });
    return res;
  }
}