class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        # Obtiene el carrito de la sesión, si no existe, inicializa uno vacío
        carro = self.session.get('carro', {})
        if not carro:
            carro = self.session['carro']={}
        self.carro = carro
    
    def agregar(self, producto):
        # Si el producto no está en el carrito, lo agrega con cantidad 1
        producto.id = str(producto.id)
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre_disco,  # Utiliza nombre_disco en lugar de nombre
                'precio': str(producto.precio),
                'cantidad': 1,
                'imagen': producto.imagen_tapa.url if producto.imagen_tapa else ''
            }
            # Si el producto ya está en el carrito, incrementa la cantidad en 1
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"] +1
                    break
        
        self.guardar_carro()
   
       
    def guardar_carro(self):
        # Guarda el carro en la sesión y marca la sesión como modificada
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def eliminar(self, producto):
        # Elimina el producto del carrito si está presente
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        # Resta la cantidad de un producto en el carrito
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"] -1
                if value["cantidad"] <1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
    
    def limpiar_carro(self):
        # Vacía el carrito
        self.session['carro'] = {}
        self.session.modified = True

    def obtener_total(self):
        total = 0
        for item in self.carro.values():
            precio_producto = float(item['precio'])
            cantidad_producto = item['cantidad']
            total += precio_producto * cantidad_producto
        return total