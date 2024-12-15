const deb = debounceMaker((val: any) => {
  console.log(this);
}, 2000)

function click(){
  deb('hahha');
}

function debounceMaker(callback: (...args: any) => any, wait: number) {
  let timer: ReturnType<typeof setTimeout>;

  return (...args: any) => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      callback(...args);
    }, wait);
  }
}


// test
click();
click();
click();