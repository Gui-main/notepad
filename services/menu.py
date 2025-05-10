from model.functions import Functions

class Menu():
  @staticmethod
  def Options(name):
    t = Functions()
    option = str(input("""
╔════════════════════════════════════╗
║               FUNCTIONS          
  ══════════════════════════════════
║ [1] View titles                      
║ [2] View note	
║ [3] Add note                      
║ [4] Delete note                      
║ [control c + enter] To Exit                      
╚════════════════════════════════════╝
>>> """))
    if '1' in option:
      t.view_titles(name)
    elif '2' in option:
    	t.view_note(name)
    elif '3' in option:
      t.add_note(name)
    elif '4' in option:
      t.remove_note(name)
    else:
    	print('Invalid option.')