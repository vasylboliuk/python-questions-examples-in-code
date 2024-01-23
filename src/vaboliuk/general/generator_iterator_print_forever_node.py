
class FruitNode:
    """
    Task-1: As a user I would like to see in console forever printed fruit node list.
        Where the input data is a list of [FruitNode("<fruit_name>"), ...].
        Finish the execution once you reach 100 printed fruits in console
    """

    def __init__(self, fruit):
        self.fruit = fruit


class FruitCluster:

    def __init__(self, nodes: list[FruitNode]):
        self.nodes = nodes

    def forever_give_fruit(self):
        while True:
            for item in self.nodes:
                yield item.fruit


class TestIteratorGeneratorForeverExecutionNode:

    def test_forever_fruit_nodes(self):
        cluster = FruitCluster(nodes=[FruitNode('cherry'), FruitNode('mango'), FruitNode('banana')])
        number_of_nodes = 100
        for node in cluster.forever_give_fruit():
            print(node)
            if number_of_nodes == 0:
                break
            number_of_nodes -= 1



