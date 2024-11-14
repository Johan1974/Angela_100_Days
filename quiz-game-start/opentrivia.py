import requests

class ClsCategory:
    def __init__(self, CatID, CatName):
        self.ID = CatID
        self.Cat = CatName

class ClsOpenTrivia:
    def __init__(self):
        self.CatID = ''
        self.CatName = ''
        self.response = ''

        #Category
        self.url_category = 'https://opentdb.com/api_category.php'
        self.LsCategory = []

        #Question Count
        self.url_question_count = 'https://opentdb.com/api_count.php?category='  #CATEGORY_ID_HERE
        self.url_question_count_global   = 'https://opentdb.com/api_count_global.php'  # Get all questions

    def ask_category(self):
        choices = []
        self.response = requests.get(self.url_category)
        if self.response.status_code == 200:
            for category in self.response.json()['trivia_categories']:
                self.LsCategory.append(ClsCategory(category['id'],category['name']))
                # Display the categories

            print("Choose a category:")
            for index, category in enumerate(self.LsCategory):
                print(f"{index + 1}. {category.Cat}")

            while True:

                try:
                    choice = int(input("Choose your Category: ")) - 1
                    if 0 <= choice < len(self.LsCategory):
                        self.CatID = self.LsCategory[choice].ID
                        self.CatName = self.LsCategory[choice].Cat
                        break  # Exit the loop if the choice is valid
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")


        else:
                print(f"Error: {self.response.status_code}")

    def question_count(self):
        if self.CatID != '':
            self.response = requests.get(self.url_question_count + str(self.CatID))
            print('\n')
        else:
            self.response = requests.get(self.url_question_count_global)

        if self.response.status_code == 200:
            print(self.response.json())
            # data = self.response.json()['category_question_count']
            # print(f"Total Questions     : {data['total_question_count']}")
            # print(f"Easy Questions      : {data['total_easy_question_count']}")
            # print(f"Medium Questions    : {data['total_medium_question_count']}")
            # print(f"Hard Questions      : {data['total_hard_question_count']}")

        else:
            print(self.response.status_code)

# {'category_id': 31, 'category_question_count': {'total_question_count': 184, 'total_easy_question_count': 59, 'total_medium_question_count': 80, 'total_hard_question_count': 45}}
