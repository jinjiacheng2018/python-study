# coding: utf-8
# 使用列表与字典,通过函数封装完成一个名片管理系统,完成基本的CRUD操作
# 定义一个列表保存名片信息
list_card = []

def fn_print_menu():
    "功能：打印名片管理系统的提示信息"
    amount = 25
    print("=" * 30)
    print("欢迎来到名片管理系统 ".center(amount))
    print("1.添加一个名片".center(amount))
    print("2.删除一个名片".center(amount))
    print("3.更新一个名片".center(amount))
    print("4.查询一个名片".center(amount))
    print("5.查看所有名片".center(amount))
    print("6.安全退出系统".center(amount))
    print("=" * 30)


def fn_judge_operation():
    "功能：接收用户的输入,将字符串转换成对应的数值"
    operation_str = input("请选择需要的功能:")
    operation = 0

    if operation_str.isdigit():
        operation = int(operation_str)

    return operation


def fn_add_card():
    "功能：添加一个新的名片信息"
    new_name = input("请输入用户名：")
    new_qq = input("请输入用户QQ号码：")
    new_address = input("请输入用户的地址：")

    # 将信息添加进字典中
    dict_card = {}
    dict_card["name"] = new_name
    dict_card["qq"] = new_qq
    dict_card["address"] = new_address

    # 将字典添加进集合(全局变量)中,当列表,字典是全局变量时,要在函数中修改全局变量的值,
    # 可以不使用global来声明,同样可以更改全局变量的值,但是这样写的好处一看就知道是全局变量
    global list_card
    list_card.append(dict_card)


def fn_del_card():
    "功能：通过用户名删除一个对应的卡片信息"
    del_name = input("请输入需要删除的名片的用户名：")

    # 定义状态：判断用户是否存在
    no_user = True

    # 使用global可以声明在函数内部使用全局的变量
    global list_card
    for dict_tmp in list_card:
        if dict_tmp["name"] == del_name:
            list_card.remove(dict_tmp)
            no_user = False
            print("成功删除用户名片信息...")
            break

    # 用户不存在时需要进行反馈
    if no_user:
        print("对不起,删除的用户不存在....")


def fn_update_card():
    "功能：通过用户名更新一个用户的卡片信息"
    update_name = input("请输入需要更改的名片姓名：")

    # 判断需要更新的用户是否存在
    no_user = True

    global list_card
    for dict_tmp in list_card:
        if dict_tmp["name"] == update_name:
            update_new_name = input("请输入新的的用户姓名：")
            update_new_qq = input("请输入新的用户QQ号码：")
            update_new_address = input("请输入新的用户地址：")

            # 字典中通过键key修改对应的value值
            dict_tmp["name"] = update_new_name
            dict_tmp["qq"] = update_new_qq
            dict_tmp["address"] = update_new_address
            no_user = False
            break

    if no_user:
        print("该用户不存在,无法进行更新信息...")


def fn_query_card():
    "功能：通过用户名查询一个用户的卡片信息"
    find_name = input("请输入您需要查找的用户姓名：")

    # 定义一个状态：不存在此人
    has_user_status = True

    global list_card
    for tmp in list_card:
        if tmp["name"] == find_name:
            print("%s_%s_%s" % (tmp["name"], tmp["qq"], tmp["address"]))
            # 当查询到用户时需要更改状态信息
            has_user_status = False
            break

    # 根据状态进行反馈
    if has_user_status:
        print("查无此人...")


def fn_query_all_card():
    print("用户名\tQQ号码\t用户住址")
    for tmp_dict in list_card:
        print("%s\t%s\t%s" % (tmp_dict["name"], tmp_dict["qq"], tmp_dict["address"]))


# 定义main函数,程序的入口程序
def main():
    while True:
        # 1.调用函数打印系统提示信息
        fn_print_menu()

        # 2,用户选择指定的操作进行输入
        operation = fn_judge_operation()

        # 3,根据用户选择的操作进行对应的操作
        if operation == 1:
            # 1.添加一个名片
            fn_add_card()
        elif operation == 2:
            # 2.删除一个名片
            fn_del_card()
        elif operation == 3:
            # 3.更新一个名片
            fn_update_card()
        elif operation == 4:
            # 4.查询一个名片
            fn_query_card()
        elif operation == 5:
            # 5.查看所有名片
            fn_query_all_card()
        elif operation == 6:
            # 6.退出名片管理系统
            break
        else:
            print("您的输入有误,请输入正确的功能选项...")
        # 控制格式换行
        print()


# 调用程序的main函数
main()
print("安全退出名片管理系统....")