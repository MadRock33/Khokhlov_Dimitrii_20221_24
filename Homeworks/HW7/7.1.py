def santa_list(user_list:list[list[str,int]]) -> dict:
    user_dict = {}
    for user in user_list:
        name_parts = user[0].split()
        user_name = " ".join(name_parts)
        user_index = user[1] if len(user) == 2 else None
        user_dict[user_name] = user_index
    return user_dict

if __name__ == "__main__":
    users_list = [["Маргарита Козловская"],
                  ["Ульяна Котова",336522],
                  ["Арсений Зайцев", 12354],
                  ["Артём Титов", 12435]]
    result_dict = santa_list(users_list)
    print(result_dict)


