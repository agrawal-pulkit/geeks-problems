from abc import ABC, abstractmethod

class Tree(ABC):

    class Positon:

        @abstractmethod
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        @abstractmethod
        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        @abstractmethod
        def __ne__(self, other):
            raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    @abstractmethod
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _length
