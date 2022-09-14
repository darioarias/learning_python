#         (client)          (invoker)         (command)                               
#      |-------------|      |--------|     |---------------|                                                   
#      | Application |      |  Menu  | --► |    Command    |                                                   
#      |-------------|      |--------|     | execute()     | ◄ - - - - - - - - - - - - - - |                    
#         ▲  ▲                             |---------------|                               |
#         |  |                                   ▲                                         |
#         |  |               - - - - - - - - - - | - - - - - - - - - - |                   |
#         |  |              |                    |                     |                   |     
#         |  |       |---------------|      |---------------|     |---------------|        |                                          
#         |  |       |  OpenCommand  |      |  PasteCommand |     |  MacroCommand |  - - - |                                    
#         |  | - - - | execute()     |      | execute()     |     | execute()     |                                      
#         |          |---------------|      |---------------|     |---------------|                                      
#         |                                         |   ▲                 ▲
#         |                                         |   | - - - - - - - - |
#         |                                         ▼                 (concrete commands)
#         |                                 |---------------|                                  
#         |                                 |   Document    |                
#     (Receivers) - - - - - - - - - - - - ► | insert_text() |                
#                                           |---------------|   
#              ▲ ▼ ► ◄                                            
# UML class diagram for menu-driven text editor implemented with the Command design pattern. 
# Each command may have a different receiver: the object that implements the action. 
# For PasteCommand, the receiver is the Document. For OpenCom mand, the receiver is the application.

#  Each instance of MacroCommand has an internal list of commands
class MacroCommand:
  """A command that executes a list of commands"""
  def __init__(self, commands) -> None:
    self.commands = list(commands)

  def __call__(self):
    for command in self.commands:
      command()
