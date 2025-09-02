from task_manager import TaskManager

def main():
    print("--- Inicializando o gerenciador de tarefas ---")
    tm = TaskManager()

    # Adicionando tarefas
    print("\nAdicionando tarefas...")
    task1 = tm.add_task("Comprar mantimentos", "Ir ao supermercado")
    task2 = tm.add_task("Pagar contas", "Pagar a conta de luz e água")
    print(f"Tarefa adicionada: {task1}")
    print(f"Tarefa adicionada: {task2}")

    # Listando todas as tarefas
    print("\nListando todas as tarefas:")
    tasks = tm.list_tasks()
    for task in tasks:
        print(f"  - ID: {task['id']}, Título: {task['title']}, Completa: {task['completed']}")

    # Atualizando o status de uma tarefa
    print("\nAtualizando o status da tarefa 'Pagar contas'...")
    tm.update_task_status(task2["id"], True)
    task2_updated = tm.get_task(task2["id"])
    print(f"Status atualizado: {task2_updated}")

    # Deletando uma tarefa
    print("\nDeletando a tarefa 'Comprar mantimentos'...")
    tm.delete_task(task1["id"])

    # Listando as tarefas restantes
    print("\nListando tarefas restantes:")
    tasks_left = tm.list_tasks()
    if tasks_left:
        for task in tasks_left:
            print(f"  - ID: {task['id']}, Título: {task['title']}, Completa: {task['completed']}")
    else:
        print("Nenhuma tarefa restante.")

if __name__ == "__main__":
    main()
