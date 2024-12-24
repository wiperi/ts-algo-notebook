# 回溯算法

## 代码框架

```py
def 回溯(...):
    
    if 终止条件:
        记录结果
        return
        
    for 选择 in 选择列表
        剪枝

        做选择
        回溯(...) # 开始下一次选择
        撤销选择
```


解决实际问题中的模板运用


```py
def 问题():
    
    状态

    return

    def 回溯(状态): # 函数参数和全局变量都可以记录状态
        
        if 终止条件:
            记录结果
            return
            
        for 选择 in 选择列表
            剪枝

            更新状态
            回溯(新的状态) # 进入递归树的下一层
            回退状态

```

## 对比dfs，动态规划

回溯算法和dfs的本质思想相同，都是采用递归的方式暴力穷举，对解空间进行深度优先遍历。区别在于关注点不同，回溯算法的关注点在「树枝」，DFS 算法的关注点在「节点」。

回溯/dfs和动态规划的本质都是穷举，只不过动态规划存在「重叠子问题」可以优化，而回溯算法不存在而已

### 外层，内层区域的区别

 - 回溯：关注遍历树枝（选择），在进入下一层的非法节点之前 or 做出错误选择之前 剪枝

 - dfs：关注遍历节点，在进入下一层的非法节点之后 or 做出错误选择之后 触发base case回退

```py
def backtrack(root):

    # 外层区域：前序
    print(f"我在 ${root} 节点上做选择")

    for c in choices:

        #  内层区域：前序
        print(f"我在 ${root} 和 ${child} 中间的树枝上做选择")
        
        backtrack(root)

        #  内层区域：后序
        print(f"我在 ${root} 和 ${child} 中间的树枝上撤销选择")

    #  外层区域：后序
    print(f"我在 ${root} 节点上撤销选择")
```

外层区域和内层区域的轨迹区别

```ts
import { __Node, MultiTree } from "@/tree/MultiTree";

const adjMap = new Map<number, number[]>();
adjMap.set(0, [1, 2, 3, 10, 11]);
adjMap.set(1, [4, 5]);
adjMap.set(2, [6, 7]);
adjMap.set(3, [8, 9, 12, 13]);
const tree = new MultiTree(adjMap);

console.log(tree);

let outerPre = '';
let outerPost = '';
let innverPre = '';
let innverPost = '';

function dfs(root: __Node) {

  outerPre += root.val + ' ';

  if (!root.children) root.children = [];

  for (let ch of root.children) {
    innverPre += ch.val + ' ';
    dfs(ch);
    innverPost += ch.val + ' ';
  }
  outerPost += root.val + ' ';
}


dfs(tree.root);

console.log('outerPre\t', outerPre);
console.log('innverPre\t', innverPre);
console.log('outerPost\t', outerPost);
console.log('innverPost\t', innverPost);
```

输出

```bash
> ts-node -r tsconfig-paths/register .\tt.ts

└─ 0
   ├─ 1
   │  ├─ 4
   │  └─ 5
   ├─ 2
   │  ├─ 6
   │  └─ 7
   ├─ 3
   │  ├─ 8
   │  ├─ 9
   │  ├─ 12
   │  └─ 13
   ├─ 10
   └─ 11
outerPre         0 1 4 5 2 6 7 3 8 9 12 13 10 11
innverPre        1 4 5 2 6 7 3 8 9 12 13 10 11
outerPost        4 5 1 6 7 2 8 9 12 13 3 10 11 0
innverPost       4 5 1 6 7 2 8 9 12 13 3 10 11
```
