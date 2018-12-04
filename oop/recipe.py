# prepared
# recipe
# cleanup

from abc import ABC, abstractmethod


class AbstractRecipe(ABC):

    def execute(self):
        self.prepared()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepared(self): pass

    @abstractmethod
    def recipe(self): pass

    @abstractmethod
    def cleanup(self): pass


class RecipeImplement(AbstractRecipe):

    def prepared(self):
        print('do the dishes')
        print('get raw materials')
        pass

    def recipe(self):
        print('execute recipe')
        pass

    def cleanup(self):
        print('clean')
        pass


recipe = RecipeImplement()
recipe.execute()