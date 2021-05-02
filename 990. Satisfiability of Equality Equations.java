class Solution {
    public boolean equationsPossible(String[] equations) {
      // 26 letters
    UF uf = new UF(26);
    // Let equal letters form connected components first
    for (String eq : equations) {
        if (eq.charAt(1) == '=') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            uf.union(x - 'a', y - 'a');
        }
    }
    // Check if inequality relationship breaks connectivity of equal relationship
    for (String eq : equations) {
        if (eq.charAt(1) == '!') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            // If the equality relationship holds, it is a logical conflict
            if (uf.connected(x - 'a', y - 'a'))
                return false;
        }
    }
    return true;
}
class UF {
    // Record the number of connected components
    private int count;
    // Store several trees
    private int[] parent;
    // Record the "weight" of the tree
    private int[] size;

    public UF(int n) {
        this.count = n;
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }
    
    /* Connect p and q */
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ)
            return;
        
        // The small tree is more balanced under the big tree
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        count--;
    }

    /* Determine whether p and q are connected to each other */
    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        // Nodes on the same tree are interconnected
        return rootP == rootQ;
    }

    /* Returns the root node of node x */
    private int find(int x) {
        while (parent[x] != x) {
            // Path compression
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    
    public int count() {
        return count;
    }
}
}