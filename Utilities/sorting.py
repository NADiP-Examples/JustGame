
# Сортирует объекты для рендера по возрастанию y-координаты, чтобы те, что стоят ближе, визуально перекрывали
# те, что стоят дальше.


def get_y(obj):
    return obj.rect.y


def sort_by_y(obj_list):
    obj_list.sort(key=get_y)

#
# def get_map_y(obj):


# def sort_json(json_map):
