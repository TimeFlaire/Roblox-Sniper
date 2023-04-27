import os
try:
   from rgbprint import gradient_print, Color, rgbprint
except:
    os.system("pip install rgbprint")
    
title = ("""
████████╗██╗███╗   ███╗███████╗███████╗██╗      █████╗ ██╗██████╗ ███████╗    
╚══██╔══╝██║████╗ ████║██╔════╝██╔════╝██║     ██╔══██╗██║██╔══██╗██╔════╝    
   ██║   ██║██╔████╔██║█████╗  █████╗  ██║     ███████║██║██████╔╝█████╗      
   ██║   ██║██║╚██╔╝██║██╔══╝  ██╔══╝  ██║     ██╔══██║██║██╔══██╗██╔══╝      
   ██║   ██║██║ ╚═╝ ██║███████╗██║     ███████╗██║  ██║██║██║  ██║███████╗    
   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝    
                                                                              
            ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗                      
            ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗                     
            ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝                     
            ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗                     
            ███████║██║ ╚████║██║██║     ███████╗██║  ██║                     
            ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
""")

def _print_stats(self) -> None:
        gradient_print(title, start_color=Color(0x06088c), end_color=Color(0xd200fc))
        gradient_print(f"             ★Version : 1.0.0         ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        gradient_print(f"             Designed by Timeflaire         ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        print()
        gradient_print(f"             ★ Stars found : {self.buys}       ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        gradient_print(f"             ★ Stars lost  : {self.errors}    ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        gradient_print(f"             ★ Speeds  : {self.last_time}  ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        gradient_print(f"             ★ Checks  : {self.checks}      ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        gradient_print(f"             ★ Current Stars researched  : {', '.join(self.items)} ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
        gradient_print(f"             ★ Status : {self.task} ", start_color=Color(0xd200fc), end_color=Color(0x06088c))
