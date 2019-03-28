class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        1st approach: union find

        consider

        case 1, all in the same set:
        a/b=2, b/c=3
        we can compute any combinations of the a,b,c 

        case 2, different sets:
        a/b=2, c/d=3
        we can compute any combinations of the a,b and any combinations of the c/d

        case 3, they are in different sets initially, but they combine afterwards
        a/b=2, c/d=3, a/c=4
        first compute a,b, compute c,d
        then for the symbols in set(a,b), mutiply them to a correct scale as set(c,d)

        Time    O(E*N*logN) E: equations, N: nodes
        Space   O(2N) nodes in union find
        20 ms, faster than 70.51%
        """
        # init unionfind
        nodeSet = set()
        for i in range(len(equations)):
            a, b = equations[i]
            nodeSet.add(a)
            nodeSet.add(b)
        nodes = list(nodeSet)
        uf = UnionFind(nodes)
        # equations
        ht = {}
        for i in range(len(equations)):
            a, b = equations[i]

            # if they are seen and they are not in the same set
            # multiply all the values in A and values[i] so that set A and set B will be with a same ratio
            rootA = uf.find(a)
            rootB = uf.find(b)
            if a in ht and b in ht and rootA != rootB:
                for node in nodes:
                    if uf.find(node) == rootA:
                        ht[node] *= values[i]*ht[b]
            else:
                if a not in ht and b not in ht:
                    ht[a] = values[i]
                    ht[b] = 1.0
                elif a not in ht:
                    ht[a] = values[i] * ht[b]
                elif b not in ht:
                    ht[b] = ht[a] / values[i]
            uf.union(a, b)
        # compute result
        res = []
        for q in queries:
            a, b = q
            rootA = uf.find(a)
            rootB = uf.find(b)
            if rootA == rootB and rootA != None:
                res.append(ht[a]/ht[b])
            else:
                res.append(-1.0)
        return res


class UnionFind(object):
    def __init__(self, vertices):
        self.count = len(vertices)
        self.ids = {}
        self.caps = {}
        for vertex in vertices:
            self.ids[vertex] = vertex
            self.caps[vertex] = 1

    def find(self, key):
        # loop to find to ultimate root
        if key not in self.ids:
            return None
        cur = key
        while cur != self.ids[cur]:
            cur = self.ids[cur]
        return cur

    def union(self, p, q):
        if p not in self.ids or q not in self.ids:
            return

        pId = self.find(p)
        qId = self.find(q)
        if pId == qId:
            return
        # attach to the larger tree
        if self.caps[pId] < self.caps[qId]:
            self.ids[pId] = qId
            self.caps[qId] += self.caps[pId]
        else:
            self.ids[qId] = pId
            self.caps[pId] += self.caps[qId]
        self.count -= 1


# normal
a = [["a", "b"], ["b", "c"]]
b = [2.0, 3.0]
c = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(Solution().calcEquation(a, b, c))

# very important test case: combine sets after we saved
a = [["a", "b"], ["e", "f"], ["b", "e"]]
b = [3.4, 1.4, 2.3]
c = [["b", "a"], ["a", "f"], ["f", "f"], [
    "e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
print(Solution().calcEquation(a, b, c))
