from model.tasks import Tasks 

class Menu():
  @staticmethod
  def Options(name):
    t = Tasks()
    option = str(input("""
╔════════════════════════════════════╗
║        MANAGEMENT OPTIONS         ║
╠════════════════════════════════════╣
║ [1] View tasks                    ║
║ [2] Add tasks                     ║
║ [3] Delete tasks                  ║
╚════════════════════════════════════╝
>>> """))
    if '1' in option:
      t.view_tasks(name)
    elif '2' in option:
      t.add_task(name)
    elif '3' in option:
      t.remove_task(name)