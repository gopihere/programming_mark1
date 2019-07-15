function findFactorialRecursive(number) {
  if(number==2){
    return 2;
  }
  return number * findFactorialRecursive(number-1);
}

function findFactorialIterative(number) {
  let m=1;
  for(let i=2;i<=number;i++){
    m=m * i;
  }
  return m;
}

findFactorialRecursive(5)
findFactorialIterative(5) 
