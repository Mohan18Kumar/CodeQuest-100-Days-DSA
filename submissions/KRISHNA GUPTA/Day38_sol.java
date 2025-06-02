import java.util.*;
public class Day38_sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<String, List<String>> graph = new HashMap<>();

        System.out.println("Input: Graphm");
        while (true) {
            String line = sc.nextLine().trim();
            if (line.isEmpty()) break;  

            String[] parts = line.split(":");
            String node = parts[0].trim();

            List<String> neighbors = new ArrayList<>();
            if (parts.length > 1 && !parts[1].trim().isEmpty()) {
                String[] nbrs = parts[1].trim().split("\\s+");
                for (String n : nbrs) {
                    neighbors.add(n.trim());
                }
            }
            graph.put(node, neighbors);
        }

        System.out.print("Input: Starting node for BFS: ");
        String start = sc.nextLine().trim();

        System.out.println("Output: BFS traversal:");
        bfs(graph, start);

        sc.close();
    }

    static void bfs(Map<String, List<String>> graph, String start) {
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.add(start);
        visited.add(start);
        while (!queue.isEmpty()) {
            String current = queue.poll();
            System.out.print(current + " ");
            List<String> neighbors = graph.getOrDefault(current, new ArrayList<>());
            for (String nbr : neighbors) {
                if (!visited.contains(nbr)) {
                    visited.add(nbr);
                    queue.add(nbr);
                }
            }
        }
    }
}
