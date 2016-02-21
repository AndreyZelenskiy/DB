from application import Application


app = Application();
flag = 1
while flag:
    app.display_menu();
    menu_item = raw_input()
    if menu_item == "exit":
        flag = 0
        continue
    app.action(int(menu_item))