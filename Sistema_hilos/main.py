"""
PROGRAMA DE EJEMPLO SOBRE EJECUCIÓN DE TAREAS CON Y SIN HILOS

Este programa simula la ejecución de múltiples tareas realizadas por distintos hilos,
con el fin de comparar la ejecución secuencial y la ejecución concurrente mediante 
el uso de hilos en Python. A través de este ejemplo, se demuestra cómo los hilos 
permiten ejecutar varias tareas al mismo tiempo, mejorando el tiempo total de ejecución
y el aprovechamiento de los recursos del sistema.
"""

# Importa los modelos existentes del proyecto
from model.Task import Task, Thread
# Importa los servicios existentes del proyecto
from services.TaskManager import TaskManager

# Método para crear los datos
def crear_datos_ejemplo():

    # Crear hilos
    threads= [
        Thread(1, "Hilo 1"),
        Thread(2, "Hilo 2"),
        Thread(3, "Hilo 3")
    ]
    
    # Crear tareas
    tasks = [
        Task("Descargar archivo A", 2),
        Task("Procesar imagen B", 3),
        Task("Generar reporte C", 4),
        Task("Subir archivo D", 1),
        Task("Analizar datos E", 2),
        Task("Crear backup F", 3),
        Task("Enviar email G", 1),
        Task("Actualizar sistema H", 2)
    ]
    
    return threads, tasks

# Mpetodo para ejecutar las tareas una por una (sin hilos)
def ejecucion_secuencial(threads, tasks):

    print("\n" + "="*40)
    print("🐌 EJECUCIÓN SECUENCIAL (SIN HILOS)")
    print("="*40)
    
    # Importa la librería de tiempo
    import time
    inicio = time.time() 
    
    # Bucle for para ejecutar cada tarea secuencialmente
    for i, task in enumerate(tasks):
        thread = threads[i % len(threads)]
        print(f"💻 {thread.nombre} comienza: {task.nombre}")
        
        # Hilo con realización de la tarea
        time.sleep(task.duracion)
        print(f"✅ {thread.nombre} completó: {task.nombre}")
    
    # Medir tiempo final de ejecución
    fin = time.time()
    print(f"\n⏱️  Tiempo secuencial: {fin - inicio:.1f} segundos")

# Método para ejecutar las tareas concurrentemente (con hilos)
def ejecucion_con_hilos(threads, tasks):
    gestor = TaskManager()
    gestor.ejecutar_tareas_concurrentes(threads, tasks)

# Función principal del programa
def main():
    
    print("="*50)
    print("💻 SISTEMA DE HILOS")
    print("="*50)
    
    # Crear datos del objeto
    threads, tasks = crear_datos_ejemplo()
    
    # Bucle while para el menú principal
    while True:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Ver información de hilos y tareas")
        print("2. Ejecutar tareas SECUENCIALMENTE (sin hilos)")
        print("3. Ejecutar tareas CON HILOS (concurrente)")
        print("4. Ejecutar AMBAS y comparar tiempos")
        print("5. Salir")
        print("="*50)
        
        opcion = input("\nElige una opción (1-5): ")

        # Condicional para cada opción del menú
        if opcion == "1":
            print("\n💻 HILOS:")
            for t in threads:
                print(f"  - {t.nombre}")
            
            print("\n📋 TAREAS:")
            for t in tasks:
                print(f"  - {t.nombre} ({t.duracion}s)")
        
        elif opcion == "2":
            ejecucion_secuencial(threads, tasks)
        
        elif opcion == "3":
            ejecucion_con_hilos(threads, tasks)
        
        elif opcion == "4":
            print("\n" + "="*50)
            print("📊 COMPARANDO EJECUCIÓN SECUENCIAL VS CON HILOS")
            print("="*50)
            
            # Reiniciar estados
            for t in tasks:
                t.estado = "PENDIENTE"
                t.resultado = None
            
            # Ejecutar secuencialmente
            ejecucion_secuencial(threads, tasks)
            
            # Reiniciar estados por bucle for
            for t in tasks:
                t.estado = "PENDIENTE"
                t.resultado = None
            for t in threads:
                t.tareas_completadas = 0
            
            # Ejecutar con hilos
            ejecucion_con_hilos(threads, tasks)
            
            print("\n💡 CONCLUSIÓN: Los hilos permiten ejecutar")
            print("   múltiples tareas al mismo tiempo, reduciendo")
            print("   el tiempo total de ejecución.")
        
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el gestor de hilos! 🖥️")
            break
        
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()