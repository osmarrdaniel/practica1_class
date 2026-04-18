class Tenis:
    def __init__(self, marca, modelo, precio, descuento, talla):
        self.__marca = marca
        self.__modelo = modelo 
        self.__precio = precio 
        self.__descuento = descuento 
        self.__talla = talla 
        self.__preciofinal = 0
        
    def get_marca(self): 
        return self.__marca 
    def set_marca(self, marca):
        self.__marca = marca
    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo 
    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio 
            