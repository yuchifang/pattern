from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. 
    
    The Creator's subclasses usually provide the
    implementation of this method.
    """
    # Creator 的子 class 通常提供 此方法的實現

    @abstractmethod
    def factory_method(self):

        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        # Creator 預寫一些 default 方法
        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products.
        """
        # Creator 的主要責任不是創造產品

        """
        Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        """
        # 它通常包含一些業物邏輯 由工廠方法返回

        """
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """
        # 子類 可以通過重寫 工廠方法並從中返回不同類型的產品

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""
# 重寫 工廠的方法 以更改產品結果類型

class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. 
    """
    
    """
    This way the Creator can stay independent of concrete product classes.
    """
    # Concrete 還是引用 Creator 這樣 Creator 就可以獨力在不同產品中

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    # Product 聲明了所有具體產品的操作 必須實施
    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""
# 提供 Product 接口 的各種實建方法

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

print("some",__name__)
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())