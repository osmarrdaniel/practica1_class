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
    def get_descuento(self):
        return self.__descuento
    def set_descuento(self, descuento):
        self.__descuento = descuento 
    def get_talla(self):
        return self.__talla
    def set_talla(self, talla):
        self.__talla = talla
        
    def calcular_precio_final(self):
        descuento = self.__precio * self.__descuento
        self.__preciofinal = self.__precio - descuento
        return self.__preciofinal
            
    def calcular_ahorro(self):
        ahorro = self.__precio * self.__descuento
        return ahorro
            