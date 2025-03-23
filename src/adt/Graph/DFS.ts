import { UndirectedGraph } from 'data-structure-typed';

// Create a new undirected graph
const g = new UndirectedGraph<string, number>();

// Add vertices
g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');

// Add edges with weights
g.addEdge('A', 'B', 1);
g.addEdge('A', 'C', 2);
g.addEdge('B', 'D', 3);
g.addEdge('C', 'D', 4);
g.addEdge('C', 'E', 5);
g.addEdge('D', 'E', 6);


// Example of DFS traversal
function dfs(graph: UndirectedGraph<string, number>, startVertex: string): string[] {
  const visited: Set<string> = new Set();
  const result: string[] = [];
  
  function traverse(vertex: string) {
    visited.add(vertex);
    result.push(vertex);

    const neighbors = graph.getNeighbors(vertex);
    for (const neighbor of neighbors) {
      const neighborVertex = neighbor.key;
      if (!visited.has(neighborVertex)) {
        traverse(neighborVertex);
      }
    }
  }
  
  traverse(startVertex);
  return result;
}

// Run DFS starting from vertex 'A'
const dfsResult = dfs(g, 'A');
console.log('DFS traversal:', dfsResult);