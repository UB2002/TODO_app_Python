class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            print(f'Task "{deleted_task}" deleted.')
        else:
            print('Invalid task index.')

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):           
            self.tasks[index] += ' - Completed'
            print(f'Task "{self.tasks[index]}" marked as completed.')
        else:
            print('Invalid task index.')

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("----"*10)
            print("tasks are empty")
            print("----"*10)
        else:   
            print("-----"*25)
            print('Tasks:')
            print("-----"*25)
            for i, task in enumerate(self.tasks):
                print(f'{i + 1}. {task}')


def main():
    todo_list = TodoList()

    while True:
        print('\nMenu:')
        print('1. Add Task')
        print('2. Delete Task')
        print('3. Mark Task as Completed')
        print('4. Display Tasks')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter task: ')
            todo_list.add_task(task)
        elif choice == '2':
            index = int(input('Enter task index to delete: ')) - 1
            todo_list.delete_task(index)
        elif choice == '3':
            index = int(input('Enter task index to mark as completed: ')) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
