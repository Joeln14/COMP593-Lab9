from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_poke_info

root = Tk()

# Setting icon of master window
icon_pic = "Poké_Ball_icon.svg.ico"

root.iconbitmap(icon_pic)


root.title('Pokemon Stats Viewer')
root.resizable(False, False)



#Add grid
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, pady=(20, 20))

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(30, 15), sticky=N)

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=(15, 30), pady=(0, 30))

#Add widgets
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0, padx=(0, ), pady=20)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=(5,), pady=20)


def handle_get_info():
    #Get poke name
    poke_name = ent_name.get().strip()
    if len(poke_name) == 0:
        return
    

    

    #Get poke info from pokeapi
    poke_info = get_poke_info(poke_name)
    if poke_info is None:
        err_msg = f'Unable to fetch information for {poke_name.capitalize()} from the PokeAPI'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
        return

    types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
    types = ', '.join(types_list)

    lbl_height_val['text'] = f"{poke_info['height']} dm"
    lbl_weight_val['text'] = f"{poke_info['weight']} hg"
    lbl_type_val['text'] = f"{types}"




    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_attack['value'] = poke_info['stats'][1]['base_stat']
    bar_defence['value'] = poke_info['stats'][2]['base_stat']
    bar_special_attack['value'] = poke_info['stats'][3]['base_stat']
    bar_special_defence['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']

    return

btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info)
btn_get_info.grid(row=0, column=2, padx=(0, 20), pady=(20, 20))


#populate widget in the info frame

lbl_height = ttk.Label(frm_btm_left, text='Height: ')
lbl_height.grid(row=0, column=0, pady=(10, 5), padx=(15, 0), sticky=E)
lbl_height_val = ttk.Label(frm_btm_left, text='tbd')
lbl_height_val.grid(row=0, column=1, pady=(10, 5), padx=(0, 15))

lbl_weight = ttk.Label(frm_btm_left, text='Weight: ')
lbl_weight.grid(row=1, column=0, pady=(5, 5), padx=(15, 0), sticky=E)
lbl_weight_val = ttk.Label(frm_btm_left, text='tbd')
lbl_weight_val.grid(row=1, column=1, pady=(5, 5), padx=(0, 15))

lbl_type = ttk.Label(frm_btm_left, text='Type: ')
lbl_type.grid(row=2, column=0, pady=(5, 15), padx=(15, 0), sticky=E)
lbl_type_val = ttk.Label(frm_btm_left, text='tbd')
lbl_type_val.grid(row=2, column=1, pady=(5, 15), padx=(0, 15))


#populate widgets in stats frame

lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E)
bar_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_hp.grid(row=0, column=1, padx=(5, 10), pady=10)
bar_hp['value'] = 0

lbl_attack = ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)
bar_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_attack.grid(row=1, column=1, padx=(5, 10), pady=10)
bar_attack['value'] = 0

lbl_defence = ttk.Label(frm_btm_right, text='Defence:')
lbl_defence.grid(row=2, column=0, sticky=E)
bar_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_defence.grid(row=2, column=1, padx=(5, 10), pady=10)
bar_defence['value'] = 0

lbl_special_attack = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_special_attack.grid(row=3, column=0, sticky=E)
bar_special_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_attack.grid(row=3, column=1, padx=(5, 10), pady=10)
bar_special_attack['value'] = 0

lbl_special_defence = ttk.Label(frm_btm_right, text='Special Defence:')
lbl_special_defence.grid(row=4, column=0, padx=(10, 0), sticky=E)
bar_special_defence = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_special_defence.grid(row=4, column=1, padx=(5, 10), pady=10)
bar_special_defence['value'] = 0

lbl_speed = ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, sticky=E)
bar_speed = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
bar_speed.grid(row=5, column=1, padx=(5, 10), pady=(10, 15))
bar_speed['value'] = 0



root.mainloop()