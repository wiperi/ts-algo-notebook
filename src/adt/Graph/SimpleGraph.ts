/**
 * A simple undirected graph implementation using adjacency lists
 */
export class SimpleGraph<T = number> {
  private adjList: Map<T, Set<T>>;
  private numEdges: number;

  /**
   * Initializes an empty graph
   */
  constructor() {
    this.adjList = new Map<T, Set<T>>();
    this.numEdges = 0;
  }

  /**
   * Returns the number of vertices in the graph
   */
  public numVertex(): number {
    return this.adjList.size;
  }

  /**
   * Returns the number of edges in the graph
   */
  public numEdge(): number {
    return this.numEdges;
  }

  /**
   * Adds a vertex to the graph if it doesn't already exist
   * @param v The vertex to add
   */
  public addVertex(v: T): void {
    if (!this.adjList.has(v)) {
      this.adjList.set(v, new Set<T>());
    }
  }

  /**
   * Adds an edge between vertices v and w
   * @param v First vertex
   * @param w Second vertex
   * @throws Error if either vertex doesn't exist
   */
  public addEdge(v: T, w: T): void {
    this.validateVertex(v);
    this.validateVertex(w);

    // Add edge in both directions (undirected graph)
    this.adjList.get(v)!.add(w);
    if (v !== w) {
      this.adjList.get(w)!.add(v);
    }
    this.numEdges++;
  }

  /**
   * Returns all adjacent vertices to vertex v
   * @param v The vertex to get neighbors for
   * @returns An array of adjacent vertices
   * @throws Error if the vertex doesn't exist
   */
  public neighbours(v: T): T[] {
    this.validateVertex(v);
    return Array.from(this.adjList.get(v)!);
  }

  /**
   * Returns the degree of a vertex (number of connected edges)
   * @param v The vertex to check
   * @returns The degree of the vertex
   * @throws Error if the vertex doesn't exist
   */
  public degree(v: T): number {
    this.validateVertex(v);
    return this.adjList.get(v)!.size;
  }

  /**
   * Returns the maximum degree of any vertex in the graph
   */
  public maxDegree(): number {
    let max = 0;
    for (const v of this.adjList.keys()) {
      const degree = this.degree(v);
      if (degree > max) {
        max = degree;
      }
    }
    return max;
  }

  /**
   * Returns the average degree of all vertices in the graph
   */
  public averageDegree(): number {
    return (2.0 * this.numEdges) / this.numVertex();
  }

  /**
   * Returns the number of self-loops in the graph
   */
  public numberOfSelfLoops(): number {
    let count = 0;
    for (const v of this.adjList.keys()) {
      if (this.adjList.get(v)!.has(v)) {
        count++;
      }
    }
    return count;
  }

  /**
   * Returns a string representation of the graph
   */
  public toString(): string {
    let s = '';
    for (const [vertex, neighbors] of this.adjList.entries()) {
      s += `${String(vertex)}: ${Array.from(neighbors).map(String).join(', ')}\n`;
    }
    return s;
  }

  /**
   * Validates that a vertex exists in the graph
   * @param v The vertex to validate
   * @throws Error if the vertex doesn't exist
   */
  private validateVertex(v: T): void {
    if (!this.adjList.has(v)) {
      throw new Error(`Vertex ${String(v)} is not in the graph`);
    }
  }

  /**
   * Creates a graph from a string representation
   * Format: "numVertices / v1 v2 v3 ... / v4 v5 v6 ..."
   * @param s The string representation
   * @returns A new graph
   */
  public static fromString(s: string): SimpleGraph<string> {
    const graph = new SimpleGraph<string>();
    const parts = s.split('/');

    // First part contains number of vertices
    const numVertices = parseInt(parts[0].trim(), 10);
    if (numVertices <= 0) {
      throw new Error('Number of vertices should be greater than 0');
    }

    // Process each part after the first
    for (let i = 1; i < parts.length; i++) {
      const vertices = parts[i]
        .trim()
        .split(/\s+/)
        .map(v => v.trim());
      if (vertices.length <= 1) {
        throw new Error('Each part should have at least 2 vertices');
      }

      const sourceVertex = vertices[0];
      graph.addVertex(sourceVertex);

      for (let j = 1; j < vertices.length; j++) {
        const targetVertex = vertices[j];
        graph.addVertex(targetVertex);
        graph.addEdge(sourceVertex, targetVertex);
      }
    }

    return graph;
  }
}

if (require.main === module) {
  // Test the SimpleGraph implementation
  const g = new SimpleGraph<string>();
  console.log('Empty graph:', g);

  // Add some vertices
  for (let i = 0; i < 10; i++) {
    g.addVertex(i.toString());
  }
  console.log('Graph with vertices:', g);

  // Add some edges
  g.addEdge('0', '1');
  g.addEdge('0', '2');
  g.addEdge('1', '3');
  g.addEdge('2', '4');
  g.addEdge('3', '3'); // self-loop

  console.log('Graph with edges:', g);

  // Count self-loops
  const selfLoops = countSelfLoops(g);
  console.log('Number of self-loops:', selfLoops);

  // Helper function to count self-loops in a graph
  function countSelfLoops(graph: SimpleGraph<string>): number {
    let count = 0;
    for (let i = 0; i < 10; i++) {
      const vertex = i.toString();
      const neighbors = graph.neighbours(vertex);
      if (neighbors.includes(vertex)) {
        count++;
      }
    }
    return count;
  }

  // Test the fromString method
  const graphFromString = SimpleGraph.fromString('5 / 0 1 2 / 1 3 / 2 4 / 3 3');
  console.log('Graph from string:', graphFromString);
  
  // Example with different vertex types
  const objectGraph = new SimpleGraph<{id: number}>();
  const v1 = {id: 1};
  const v2 = {id: 2};
  const v3 = {id: 3};
  
  objectGraph.addVertex(v1);
  objectGraph.addVertex(v2);
  objectGraph.addVertex(v3);
  
  objectGraph.addEdge(v1, v2);
  objectGraph.addEdge(v2, v3);
  
  console.log('Object graph neighbors of v1:', objectGraph.neighbours(v1));
}
