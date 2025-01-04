/**
 * Promise 的执行原理
 * Promise 的构造函数（new Promise）中的代码是同步执行的。
 * Promise.then、Promise.catch 或 Promise.finally 的回调函数会被推入微任务队列。
 */

enum S {
  PENDING = 'pending',
  FULFILLED = 'fulfilled',
  REJECTED = 'rejected',
}

// 将回调函数添加到微任务队列
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

  /**
   * @param func 用户输入的回调函数，带有resolve和reject两个参数，用于定义如何解决当前Promise。
   */
  constructor(func: (resolve: any, reject: any) => void) {

    // resolve 和 reject 函数同步的更新Promise的状态
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

    // 确保 onFulfilled, onRejected 的类型正确
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : val => val;
    onRejected =
      typeof onRejected === 'function'
        ? onRejected
        : val => {
            throw val;
          };

    const newPromise = new MyPromise((resolve, reject) => {

      /**
       * 将 onSettled 添加到微任务队列中等待执行。
       * 根据 onFulfilled 或 onRejected 的返回值 resolve then()返回的Promise。
       * @param onSettled onFulfilled 或 onRejected
       */
      const resolveNewPromise = (onSettled: (value: any) => any) => {
        asyncRun(() => {
          try {
            const res = onSettled(this.value);

            if (res === newPromise) {
              throw new TypeError('Chaining cycle detected');
            }
            
            // 从返回的 Promise 中提取值，并使用该值来解决新的 Promise。
            // 等同于 res.then(val => resolve(val), reason => reject(reason));
            if (res instanceof MyPromise) {
              res.then(resolve, reject);
              return;
            }

            resolve(res);

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

        // executor 中的 resolve(x) / reject(x) 尚未被执行,
        // 将 onFulfilled 和 onRejected 添加到队列中等待执行。

        // example:
        // new Promise((resovle, reject) => {
        //   setTimeout(() => {
        //     resolve(666);
        //   }, 1000);
        // })

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