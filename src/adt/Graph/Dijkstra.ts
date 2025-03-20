// Graph representation using adjacency list
interface Graph {
  [vertex: string]: { [neighbor: string]: number };
}

/**
 * Dijkstra's algorithm for finding shortest paths in a weighted graph
 * @param graph - The graph represented as an adjacency list
 * @param startVertex - The starting vertex
 * @returns An object containing distances and the previous vertices on the shortest path
 */
export function dijkstra(graph: Graph, startVertex: string): { 
  distances: { [vertex: string]: number }, 
  previous: { [vertex: string]: string | null } 
} {
  // Initialize distances with Infinity for all vertices except the start
  const distances: { [vertex: string]: number } = {};
  // Track previous vertices for path reconstruction
  const previous: { [vertex: string]: string | null } = {};
  // Set of unvisited vertices
  const unvisited: Set<string> = new Set();

  // Initialize all vertices
  for (const vertex in graph) {
    distances[vertex] = vertex === startVertex ? 0 : Infinity;
    previous[vertex] = null;
    unvisited.add(vertex);
  }

  // Process vertices while unvisited set is not empty
  while (unvisited.size > 0) {
    // Find the unvisited vertex with minimum distance
    let current: string | null = null;
    let minDistance = Infinity;

    for (const vertex of unvisited) {
      if (distances[vertex] < minDistance) {
        minDistance = distances[vertex];
        current = vertex;
      }
    }

    // If no reachable vertices left, break
    if (current === null || distances[current] === Infinity) {
      break;
    }

    // Remove current vertex from unvisited set
    unvisited.delete(current);

    // Update distances to neighbors
    for (const neighbor in graph[current]) {
      if (unvisited.has(neighbor)) {
        // Calculate potential new distance
        const distance = distances[current] + graph[current][neighbor];
        
        // Update if new distance is shorter
        if (distance < distances[neighbor]) {
          distances[neighbor] = distance;
          previous[neighbor] = current;
        }
      }
    }
  }

  return { distances, previous };
}

/**
 * Helper function to reconstruct the shortest path
 * @param previous - Previous vertices on the shortest path
 * @param endVertex - The destination vertex
 * @returns Array representing the path from start to end
 */
export function getShortestPath(previous: { [vertex: string]: string | null }, endVertex: string): string[] {
  const path: string[] = [];
  let current: string | null = endVertex;
  
  // Build path backwards from end to start
  while (current !== null) {
    path.unshift(current);
    current = previous[current];
  }
  
  return path;
}

// Example usage:
/*
const graph: Graph = {
  'A': { 'B': 4, 'C': 2 },
  'B': { 'A': 4, 'C': 1, 'D': 5 },
  'C': { 'A': 2, 'B': 1, 'D': 8 },
  'D': { 'B': 5, 'C': 8 }
};

const startVertex = 'A';
const { distances, previous } = dijkstra(graph, startVertex);

console.log("Distances from vertex", startVertex);
console.log(distances);

console.log("Shortest path from A to D:");
console.log(getShortestPath(previous, 'D'));
*/
