

# Modelos simples para el ejemplo

# Subclase que determinar los atributos de una tarea simple
class Task:
    # Constructor de la clase Tarea 
    def __init__(self, nombre, duracion):
        self.nombre = nombre # Atributo del nombre de la tarea
        self.duracion = duracion  # Atributo de la duración estimada en segundos
        self.estado = "PENDIENTE"  # atributo del estado de la tarea
        self.resultado = None # Atributo del resultado de la tarea

# Subclase que determina los atributos de un trabajador que realiza la tarea
class Thread:
    # Constructor de la clase Hilo
    def __init__(self, id_hilo, nombre): 
        self.id_hilo = id_hilo # Atributo del ID del hilo
        self.nombre = nombre # Atributo del nombre del hilo
        self.tareas_completadas = 0 # Atributo del número de tareas completadas por el hilo