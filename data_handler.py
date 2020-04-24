import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story(one_user_story_id=None):
    """
    :param one_user_story_id:
        If given, it will act as a filter and return the dictionary of one specific User Story
        If not given, it will return a list of dictionaries with all the details
    """
    csv_dict_list = []
    with open(DATA_FILE_PATH, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csv_dict_list.append(row)

    if one_user_story_id is not None:
        for dictionary in csv_dict_list:
            if dictionary['id'] == str(one_user_story_id):
                return dictionary
    return csv_dict_list


def generate_id():
    max_id=0
    for row in get_all_user_story():
        if int(row['id'])>max_id:
            max_id=int(row['id'])
    return max_id +1


def add_on_csv(new_story):
    with open(DATA_FILE_PATH, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=DATA_HEADER)
        csv_writer.writerow(new_story)
    return 'New story submitted'


def update_on_csv(story_id,update_dict):

    list_of_all = get_all_user_story()
    print(list_of_all)
    with open(DATA_FILE_PATH, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=DATA_HEADER)
        csv_writer.writeheader()
        for row in list_of_all:
            if row['id'] == story_id:
                row = update_dict
            csv_writer.writerow(row)

    return "update succesfull"


