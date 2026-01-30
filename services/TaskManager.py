
# Importa las librerías necesarias
import threading
import time
import random 

# Subclase de servicio que maneja la ejecución de las tareas con hilos
class TaskManager:
    # Constructor de la clase vacío
    def __init__(self):
        self.tareas_completadas = 0  # Atributo del contador de tareas completadas
        self.lock = threading.Lock()  # Atributo para proteger contadores

    # Método para ejecutar una tarea asignada a un hilo   
    def ejecutar_tarea(self, thread, task):
        print(f"👷 {thread.nombre} comienza tarea: {task.nombre}")
        task.estado = "EJECUTANDO"
        
        # Simular tiempo de trabajo del hilo en segundos
        tiempo_real = task.duracion * random.uniform(0.8, 1.2)
        time.sleep(tiempo_real)
        
        # Simular éxito o fallo aleatorio
        exito = random.random() > 0.1  # 90% de éxito
        
        # Condicional para determinar el estado final de la tarea
        if exito:
            task.estado = "COMPLETADA"
            task.resultado = f"Éxito en {tiempo_real:.1f}s"
            print(f"✅ {thread.nombre} completó: {task.nombre}")
        else:
            task.estado = "FALLIDA"
            task.resultado = f"Falló después de {tiempo_real:.1f}s"
            print(f"❌ {thread.nombre} falló en: {task.nombre}")
        
        # Actualizar contador de forma segura
        with self.lock:
            self.tareas_completadas += 1
            thread.tareas_completadas += 1
    
    # Método para ejecutar todas las tareas concurrentemente
    def ejecutar_tareas_concurrentes(self, threads, tasks):
        print("\n" + "="*40)
        print("🚀 INICIANDO EJECUCIÓN CON HILOS")
        print("="*40)
        # Medir tiempo de ejecución
        inicio = time.time() 
        hilos = [] # Lista para almacenar los hilos creados
        
        # Crear un hilo por cada tarea
        for i, task in enumerate(tasks):
            # Asignar hilo cíclicamente
            thread = threads[i % len(threads)] # Seleccionar el hilo
            
            # Crear el hilo
            hilo = threading.Thread(
                target=self.ejecutar_tarea,
                args=(thread, task),
                name=f"Hilo-{task.nombre}"
            )
            # Iniciar el hilo
            hilos.append(hilo)
            hilo.start()
        
        print(f"\n📊 {len(hilos)} hilos iniciados...")
        
        # Esperar a que todos los hilos terminen de ejecutarse
        for hilo in hilos:
            hilo.join()
        
        # Medir tiempo final de ejecución
        fin = time.time()
        
        # Mostrar resultados
        self.mostrar_resultados(threads, tasks, fin - inicio)
    
    # Método para mostrar los resultados de la ejecución
    def mostrar_resultados(self, threads, tasks, tiempo_total):
        print("\n" + "="*40)
        print("📊 RESULTADOS FINALES")
        print("="*40)
        
        print(f"\n⏱️  Tiempo total: {tiempo_total:.1f} segundos")
        print(f"📋 Tareas procesadas: {self.tareas_completadas} de {len(tasks)}")
        
        # Contar tareas por estado
        completadas = sum(1 for t in tasks if t.estado == "COMPLETADA")
        fallidas = sum(1 for t in tasks if t.estado == "FALLIDA")
        
        print(f"✅ Tareas exitosas: {completadas}")
        print(f"❌ Tareas fallidas: {fallidas}")
        
        print("\n💻 DESEMPEÑO DE HILOS:")
        # Bucle for para mostrar tareas completadas por cada hilo
        for thread in threads:
            print(f"  {thread.nombre}: {thread.tareas_completadas} tareas")
        
        print("\n📝 DETALLE DE TAREAS:")
        # Bucle for para mostrar el estado y resultado de cada tarea
        for task in tasks:
            print(f"  {task.nombre}: {task.estado} - {task.resultado}")